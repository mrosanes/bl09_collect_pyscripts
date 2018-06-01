# TEST SCRIPT FOR SEEING IF IT IS POSSIBLE TO AUTOMATE A TOMO with 2 polarizations.

import numpy as np

# Filenames
file_name = 'dichro_2.txt'  
file_name_jj_one = 'dichro_jj_one_2.txt'  
file_name_jj_two = 'dichro_jj_two_2.txt'  


# NUM OF TOMOS
#num_of_tomos = 1
  

# Tomo parameters; 
# naming convention date_sampleName_JJoffset_angle_number.xrm
# FF naming convention date_sampleName_JJoffset_FF_number.xrm

date = '20180531'  
sample_name_1 = 'F80N80F80C'

binning = 1  #set your binning, unit: field of view 
exptime1 = 20  #set your exposure time, unit: second
exptime2 = 12
exptime3 = 8
exptimeFF = 3

# define energy
E = 707.4

# define sample & FF positions
X = -40
Y = -7.1
Z = -640
FF_Z = -1100
FF2_Z = Z #to come back to initial sample positions
FF_X = 1700
FF2_X = X #to come back to initiacl sample positions
#FF_Y = 100

# Define JJ_up & JJ_down
JJU_1 = 0.9 #UP
JJD_1 = -2.2 #UP
JJU_2 = -3.1 #DOWN
JJD_2 = -6.2 #DOWN
JJU_3 = 10 #to open after macro has finished
JJD_3 = -10 #to open after macro has finished
JJ_offset_1 = (JJU_1 + JJD_1) / 2.0
JJ_offset_2 = (JJU_2 + JJD_2) / 2.0

T0 = 0
Tini = -55.5
T_0 = -55
T_1 = -44
T_2 = -24
T_3 = 24
T_4 = 44
T_5 = 55

T_step1 = 1.0
T_step2 = 2.0
FF_T = -45
FF2_T = 0

# Zoneplate Values
ZPz_1 = -11306.0
ZPz_2 = -11304.5

#repetitions = 10
repetitions_FF = 50

f = open(file_name, 'w')

# Move to Energy: important for preprocessing
f.write('moveto energy %6.2f\n' %E)

#### Confirm Sample Position ####
f.write('moveto X %6.2f\n' %X) 
f.write('moveto Y %6.2f\n' %Y)
f.write('moveto Z %6.2f\n' %Z)

#### JU_1, JD_1 ###

f.write('setbinning ' + str(binning) + '\n')

f.write('moveto T %6.2f\n' %Tini)

for T in np.arange(T_0, T_1+T_step1, T_step1):
    f.write('setexp ' + str(exptime1) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    f.write('moveto ZPz %6.2f\n' %ZPz_1)
    f.write('wait 65\n')
    for j in range(25):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    f.write('moveto phy %6.2f\n' %JJD_2)
    f.write('moveto phx %6.2f\n' %JJU_2)
    f.write('moveto ZPz %6.2f\n' %ZPz_2)
    f.write('wait 65\n')
    for j in range(25):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j)) 
    T = T + T_step1

for T in np.arange(T_1+T_step1, T_2+T_step1, T_step1):
    f.write('setexp ' + str(exptime2) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    f.write('moveto ZPz %6.2f\n' %ZPz_1)
    f.write('wait 65\n')
    for j in range(20):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    f.write('moveto phy %6.2f\n' %JJD_2)
    f.write('moveto phx %6.2f\n' %JJU_2)
    f.write('moveto ZPz %6.2f\n' %ZPz_2)
    f.write('wait 65\n')
    for j in range(20):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j)) 
    T = T + T_step1

for T in np.arange(T_2+T_step2, T_3+T_step2, T_step2):
    f.write('setexp ' + str(exptime3) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    f.write('moveto ZPz %6.2f\n' %ZPz_1)
    f.write('wait 65\n')
    for j in range(15):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    f.write('moveto phy %6.2f\n' %JJD_2)
    f.write('moveto phx %6.2f\n' %JJU_2)
    f.write('moveto ZPz %6.2f\n' %ZPz_2)
    f.write('wait 65\n')
    for j in range(15):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j)) 
    T = T + T_step2

for T in np.arange(T_3+T_step1, T_4+T_step1, T_step1):
    f.write('setexp ' + str(exptime2) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    f.write('moveto ZPz %6.2f\n' %ZPz_1)
    f.write('wait 65\n')
    for j in range(20):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    f.write('moveto phy %6.2f\n' %JJD_2)
    f.write('moveto phx %6.2f\n' %JJU_2)
    f.write('moveto ZPz %6.2f\n' %ZPz_2)
    f.write('wait 65\n')
    for j in range(20):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j)) 
    T = T + T_step1

for T in np.arange(T_4+T_step1, T_5+T_step1, T_step1):
    f.write('setexp ' + str(exptime1) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    f.write('moveto ZPz %6.2f\n' %ZPz_1)
    f.write('wait 65\n')
    for j in range(25):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    f.write('moveto phy %6.2f\n' %JJD_2)
    f.write('moveto phx %6.2f\n' %JJU_2)
    f.write('moveto ZPz %6.2f\n' %ZPz_2)
    f.write('wait 65\n')
    for j in range(25):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j)) 
    T = T + T_step1

f.write('moveto T %6.2f\n' %T0)
   

# FF Acquisition
f.write('moveto T %6.2f\n' %FF_T)
f.write('moveto Z %6.2f\n' %FF_Z) 
f.write('moveto X %6.2f\n' %FF_X)
f.write('setexp ' + str(exptimeFF) + '\n')
for j in range(repetitions_FF):
    f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, "FF", j))

f.write('moveto phy %6.2f\n' %JJD_1)
f.write('moveto phx %6.2f\n' %JJU_1)
f.write('moveto ZPz %6.2f\n' %ZPz_1)
f.write('wait 65\n')
for j in range(repetitions_FF):
    f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, "FF", j))

f.write('moveto X %6.2f\n' %FF2_X)
f.write('moveto Z %6.2f\n' %FF2_Z)
f.write('moveto T %6.2f\n' %FF2_T)
f.write('moveto phy %6.2f\n' %JJD_3)
f.write('moveto phx %6.2f\n' %JJU_3)

f.close()





####### File necessary for preprocessing of second JJ positions: JJ_offset_1 ###

f = open(file_name_jj_one, 'w')

# Move to Energy: important for preprocessing
f.write('moveto energy %6.2f\n' %E)

#### Confirm Sample Position ####
f.write('moveto X %6.2f\n' %X) 
f.write('moveto Y %6.2f\n' %Y)
f.write('moveto Z %6.2f\n' %Z)
f.write('setbinning ' + str(binning) + '\n')

f.write('moveto T %6.2f\n' %Tini)

for T in np.arange(T_0, T_1+T_step1, T_step1):
    f.write('setexp ' + str(exptime1) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(25):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    T = T + T_step1

for T in np.arange(T_1+T_step1, T_2+T_step1, T_step1):
    f.write('setexp ' + str(exptime2) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(20):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    T = T + T_step1

for T in np.arange(T_2+T_step2, T_3+T_step2, T_step2):
    f.write('setexp ' + str(exptime3) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(15):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    T = T + T_step2

for T in np.arange(T_3+T_step1, T_4+T_step1, T_step1):
    f.write('setexp ' + str(exptime2) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(20):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    T = T + T_step1

for T in np.arange(T_4, T_5+T_step1, T_step1):
    f.write('setexp ' + str(exptime1) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(25):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, T, j))
    T = T + T_step1

f.write('moveto T %6.2f\n' %T0)

# FF Acquisition
f.write('moveto T %6.2f\n' %FF_T)
f.write('moveto Z %6.2f\n' %FF_Z) 
f.write('moveto X %6.2f\n' %FF_X)
f.write('setexp ' + str(exptimeFF) + '\n')
f.write('moveto phy %6.2f\n' %JJD_1)
f.write('moveto phx %6.2f\n' %JJU_1)
for j in range(repetitions_FF):
    f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_1, "FF", j))

f.close()



####### File necessary for preprocessing of second JJ positions: JJ_offset_2 ###

f = open(file_name_jj_two, 'w')

# Move to Energy: important for preprocessing
f.write('moveto energy %6.2f\n' %E)

#### Confirm Sample Position ####
f.write('moveto X %6.2f\n' %X) 
f.write('moveto Y %6.2f\n' %Y)
f.write('moveto Z %6.2f\n' %Z)
f.write('setbinning ' + str(binning) + '\n')

f.write('moveto T %6.2f\n' %Tini)

for T in np.arange(T_0, T_1+T_step1, T_step1):
    f.write('setexp ' + str(exptime1) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(25):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j))
    T = T + T_step1

for T in np.arange(T_1+T_step1, T_2+T_step1, T_step1):
    f.write('setexp ' + str(exptime2) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(20):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j))
    T = T + T_step1

for T in np.arange(T_2+T_step2, T_3+T_step2, T_step2):
    f.write('setexp ' + str(exptime3) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(15):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j))
    T = T + T_step2

for T in np.arange(T_3+T_step1, T_4+T_step1, T_step1):
    f.write('setexp ' + str(exptime2) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(20):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j))
    T = T + T_step1

for T in np.arange(T_4, T_5+T_step1, T_step1):
    f.write('setexp ' + str(exptime1) + '\n')
    f.write('moveto T %6.2f\n' %T)
    f.write('moveto phy %6.2f\n' %JJD_1)
    f.write('moveto phx %6.2f\n' %JJU_1)
    for j in range(25):
        f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, T, j))
    T = T + T_step1

###

f.write('moveto T %6.2f\n' %T0)

# FF Acquisition
f.write('moveto T %6.2f\n' %FF_T)
f.write('moveto Z %6.2f\n' %FF_Z) 
f.write('moveto X %6.2f\n' %FF_X)
f.write('setexp ' + str(exptimeFF) + '\n')
f.write('moveto phy %6.2f\n' %JJD_2)
f.write('moveto phx %6.2f\n' %JJU_2)
for j in range(repetitions_FF):
    f.write('collect {0}_{1}_{2}_{3}_{4}.xrm\n'.format(date, sample_name_1, JJ_offset_2, "FF", j))

f.close()


