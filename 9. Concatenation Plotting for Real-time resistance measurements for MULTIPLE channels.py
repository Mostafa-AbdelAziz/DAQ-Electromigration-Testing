# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:18:47 2019

@author: m8abdela
"""
import scipy.io
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.patches as mpatches

test1 = scipy.io.loadmat('191016093312Istressing_BGA_realtimeviewingtest.mat')
print(type(test1))
test2 = scipy.io.loadmat('191017010234Istressing_BGA_realtimeviewingtest.mat')
test3 = scipy.io.loadmat('191017165109Istressing_BGA_realtimeviewingtest.mat')
test4 = scipy.io.loadmat('191018092600Istressing_BGA_realtimeviewingtest.mat')
test5 = scipy.io.loadmat('191019030303Istressing_BGA_realtimeviewingtest.mat')
test6 = scipy.io.loadmat('191019214807Istressing_BGA_realtimeviewingtest.mat')
test7 = scipy.io.loadmat('191020173254Istressing_BGA_realtimeviewingtest.mat')
test8 = scipy.io.loadmat('191021141653Istressing_BGA_realtimeviewingtest.mat')
test9 = scipy.io.loadmat('191022120116Istressing_BGA_realtimeviewingtest.mat')
test10 = scipy.io.loadmat('191023104748Istressing_BGA_realtimeviewingtest.mat')
test11 = scipy.io.loadmat('191024103849Istressing_BGA_realtimeviewingtest.mat')
test12 = scipy.io.loadmat('191025113448Istressing_BGA_realtimeviewingtest.mat')
test13 = scipy.io.loadmat('191026133509Istressing_BGA_realtimeviewingtest.mat')
test14 = scipy.io.loadmat('191027164206Istressing_BGA_realtimeviewingtest.mat')
test15 = scipy.io.loadmat('191028101136Istressing_BGA_realtimeviewingtest.mat')
test16 = scipy.io.loadmat('191029102809Istressing_BGA_realtimeviewingtest.mat')
test17 = scipy.io.loadmat('191030015225Istressing_BGA_realtimeviewingtest.mat')
test18 = scipy.io.loadmat('191030173248Istressing_BGA_realtimeviewingtest.mat')
test19 = scipy.io.loadmat('191031095452Istressing_BGA_realtimeviewingtest.mat')
test20 = scipy.io.loadmat('191101031250Istressing_BGA_realtimeviewingtest.mat')

R1=test1['R']
V1=test1['V']
t1=test1['t']
T1=test1['T']
R2=test2['R']
t2=test2['t']
T2=test2['T']
R3=test3['R']
t3=test3['t']
T3=test3['T']
R4=test4['R']
t4=test4['t']
T4=test4['T']
R5=test5['R']
t5=test5['t']
T5=test5['T']
R6=test6['R']
t6=test6['t']
T6=test6['T']
R7=test7['R']
t7=test7['t']
T7=test7['T']
R8=test8['R']
t8=test8['t']
T8=test8['T']
R9=test9['R']
t9=test9['t']
T9=test9['T']
R10=test10['R']
t10=test10['t']
T10=test10['T']
R11=test11['R']
t11=test11['t']
T11=test11['T']
R12=test12['R']
t12=test12['t']
T12=test12['T']
R13=test13['R']
t13=test13['t']
T13=test13['T']
R14=test14['R']
t14=test14['t']
T14=test14['T']
R15=test15['R']
t15=test15['t']
T15=test15['T']
R16=test16['R']
t16=test16['t']
T16=test16['T']
R17=test17['R']
t17=test17['t']
T17=test17['T']
R18=test18['R']
t18=test18['t']
T18=test18['T']
R19=test19['R']
t19=test19['t']
T19=test19['T']
R20=test20['R']
t20=test20['t']
T20=test20['T']

Rtotal=np.concatenate((R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13), axis=1)
ttotal=np.concatenate((t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13), axis=1)
Ttotal=np.concatenate((T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13), axis=1)

#Analysis
Total_time_all_tests = ttotal=np.concatenate((t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20), axis=1)
Total_time_1_14 = ttotal=np.concatenate((t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14), axis=1)
Total_time_15_20 = ttotal=np.concatenate((t15,t16,t17,t18,t19,t20), axis=1)

##Plotting
## Resistance Vs. Time
#ax=plt.figure()
#plt.plot((ttotal[0]/3600),(Rtotal[0]*1000), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Time [hrs]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Resistance [mΩ]',fontsize=34)
#plt.show()
#
## Temperature Vs. Time
#ax=plt.figure()
#plt.plot((ttotal[0]/3600),(Ttotal[0]), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Time [hrs]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Temperature [°C]',fontsize=34)
#plt.show()
#
## Resistance Vs. Temperature
#ax=plt.figure()
#plt.plot((Ttotal[0]),(Rtotal[0]*1000), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Temperature [°C]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Resistance [mΩ]',fontsize=34)
#plt.show()
#
## Resistance Vs. Temperature
#ax=plt.figure()
#plt.plot((Ttotal[0,1:134000]),(Rtotal[0,1:134000]*1000), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Temperature [°C]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Resistance [mΩ]',fontsize=34)
#plt.show()
#
## Resistance & Temperature Vs. Time (2 Different Scales)
#fig, ax1 = plt.subplots()
#color = 'tab:red'
#ax1.set_xlabel('Time [hrs]', fontsize=34)
#ax1.set_ylabel('Resistance [mΩ]', color=color, fontsize=34)
#ax1.plot((ttotal[0]/3600), Rtotal[0]*1000, color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#ax2 = ax1.twinx()
#color = 'tab:blue'
#ax2.set_ylabel('Temperature [°C]', color=color, fontsize=34)
#ax2.plot((ttotal[0]/3600), Ttotal[0], color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#fig.tight_layout()
#plt.show()

##Part 2
#Rtotal_part2=np.concatenate((R16,R17,R18,R19,R20), axis=1)
#ttotal_part2=np.concatenate((t16,t17,t18,t19,t20), axis=1)
#Ttotal_part2=np.concatenate((T16,T17,T18,T19,T20), axis=1)
##Plotting
## Resistance Vs. Time
#ax=plt.figure()
#plt.plot((ttotal_part2[0]/3600),(Rtotal_part2[0]*1000), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Time [hrs]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Resistance [mΩ]',fontsize=34)
#plt.show()
#
## Temperature Vs. Time
#ax=plt.figure()
#plt.plot((ttotal_part2[0]/3600),(Ttotal_part2[0]), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Time [hrs]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Temperature [°C]',fontsize=34)
#plt.show()
#
## Resistance Vs. Temperature
#ax=plt.figure()
#plt.plot((Ttotal_part2[0]),(Rtotal_part2[0]*1000), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Temperature [°C]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Resistance [mΩ]',fontsize=34)
#plt.show()
#
## Resistance Vs. Temperature
#ax=plt.figure()
#plt.plot((Ttotal_part2[0,1:134000]),(Rtotal_part2[0,1:134000]*1000), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Temperature [°C]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Resistance [mΩ]',fontsize=34)
#plt.show()
#
## Resistance & Temperature Vs. Time (2 Different Scales)
#fig, ax1 = plt.subplots()
#color = 'tab:red'
#ax1.set_xlabel('Time [hrs]', fontsize=34)
#ax1.set_ylabel('Resistance [mΩ]', color=color, fontsize=34)
#ax1.plot((ttotal_part2[0]/3600), Rtotal_part2[0]*1000, color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#ax2 = ax1.twinx()
#color = 'tab:blue'
#ax2.set_ylabel('Temperature [°C]', color=color, fontsize=34)
#ax2.plot((ttotal_part2[0]/3600), Ttotal_part2[0], color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#fig.tight_layout()
#plt.show()

#Remove open circuit
R14_new = R14[:,0:5860]
t14_new= t14[:,0:5860]
T14_new = T14[:,0:5860]

R19_new = R19[:,0:5934]
t19_new= t19[:,0:5934]
T19_new = T19[:,0:5934]

Rtotal_part1=np.concatenate((R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14_new), axis=1)
ttotal_part1=np.concatenate((t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14_new), axis=1)
Ttotal_part1=np.concatenate((T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14_new), axis=1)
#Started test R15 and R16 but stopped and reset
Rtotal_part2=np.concatenate((R17,R18,R19_new), axis=1)
ttotal_part2=np.concatenate((t17,t18,t19_new), axis=1)
Ttotal_part2=np.concatenate((T17,T18,T19_new), axis=1)
#Add last number of t14 to t15, t16, etc...
# t14[0,5872] = 1035357.7306588
# t16[0,0] = 55456.1
# 979901.630659
# R_total.shape to get size
"""
135876 - 135885
161823 - end
"""
new_list_ttotal_part2 = [x+979901.630659 for x in ttotal_part2]

R_total_old = np.hstack((Rtotal_part1, Rtotal_part2))
t_total_old = np.hstack((ttotal_part1, new_list_ttotal_part2))
T_total_old = np.hstack((Ttotal_part1, Ttotal_part2))

R_total = R_total_old [0:135875 & 135886:171423]
t_total = t_total_old [0:135875 & 135886:171423]
T_total = T_total_old [0:135875 & 135886:171423]

## Resistance & Temperature Vs. Time (2 Different Scales)
#fig, ax1 = plt.subplots()
#color = 'tab:red'
#ax1.set_xlabel('Time [hrs]', fontsize=34)
#ax1.set_ylabel('Resistance [mΩ]', color=color, fontsize=34)
#ax1.plot((ttotal_part1[0]/3600), Rtotal_part1[0]*1000, color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#ax2 = ax1.twinx()
#color = 'tab:blue'
#ax2.set_ylabel('Temperature [°C]', color=color, fontsize=34)
#ax2.plot((ttotal_part1[0]/3600), Ttotal_part1[0], color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#fig.tight_layout()
#plt.show()

## Resistance & Temperature Vs. Time (2 Different Scales)
#fig, ax1 = plt.subplots()
#color = 'tab:red'
#ax1.set_xlabel('Time [hrs]', fontsize=34)
#ax1.set_ylabel('Resistance [mΩ]', color=color, fontsize=34)
#ax1.plot((ttotal_part2[0]/3600), Rtotal_part2[0]*1000, color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#ax2 = ax1.twinx()
#color = 'tab:blue'
#ax2.set_ylabel('Temperature [°C]', color=color, fontsize=34)
#ax2.plot((ttotal_part2[0]/3600), Ttotal_part2[0], color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#fig.tight_layout()
#plt.show()

# Resistance & Temperature Vs. Time (2 Different Scales)
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Time [h]', fontsize=34)
ax1.set_ylabel('Resistance [mΩ]', color=color, fontsize=34)
ax1.plot((t_total[0]/3600), R_total[0]*1000, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Temperature [°C]', color=color, fontsize=34)
ax2.plot((t_total[0]/3600), T_total[0], color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()

#Smooth dataset for T
from scipy.ndimage.filters import gaussian_filter1d
plt.figure()
plt.xlabel('Time [h]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Temperature [°C]',fontsize=34)
Tsmoothed = gaussian_filter1d(T_total[0], sigma=100)
Tsmoothed_addcolumn=Tsmoothed.reshape(Tsmoothed.shape+(1,))
Tsmoothed_transpose=np.transpose(Tsmoothed_addcolumn)
plt.plot(t_total[0]/3600, Tsmoothed_transpose[0])
plt.show()

#Temperature Coefficient of Resistance (TCR) Correction
#alpha_75C = 3.0844 * 10**-3
alpha_75C = 3.0844 * 10**-3

#alpha_70C = 1 * 10**-2
#R0 = R_total[0]/(1 + ((alpha_75C)*(Tsmoothed_transpose[0]-75)))
#Tsmoothed_transpose_replacement = np.full(shape=181424,fill_value=80,dtype=np.float64)
#Tsmoothed_transpose_replacement = np.full(shape=181424,fill_value=80,dtype=np.float64)
#Tsmoothed_transpose_replacement_test = Tsmoothed_transpose_replacement
#R0 = R_total[0]/(1 + ((alpha_75C)*(Tsmoothed_transpose_replacement_test[:]-75)))
#Rtest=R0.reshape(R0.shape+(1,))
#R_transpose=np.transpose(Rtest)
#R_tranpose is the same as R0

myInt = (1 + ((alpha_75C)*(80-75)))
R0 = [x / myInt for x in R_total]

#R0 = R_total/(1 + ((alpha_75C)*(80-75)))
#Rtest_1=R0.reshape(R0.shape+(1,))
#R_transpose_1=np.transpose(Rtest_1)

fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Time [h]', fontsize=34)
ax1.set_ylabel('Corrected Resistance R0 [mΩ]', color=color, fontsize=26)
ax1.plot((t_total[0]/3600), R0[0]*1000, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
ax2.set_ylim(ax1.get_ylim())
color = 'tab:blue'
ax2.set_ylabel('Original Resistance R [mΩ]', color=color, fontsize=26)
ax2.plot((t_total[0]/3600), R_total[0]*1000, color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()



#Not corrected
#fig, ax1 = plt.subplots()
#color = 'tab:red'
#ax1.set_xlabel('Time [h]', fontsize=34)
#ax1.set_ylabel('Corrected Resistance R0 [mΩ]', color=color, fontsize=26)
#ax1.plot((t_total[0]/3600), R0[0]*1000, color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#ax2 = ax1.twinx()
#ax2.set_ylim(ax1.get_ylim())
#color = 'tab:blue'
#ax2.set_ylabel('Original Resistance R [mΩ]', color=color, fontsize=26)
#ax2.plot((t_total[0]/3600), R_total[0]*1000, color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#fig.tight_layout()
#plt.show()

plt.figure()
plt.xlabel('Time [h]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance R [mΩ]',fontsize=34)
plt.plot((t_total[0]/3600), R_total[0]*1000)
plt.show()


##Corrected resistance only
#plt.figure()
#plt.xlabel('Time [hrs]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Corrected Resistance R0 [mΩ]',fontsize=34)
#plt.plot(t_total[0]/3600, R0[0]*1000)
#plt.show()
#
##Corrected resistance only
#plt.figure()
#plt.xlabel('Time [hrs]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Corrected Resistance R0 [mΩ]',fontsize=34)
#plt.plot(t_total[0]/3600, R_total[0]*1000)
#plt.show()

#Original Vs Filtered (Smooth) Temperature
#fig, ax1 = plt.subplots()
#color = 'tab:blue'
#ax1.set_xlabel('Time [hrs]', fontsize=34)
#ax1.set_ylabel('Original Temperature [°C]', color=color, fontsize=26)
#ax1.plot((t_total[0]/3600), T_total[0], color=color)
#ax1.tick_params(axis='y', labelcolor=color)
#ax2 = ax1.twinx()
#color = 'tab:red'
#ax2.set_ylabel('Corrected Temperature [°C]', color=color, fontsize=26)
#ax2.plot((t_total[0]/3600), Tsmoothed_transpose[0], color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#fig.tight_layout()
#plt.show()