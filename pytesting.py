import flapjack


user = 'dylan33smith'
passwd = 'coco33'
fj = flapjack.Flapjack('flapjack.rudge-lab.org:8000')
fj.log_in(username=user, password=passwd)

study_name = fj.get('study', name='Reporter behaviour')

# gfp_plate_1 assay has correct measurement data but is missing other information
gfp_plate_1 = fj.get('assay', name='GFP Plate 1')
# gfp_plate_2 meas data is empty becuase excel spreadsheet only has measurements for gfp_plate_1
# don't use
gfp_plate_2 = fj.get('assay', name='GFP Plate 2')

measurements = fj.measurements(assay=[gfp_plate_1.id[0]])

# data for measurements dataframe
# index for the following df's are the measurement id's
'''
Signal_id
0    3
1    7
2    3
Name: Signal_id, dtype: int64

Signal
0        GFP
1    Biomass
2        GFP
Name: Signal, dtype: object

Color
0    green
1    black
2    green
Name: Color, dtype: object

Measurement
0    0.000000
1    0.010331
2    1.953695
Name: Measurement, dtype: float64

Time
0    0.00
1    0.00
2    0.25
Name: Time, dtype: float64

Sample
0    4014
1    4014
2    4014
Name: Sample, dtype: int64

Assay
0    GFP Plate 1
1    GFP Plate 1
2    GFP Plate 1
Name: Assay, dtype: object

Study
0    Reporter behaviour
1    Reporter behaviour
2    Reporter behaviour
Name: Study, dtype: object

Media
0    M9Glucose
1    M9Glucose
2    M9Glucose
Name: Media, dtype: object

Strain
0    E.coli T7
1    E.coli T7
2    E.coli T7
Name: Strain, dtype: object

Vector
0   NaN
1   NaN
2   NaN
Name: Vector, dtype: float64

Supplement1
0   NaN
1   NaN
2   NaN
Name: Supplement1, dtype: float64

Chemical1
0   NaN
1   NaN
2   NaN
Name: Chemical1, dtype: float64

Chemical_id1
0   NaN
1   NaN
2   NaN
Name: Chemical_id1, dtype: float64

Concentration1
0   NaN
1   NaN
2   NaN
Name: Concentration1, dtype: float64

Row
0    1
1    1
2    1
Name: Row, dtype: int64

Column
0    1
1    1
2    1
Name: Column, dtype: int64

Supplement
0   NaN
1   NaN
2   NaN
Name: Supplement, dtype: float64

Chemical
1   NaN
2   NaN
Name: Chemical, dtype: float64

Chemical_id
0    [None]
1    [None]
2    [None]
Name: Chemical_id, dtype: object

'''

#vector = fj.get('vector', name='pAAA')
#media = fj.get('media', name='M9-glucose')
#strain = fj.get('strain', name='MG1655z1')
#od = fj.get('signal', name='OD')
         

                  

