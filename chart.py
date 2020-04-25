import numpy as np 

##Given
specific_volume= np.arange(start=0.8, stop=0.95, step=0.05)
relative_humidity= np.arange(start=0.1, stop=1, step=0.1)
DBT= np.arange(start=5, stop=50, step=5)
specific_humidity =np.arange(start=0, stop=0.03, step=0.01)
WBT=np.arange(start=5, stop=30, step=5)

## formulas from notes
#W= mass_watervapour/mass_dryair #specific humidity
#phi= mass_watervapour/mass_saturation# relative humidity
#h= (1.005 + 1.88*W)*t + 2500*W # enthalpy
enthalpy= []

for i in range(0,len(specific_humidity)-1):
    for j in range(0,len(DBT)-1 ):
        h=(1.005 + 1.88*specific_humidity[i])*DBT[j] + 2500*specific_humidity[i]
        enthalpy.append(h)
print(enthalpy)
        