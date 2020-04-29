#!/usr/bin/env python
#importing libraries
import numpy as np 
import matplotlib.pyplot as plt
import math 

#Given
specific_volume= [0.8,0.85,0.9,0.95]
relative_humidity= np.arange(start=0.1, stop=1.1, step=0.1)
DBT= np.arange(start=5, stop=55, step=5)

#Constants
P=101325 #Pa         #Atmospheric pressure 
Ra=287.058 #J/Kg*K   #Gas constant for air 
p=101.325 #kPa       #Atmospheric pressure 

#Variables to store plot data
x=[]
y=[]

#Calculating Saturation Pressure in Pa at a given temoerature (°C)
def p_s(t):
    return(math.exp(77.3450+0.0057*(t+273.15)-7235/(t+273.15))/pow(t+273.15,8.2))

#Plot constant relative humidity 
check=1
for i in range(0,len(relative_humidity)):
    for j in range(0,len(DBT)):
        w=.622/( (P/(p_s(DBT[j])*relative_humidity[i])) -1)
        x.append(DBT[j])
        y.append(w)
    if check==1:
        plt.plot(x,y,color='yellow', label='Constant relative humidity (%)')
        check=0
    else:
        plt.plot(x,y,color='yellow')
    x.clear()
    y.clear()
    
#Plot w=(t+5)/1000, bound for constant enthalpy 
#W in KJ/Kgda and t in°C
DBT2=np.arange(start=5, stop=52, step=.1)
for i in range (0,len(DBT2)):
    w=(DBT2[i]+5)/1000
    x.append(DBT2[i])
    y.append(w)
plt.plot(x,y,color='black')

x.clear()
y.clear()
check=1

#Plot constant enthaply(KJ/Kg(da)) 
h=np.arange(start=10, stop=110, step=10)
x.clear()
y.clear()
for i in range(0,len(h)):
    for j in range(0,len(DBT2)):
        jj=len(DBT2)-1-j
        w=(h[i]-1.0216*DBT2[jj])/2500
        if(w*1000<=5+DBT2[jj]):
            x.append(DBT2[jj])
            y.append(w)
        elif h[i]!=100:
            plt.text(DBT2[jj]-1.8,w+.0001,h[i])
            break
    if check==1:
        plt.plot(x,y,color='green', linestyle='-', label='Constant enthalpy (KJ/Kg(da))')
        check=0
    else: 
        plt.plot(x,y,color='green', linestyle='-')
    x.clear()
    y.clear()

plt.text(38,.003,'10%')
plt.text(37,.0065,'20%')
plt.text(36,.0088,'30%')
plt.text(35,.012,'40%')
plt.text(33,.014,'50%')
plt.text(32,.015,'60%')
plt.text(30,.017,'60%')
plt.text(29,.018,'70%')
plt.text(26,.019,'80%')
check=1


#Plot constant specific volume(m^3/Kg(da))
DBT2=np.arange(start=5, stop=52, step=.001)
for i in range(0, len(specific_volume)):
    v=specific_volume[i]
    phi=1
    for j in range(0,len(DBT2)):
        jj=len(DBT2)-j-1
        t=DBT2[jj]+273
        w=.622 *((P*v)/(Ra*t)-1)
        if P-Ra*t/v <p_s(t-273):
            x.append(DBT2[jj])
            y.append(w)
        else:
            w1=min(.622/( (P/(p_s(DBT2[jj])*phi)) -1), .028)
            if v!=.95:
                plt.text(DBT2[jj],w1,'%.2f'%v)
            else:
                plt.text(44,w1,'%.2f'%v)
            break
    if check==1:
        plt.plot(x,y,color='blue', linestyle='--', label='Constant specific volume (m^3/Kg(da))')
        check=0
    else:
        plt.plot(x,y,color='blue', linestyle='--')
    x.clear()
    y.clear()

#Plot parameters
plt.xlim(5, 50)  #Limits of DBT
plt.ylim(0, .03) #Limits of specific humidity
plt.title('Psychometric chart')
plt.tick_params(axis='y',which='both',labelleft=1, labelright=1) 
plt.xlabel('Dry Bulb Temperature (°C)')
plt.ylabel('Specific Humidity (kg/kg(da))')
plt.legend(loc='upper center',bbox_to_anchor=(0.55,-0.2),shadow='True',ncol=2)
plt.show()