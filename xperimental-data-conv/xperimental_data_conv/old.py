import excel2flapjack.main as e2f
import excel2sbol.converter as conv
import sbol2
import tempfile
import requests
import os
      

fj_user = ""
fj_pass = ""
sbh_pass = ''
sbh_user = ''


direct = os.path.split(__file__)[0]
file_path_in = os.path.join(direct, 'flapjack_excel_converter_v029.xlsx')
sbh_overwrite = '0'
sbh_collec = 'Flapjack'

def experimental_data_uploader(file_path_in, fj_user, fj_pass,
                               sbh_user, sbh_pass, sbh_collec, sbh_overwrite):

    # create temporary directory to write intermediate files to
    temp_dir = tempfile.TemporaryDirectory()
    file_path_out = os.path.join(temp_dir.name, 'test.xml')
    file_path_out2 = os.path.join(temp_dir.name, 'test1.xml')


    # upload the excel file to flapjack and get hash map back
    fj_url = "flapjack.rudge-lab.org:8000"
    hash_map = e2f.flapjack_upload(fj_url, fj_user, fj_pass, file_path_in)
    # print(hash_map)

    # convert the excel file to SBOL
    # use excel2sbol - could ask for an update that just gives the doc back rather than the file
    conv.converter(file_path_in, file_path_out)

    # Add flapjack annotations to the SBOL
    doc = sbol2.Document()
    doc.read(file_path_out)
    for tl in doc:
        id = str(tl).split('/')[-2]
        if id in hash_map:
            tl.setPropertyValue('https://flapjack.rudge-lab.org/ID', f'http://wwww.flapjack.com/{hash_map[id]}')
    doc.write(file_path_out2)

    # SBH Login
    response = requests.post(
        'https://synbiohub.org/login',
        headers={'Accept': 'text/plain'},
        data={
            'email': sbh_user,
            'password' : sbh_pass,
            }
    )
    x_token = response.text

    # SBH file upload
    response = requests.post(
        'https://synbiohub.org/submit',
        headers={
            'Accept': 'text/plain',
            'X-authorization': x_token
        },
        files={
        'files': open(file_path_out2,'rb'),
        },
        data={
            'id': sbh_collec,
            'version' : '1',
            'name' : sbh_collec,
            'description' : 'Description stuff',
            'overwrite_merge' : sbh_overwrite
        },

    )

    if response.text == "Submission id and version already in use":
        print('not submitted')
        raise AttributeError(f'The collection ({sbh_collec}) could not be submitted to synbiohub as the collection already exists and overite is not on')
    # if response.text == "Successfully uploaded":
    #     print('Yay')

    # Pull collection uri from synbiohub
    response = requests.get(
        'https://synbiohub.org/manage',
        headers={
            'Accept': 'text/plain',
            'X-authorization': x_token
            },
    )

    for collection in list(response.json()):
        if collection['name'] == sbh_collec:
            collec_uri = collection['uri']

    # get collection sbol
    response = requests.get(
        f'{collec_uri}/sbol',
        headers={
            'Accept': 'text/plain',
            'X-authorization': x_token
            },
    )
    with open(file_path_out2, 'wb') as f:
        f.write(response.content)

    # Parse sbol to create hashmap of flapjack id to sbol uri
    doc = sbol2.Document()
    doc.read(file_path_out2)

    sbol_hash_map = {}
    for tl in doc:
        id = str(tl)
        if 'https://flapjack.rudge-lab.org/ID' in tl.properties:
            fj_id = tl.properties['https://flapjack.rudge-lab.org/ID'][0].split('/')[-1]
            sbol_hash_map[fj_id] = id

    # Add uris to flapjack
    return(collec_uri, sbol_hash_map)
    