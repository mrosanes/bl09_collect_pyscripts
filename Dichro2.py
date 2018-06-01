# TEST SCRIPT FOR SEEING IF IT IS POSSIBLE TO AUTOMATE A TOMO with 2 polarizations.

import numpy as np

# Filename
file_name = 'dichro2.txt'  

# NUM OF TOMOS
#num_of_tomos = 1
  

# Tomo parameters; 
# naming convention date_sampleName_JJoffset_angle_number.xrm
# FF naming convention date_sampleName_JJoffset_FF_number.xrm

date = '20180529'  
sample_name_1 = 'name'

binning = 1  #set your binning, unit: field of view 
exptime1 = 3  #set your exposure time, unit: second
exptime2 = 3
exptime3 = 3
exptimeFF = 3

# define energy
energy = 708.5

# define sample & FF positions
X = 219.6
Y = 435.3
Z = -414.9
FF_X = 100
FF_Y = 100

# Define JJ_up & JJ_down
JJU_1 = -1
JJD_1 = -3
JJU_2 = 1
JJD_2 = 3
JJ_offset_1 = (JJU_1 + JJD_1) / 2.0
JJ_offset_2 = (JJU_2 + JJD_2) / 2.0

T0 = 0
Tini = -55
T_0 = -54
T_1 = -40
T_2 = 40
T_3 = 54
T_step = 2.0

f = open(file_name, 'w')

# Move to Energy: important for preprocessing
f.write('moveto energy %6.2f\n' %energy)

#### Confirm Sample Position ####
f.write('moveto X %6.2f\n' %X) 
f.write('moveto Y %6.2f\n' %Y)
f.write('moveto Z %6.2f\n' %Z)

#### JU_1, JD_1 ###

f.write('setbinning ' + str(binning) + '\n')

f.write('moveto T %6.2f\n' %Tini)

for T in np.arange(T_0, T_1+T_step, T_step):
    f.write('setexp ' + str(exptime1) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJU_1)
    f.write('moveto phx %6.2f\n' %JJD_1)
    f.write('wait 60\n')
    for j in range(10):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    f.write('moveto phy %6.2f\n' %JJU_2)
    f.write('moveto phx %6.2f\n' %JJD_2)
    f.write('wait 60\n')
    for j in range(10):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j)) 
    T = T + T_step

for T in np.arange(T_1+T_step, T_2+T_step, T_step):
    f.write('setexp ' + str(exptime2) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJU_1)
    f.write('moveto phx %6.2f\n' %JJD_1)
    f.write('wait 60\n')
    for j in range(10   ):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    f.write('moveto phy %6.2f\n' %JJU_2)
    f.write('moveto phx %6.2f\n' %JJD_2)
    f.write('wait 60\n')
    for j in range(10):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j)) 
    T = T + T_step

for T in np.arange(T_2+T_step, T_3+T_step, T_step):
    f.write('setexp ' + str(exptime3) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJU_1)
    f.write('moveto phx %6.2f\n' %JJD_1)
    f.write('wait 60\n')
    for j in range(10):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    f.write('moveto phy %6.2f\n' %JJU_2)
    f.write('moveto phx %6.2f\n' %JJD_2)
    f.write('wait 60\n')
    for j in range(10):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j)) 
    T = T + T_step

f.write('moveto T %6.2f\n' %T0)
   

# FF Acquisition
f.write('moveto X %6.2f\n' %FF_X) 
f.write('moveto Y %6.2f\n' %FF_Y)
f.write('setexp ' + str(exptimeFF) + '\n')
for j in range(10):
    f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, "FF", j))

f.write('moveto phy %6.2f\n' %JJU_1)
f.write('moveto phx %6.2f\n' %JJD_1)
f.write('wait 60\n')
for j in range(10):
    f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, "FF", j))

f.close()


