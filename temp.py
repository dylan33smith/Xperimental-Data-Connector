from sre_constants import SUCCESS
from base.xperimental_data_conv.main import experimental_data_uploader as xdc
import os

fj_user = "dylan33smith"
fj_pass = "coco33"
sbh_pass = 'dylan33smith'
sbh_user = 'coco33'

# sbh_instance = "https://synbiohub.org/"
sbh_instance = "https://synbiohub.colorado.edu"
fj_instance = "flapjack.rudge-lab.org"

direct = os.path.split(__file__)[0]
file_path_in = os.path.join(direct, 'base','tests','test_files', 'flapjack_excel_converter_v030.xlsx')
sbh_overwrite = '1'
# sbh_collec is what you want to name the collection in sbh
sbh_collec = 'Flapjack'

'''
print("\n")
print("direct: ", direct)
print("\n")
print("file_path_in:", file_path_in)
print("\n")'''


sbol_collec_url = xdc(sbh_instance, fj_instance, file_path_in, fj_user, fj_pass, sbh_pass, sbh_user, sbh_collec, sbh_overwrite=True, fj_overwrite=True)
