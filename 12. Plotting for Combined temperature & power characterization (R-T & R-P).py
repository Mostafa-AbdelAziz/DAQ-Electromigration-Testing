# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:43:57 2019

@author: Mostafa & Anna
"""

import scipy.io
import matplotlib.pyplot as plt 

test1 = scipy.io.loadmat('190720162616BGA_PCB_SAC305_Accelerated Temp & Power Characterization.mat')

I=test1['I']
Ilevels=test1['Ilevels']
thold=test1['thold']
R_RP=test1['R_RP']
I_RP=test1['I_RP'] 
V_RP=test1['V_RP'] 
t_RP=test1['t_RP'] 
P_RP=test1['P_RP'] 
R_RT=test1['R_RT'] 
T_RT=test1['T_RT']
t_RT=test1['t_RT']
tTempStage=test1['tTempStage']
tWaitStage=test1['tWaitStage']
tRTStage=test1['tRTStage']
tRPStage=test1['tRPStage']
V=test1['V']
R=test1['R']
t=test1['t']
P=test1['P']
T=test1['T']

color=['b','b--','g','g--','r','r--','c','c--','m','m--','y','y--','k','k--','b','b--']
color_even=['b--','g--','r--','c--','m--','y--','k--','b--']
color_odd=['b','g','r','c','m','y','k','b']
R_even=R[1::2]
R_odd=R[::2]
R_RP_even=R_RP[1::2]
R_RP_odd=R_RP[::2]
P_RP_even=P_RP[1::2]
P_RP_odd=P_RP[::2]


# Temperature Vs. Time
ax=plt.figure(figsize=(16,9)) 
plt.plot((t[0][0:])/3600,(T[0][0:]))
plt.ylabel('Temperature [°C]', fontsize=28)
plt.xlabel('Time [Hr]', fontsize=28)
plt.rcParams['xtick.labelsize']=28
plt.rcParams['ytick.labelsize']=28
plt.show()

# Resistance Vs. Time (Plot with Different Scale for Even/Odd)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax.legend(fontsize=18)
for a in range (8):
    label_even='Even Channel' + str(2*a+2)
    label_odd='Odd Channel' + str(2*a+1)
    ax1.plot((t[0][0:])/3600, (R_even[a][0:])*1000, '%s' %color_even[a],label='%s' %label_even)
    ax2.plot((t[0][0:])/3600, (R_odd[a][0:])*1000, '%s' %color_odd[a],label='%s' %label_odd)
ax1.legend()
ax2.legend()
ax1.set_xlabel('Time [Hr]', fontsize=28)
ax1.set_ylabel('Even CH Resistance [mΩ]', fontsize=20)
ax1.tick_params(axis='y')
ax2.set_ylabel('Odd CH [Solder] Resistance [mΩ]', fontsize=20)  # we already handled the x-label with ax1
ax2.tick_params(axis='y')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
ax.legend(fontsize=18)
plt.show()
    
# Resistance Vs. Temperature (Plot with Different Scale for Even/Odd)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax.legend(fontsize=18)
for a in range (8):
    label_even='Even Channel' + str(2*a+2)
    label_odd='Odd Channel' + str(2*a+1)
    ax1.plot((T[0][0:]), (R_even[a][0:])*1000, '%s' %color_even[a],label='%s' %label_even)
    ax2.plot((T[0][0:]), (R_odd[a][0:])*1000, '%s' %color_odd[a],label='%s' %label_odd)
ax1.legend()
ax2.legend()
ax1.set_xlabel('Temperature [°C]', fontsize=28)
ax1.set_ylabel('Even CH Resistance [mΩ]', fontsize=20)
ax1.tick_params(axis='y')
ax2.set_ylabel('Odd CH [Solder] Resistance [mΩ]', fontsize=20)  # we already handled the x-label with ax1
ax2.tick_params(axis='y')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
ax.legend(fontsize=18)
plt.show()




# Current Vs. Time
ax=plt.figure() 
for k in range (16):  
        label='Channel' + str(k+1)
        plt.plot((t_RP[0][0:]/3600),(I_RP[0][0:]), '%s' %color[k],label='%s' %label)
plt.xlabel('Time [Hr]', fontsize=28)
plt.rcParams['xtick.labelsize']=28
plt.rcParams['ytick.labelsize']=28
plt.ylabel('Current [A]',fontsize=28)
plt.show()

# Power Vs Time (Channel 6)
ax=plt.figure() 
for k in range (16):  
        label='Channel' + str(k+1)
        plt.plot((t_RP[0][0:]),(P[k][0:]*1000), '%s' %color[k],label='%s' %label)
plt.xlabel('Time [Hr]', fontsize=28)
plt.rcParams['xtick.labelsize']=28
plt.rcParams['ytick.labelsize']=28
plt.ylabel('Power [mW]',fontsize=28)
plt.show()

# Resistance Vs. Power (Channel 6)
ax=plt.figure() 
for k in range (16):  
        label='Channel' + str(k+1)
        plt.plot((P_RP[5][0:]*1000),(R_RP[5][0:]*1000), '%s' %color[k],label='%s' %label)
plt.xlabel('Power [mW]', fontsize=28)
plt.rcParams['xtick.labelsize']=28
plt.rcParams['ytick.labelsize']=28
plt.ylabel('Resistance [mΩ]',fontsize=28)
plt.show()

# Resistance Vs. Power (Plot with Different Scale for Even/Odd)
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax.legend(fontsize=18)
for a in range (8):
    label_even='Even Channel' + str(2*a+2)
    label_odd='Odd Channel' + str(2*a+1)
    ax1.plot((P_RP_even[a][0:]*1000), (R_RP_even[a][0:])*1000, '%s' %color_even[a],label='%s' %label_even)
    ax2.plot((P_RP_odd[a][0:]*1000), (R_RP_odd[a][0:])*1000, '%s' %color_odd[a],label='%s' %label_odd)
ax1.legend()
ax2.legend()
ax1.set_xlabel('Power [mW]', fontsize=28)
ax1.set_ylabel('Even CH Resistance [mΩ]', fontsize=20)
ax1.tick_params(axis='y')
ax2.set_ylabel('Odd CH [Solder] Resistance [mΩ]', fontsize=20)  # we already handled the x-label with ax1
ax2.tick_params(axis='y')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
ax.legend(fontsize=18)
plt.show()




## Power Vs. Temperature
#ax=plt.figure() 
#for k in range (16):  
#        label='Channel' + str(k+1)
#        plt.plot((T[0][0:]),(R[k][0:]*I[k][0]*I[k][0]*1000), '%s' %color[k],label='%s' %label)
#plt.xlabel('Temperature [°C]', fontsize=28)
#plt.rcParams['xtick.labelsize']=28
#plt.rcParams['ytick.labelsize']=28
#plt.ylabel('Power [mW]',fontsize=28)
#plt.show()

# Resistance Vs. Time (All Channels)
#ax=plt.figure() 
#for k in range (16):  
#        label='Channel' + str(k+1)
#        plt.plot((t[0][0:])/3600,(R[k][0:])*1000, '%s' %color[k],label='%s' %label)
#ax.legend(fontsize=18)
#plt.xlabel('Time [Hr]', fontsize=28)
#plt.rcParams['xtick.labelsize']=28
#plt.rcParams['ytick.labelsize']=28
#plt.ylabel('Resistance [mΩ]',fontsize=28)
#plt.show()

## Resistance Vs. Temperature (All Channels)
#ax=plt.figure() 
#for k in range (16):  
#        label='Channel' + str(k+1)
#        plt.plot((T[0][0:]),(R[k][0:]*1000), '%s' %color[k],label='%s' %label)
#ax.legend(fontsize=18)
#plt.xlabel('Temperature [℃]', fontsize=28)
#plt.rcParams['xtick.labelsize']=28
#plt.rcParams['ytick.labelsize']=28
#plt.ylabel('Resistance [mΩ]',fontsize=28)
#plt.show()

## Temperature Vs. Power
#ax=plt.figure() 
#for k in range (16):  
#        label='Channel' + str(k+1)
#        plt.plot((R[k][0:]*I[k][0]*I[k][0],(T[0][0:])), '%s' %color[k],label='%s' %label)
#plt.ylabel('Temperature [°C]', fontsize=24)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=28
#plt.xlabel('Power [W]',fontsize=24)
#plt.show()
