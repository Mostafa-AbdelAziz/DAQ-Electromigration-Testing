# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:36:31 2020

@author: m8abdela
"""
# MIJO 34
from itertools import chain
import scipy.io
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.patches as mpatches

test1 = scipy.io.loadmat('201113131436Resistance Measurements of SAC305 flip chip after reflow Tresky_Sample 1.mat')
print(type(test1))
test2 = scipy.io.loadmat('201113131740Resistance Measurements of SAC305 flip chip after reflow Tresky_Sample 2.mat')
test5 = scipy.io.loadmat('201113132029Resistance Measurements of SAC305 flip chip after reflow Tresky_Sample 5.mat')
test7 = scipy.io.loadmat('201113132346Resistance Measurements of SAC305 flip chip after reflow Tresky_Sample 7.mat')
test8 = scipy.io.loadmat('201113132651Resistance Measurements of SAC305 flip chip after reflow Tresky_Sample 8.mat')
test9 = scipy.io.loadmat('201113133020Resistance Measurements of SAC305 flip chip after reflow Tresky_Sample 9.mat')
test10 = scipy.io.loadmat('201113133349Resistance Measurements of SAC305 flip chip after reflow Tresky_Sample 10.mat')
test4 = scipy.io.loadmat('201113133720Resistance Measurements of SAC305 flip chip after reflow Tresky_Sample 4.mat')

channel2=['@201','@202','@203','@204','@205','@206','@207','@208','@209','@210','@211','@212','@213','@214','@215','@216']
color=['b','b--','g','g--','r','r--','c','c--','m','m--','y','y--','k','k--','b-.','b:']

#Test 1
R1=test1['R']
t1=test1['t']
T1_1=test1['T1']
T2_1=test1['T2']
Vpcb2_1=test1['Vpcb2']
#Test 2
R2=test2['R']
t2=test2['t']
T1_2=test2['T1']
T2_2=test2['T2']
Vpcb2_2=test2['Vpcb2']
#Test 5
R5=test5['R']
t5=test5['t']
T1_5=test5['T1']
T2_5=test5['T2']
Vpcb2_5=test5['Vpcb2']
#Test 7
R7=test7['R']
t7=test7['t']
T1_7=test7['T1']
T2_7=test7['T2']
Vpcb2_7=test7['Vpcb2']
#Test 8
R8=test8['R']
t8=test8['t']
T1_8=test8['T1']
T2_8=test8['T2']
Vpcb2_8=test8['Vpcb2']
#Test 9
R9=test9['R']
t9=test9['t']
T1_9=test9['T1']
T2_9=test9['T2']
Vpcb2_9=test9['Vpcb2']
#Test 10
R10=test10['R']
t10=test10['t']
T1_10=test10['T1']
T2_10=test10['T2']
Vpcb2_10=test10['Vpcb2']
#Test 4
R4=test4['R']
t4=test4['t']
T1_4=test4['T1']
T2_4=test4['T2']
Vpcb2_4=test4['Vpcb2']

Rtotal=np.concatenate((R1,R2,R5,R7,R8,R9,R10,R4), axis=1)
ttotal=np.concatenate((t1,t2,t5,t7,t8,t9,t10,t4), axis=1)
T1total=np.concatenate((T1_1,T1_2,T1_5,T1_7,T1_8,T1_9,T1_10,T1_4), axis=1)
T2total=np.concatenate((T2_1,T2_2,T2_5,T2_7,T2_8,T2_9,T2_10,T2_4), axis=1)
Vpcb2_total=np.concatenate((Vpcb2_1,Vpcb2_2,Vpcb2_5,Vpcb2_7,Vpcb2_8,Vpcb2_9,Vpcb2_10,Vpcb2_4), axis=1)

#Plotting

#Sample 1
#Remove CH 4, 11, 14, 15
ax=plt.figure()
plt.plot(t1[0],Vpcb2_1[0]/0.1*1000*-1, '%s' %color[0], label='Channel' + str(0+1))
plt.plot(t1[0],Vpcb2_1[1]/0.1*1000*-1, '%s' %color[1], label='Channel' + str(1+1))
plt.plot(t1[0],Vpcb2_1[2]/0.1*1000*-1, '%s' %color[2], label='Channel' + str(2+1))
#plt.plot(t1[0],Vpcb2_1[3]/0.1*1000*-1, '%s' %color[3], label='Channel' + str(3+1))
plt.plot(t1[0],Vpcb2_1[4]/0.1*1000*-1, '%s' %color[4], label='Channel' + str(4+1))
plt.plot(t1[0],Vpcb2_1[5]/0.1*1000*-1, '%s' %color[5], label='Channel' + str(5+1))
plt.plot(t1[0],Vpcb2_1[6]/0.1*1000*-1, '%s' %color[6], label='Channel' + str(6+1))
plt.plot(t1[0],Vpcb2_1[7]/0.1*1000*-1, '%s' %color[7], label='Channel' + str(7+1))
plt.plot(t1[0],Vpcb2_1[8]/0.1*1000*-1, '%s' %color[8], label='Channel' + str(8+1))
plt.plot(t1[0],Vpcb2_1[9]/0.1*1000*-1, '%s' %color[9], label='Channel' + str(9+1))
#plt.plot(t1[0],Vpcb2_1[10]/0.1*1000*-1, '%s' %color[10], label='Channel' + str(10+1))
#plt.plot(t1[0],Vpcb2_1[11]/0.1*1000*-1, '%s' %color[11], label='Channel' + str(11+1))
#plt.plot(t1[0],Vpcb2_1[12]/0.1*1000*-1, '%s' %color[12], label='Channel' + str(12+1))
#plt.plot(t1[0],Vpcb2_1[13]/0.1*1000*-1, '%s' %color[13], label='Channel' + str(13+1))
#plt.plot(t1[0],Vpcb2_1[14]/0.1*1000*-1, '%s' %color[14], label='Channel' + str(14+1))
plt.plot(t1[0],Vpcb2_1[15]/0.1*1000*-1, '%s' %color[15], label='Channel' + str(15+1))
plt.title(label="Resistance Sample 1 after reflow (solder balls, Tresky)", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance [mΩ]',fontsize=34)
plt.show()


#Sample 2
#Remove CH 4, 11, 14, 15
ax=plt.figure()
#plt.plot(t1[0],Vpcb2_2[0]/0.1*1000*-1, '%s' %color[0], label='Channel' + str(0+1))
plt.plot(t1[0],Vpcb2_2[1]/0.1*1000*-1, '%s' %color[1], label='Channel' + str(1+1))
plt.plot(t1[0],Vpcb2_2[2]/0.1*1000*-1, '%s' %color[2], label='Channel' + str(2+1))
#plt.plot(t1[0],Vpcb2_2[3]/0.1*1000*-1, '%s' %color[3], label='Channel' + str(3+1))
plt.plot(t1[0],Vpcb2_2[4]/0.1*1000*-1, '%s' %color[4], label='Channel' + str(4+1))
plt.plot(t1[0],Vpcb2_2[5]/0.1*1000*-1, '%s' %color[5], label='Channel' + str(5+1))
plt.plot(t1[0],Vpcb2_2[6]/0.1*1000*-1, '%s' %color[6], label='Channel' + str(6+1))
plt.plot(t1[0],Vpcb2_2[7]/0.1*1000*-1, '%s' %color[7], label='Channel' + str(7+1))
plt.plot(t1[0],Vpcb2_2[8]/0.1*1000*-1, '%s' %color[8], label='Channel' + str(8+1))
plt.plot(t1[0],Vpcb2_2[9]/0.1*1000*-1, '%s' %color[9], label='Channel' + str(9+1))
plt.plot(t1[0],Vpcb2_2[10]/0.1*1000*-1, '%s' %color[10], label='Channel' + str(10+1))
#plt.plot(t1[0],Vpcb2_2[11]/0.1*1000*-1, '%s' %color[11], label='Channel' + str(11+1))
plt.plot(t1[0],Vpcb2_2[12]/0.1*1000*-1, '%s' %color[12], label='Channel' + str(12+1))
plt.plot(t1[0],Vpcb2_2[13]/0.1*1000*-1, '%s' %color[13], label='Channel' + str(13+1))
plt.plot(t1[0],Vpcb2_2[14]/0.1*1000*-1, '%s' %color[14], label='Channel' + str(14+1))
#plt.plot(t1[0],Vpcb2_2[15]/0.1*1000*-1, '%s' %color[15], label='Channel' + str(15+1))
plt.title(label="Resistance Sample 2 after reflow (solder balls, Tresky)", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance [mΩ]',fontsize=34)
plt.show()


#Sample 5
#Remove CH 4, 11, 14, 15
ax=plt.figure()
#plt.plot(t1[0],Vpcb2_5[0]/0.1*1000*-1, '%s' %color[0], label='Channel' + str(0+1))
#plt.plot(t1[0],Vpcb2_5[1]/0.1*1000*-1, '%s' %color[1], label='Channel' + str(1+1))
plt.plot(t1[0],Vpcb2_5[2]/0.1*1000*-1, '%s' %color[2], label='Channel' + str(2+1))
#plt.plot(t1[0],Vpcb2_5[3]/0.1*1000*-1, '%s' %color[3], label='Channel' + str(3+1))
plt.plot(t1[0],Vpcb2_5[4]/0.1*1000*-1, '%s' %color[4], label='Channel' + str(4+1))
plt.plot(t1[0],Vpcb2_5[5]/0.1*1000*-1, '%s' %color[5], label='Channel' + str(5+1))
plt.plot(t1[0],Vpcb2_5[6]/0.1*1000*-1, '%s' %color[6], label='Channel' + str(6+1))
plt.plot(t1[0],Vpcb2_5[7]/0.1*1000*-1, '%s' %color[7], label='Channel' + str(7+1))
plt.plot(t1[0],Vpcb2_5[8]/0.1*1000*-1, '%s' %color[8], label='Channel' + str(8+1))
#plt.plot(t1[0],Vpcb2_5[9]/0.1*1000*-1, '%s' %color[9], label='Channel' + str(9+1))
#plt.plot(t1[0],Vpcb2_5[10]/0.1*1000*-1, '%s' %color[10], label='Channel' + str(10+1))
#plt.plot(t1[0],Vpcb2_5[11]/0.1*1000*-1, '%s' %color[11], label='Channel' + str(11+1))
#plt.plot(t1[0],Vpcb2_5[12]/0.1*1000*-1, '%s' %color[12], label='Channel' + str(12+1))
plt.plot(t1[0],Vpcb2_5[13]/0.1*1000*-1, '%s' %color[13], label='Channel' + str(13+1))
plt.plot(t1[0],Vpcb2_5[14]/0.1*1000*-1, '%s' %color[14], label='Channel' + str(14+1))
plt.plot(t1[0],Vpcb2_5[15]/0.1*1000*-1, '%s' %color[15], label='Channel' + str(15+1))
plt.title(label="Resistance Sample 5 after reflow (solder balls, Tresky)", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance [mΩ]',fontsize=34)
plt.show()


#Sample 7
#Remove CH 4, 11, 14, 15
ax=plt.figure()
#plt.plot(t1[0],Vpcb2_7[0]/0.1*1000*-1, '%s' %color[0], label='Channel' + str(0+1))
plt.plot(t1[0],Vpcb2_7[1]/0.1*1000*-1, '%s' %color[1], label='Channel' + str(1+1))
plt.plot(t1[0],Vpcb2_7[2]/0.1*1000*-1, '%s' %color[2], label='Channel' + str(2+1))
#plt.plot(t1[0],Vpcb2_7[3]/0.1*1000*-1, '%s' %color[3], label='Channel' + str(3+1))
plt.plot(t1[0],Vpcb2_7[4]/0.1*1000*-1, '%s' %color[4], label='Channel' + str(4+1))
plt.plot(t1[0],Vpcb2_7[5]/0.1*1000*-1, '%s' %color[5], label='Channel' + str(5+1))
plt.plot(t1[0],Vpcb2_7[6]/0.1*1000*-1, '%s' %color[6], label='Channel' + str(6+1))
plt.plot(t1[0],Vpcb2_7[7]/0.1*1000*-1, '%s' %color[7], label='Channel' + str(7+1))
#plt.plot(t1[0],Vpcb2_7[8]/0.1*1000*-1, '%s' %color[8], label='Channel' + str(8+1))
plt.plot(t1[0],Vpcb2_7[9]/0.1*1000*-1, '%s' %color[9], label='Channel' + str(9+1))
#plt.plot(t1[0],Vpcb2_7[10]/0.1*1000*-1, '%s' %color[10], label='Channel' + str(10+1))
#plt.plot(t1[0],Vpcb2_7[11]/0.1*1000*-1, '%s' %color[11], label='Channel' + str(11+1))
plt.plot(t1[0],Vpcb2_7[12]/0.1*1000*-1, '%s' %color[12], label='Channel' + str(12+1))
plt.plot(t1[0],Vpcb2_7[13]/0.1*1000*-1, '%s' %color[13], label='Channel' + str(13+1))
plt.plot(t1[0],Vpcb2_7[14]/0.1*1000*-1, '%s' %color[14], label='Channel' + str(14+1))
plt.plot(t1[0],Vpcb2_7[15]/0.1*1000*-1, '%s' %color[15], label='Channel' + str(15+1))
plt.title(label="Resistance Sample 7 after reflow (solder balls, Tresky)", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance [mΩ]',fontsize=34)
plt.show()


#Sample 8
#Remove CH 4, 11, 14, 15
ax=plt.figure()
plt.plot(t1[0],Vpcb2_8[0]/0.1*1000*-1, '%s' %color[0], label='Channel' + str(0+1))
plt.plot(t1[0],Vpcb2_8[1]/0.1*1000*-1, '%s' %color[1], label='Channel' + str(1+1))
plt.plot(t1[0],Vpcb2_8[2]/0.1*1000*-1, '%s' %color[2], label='Channel' + str(2+1))
plt.plot(t1[0],Vpcb2_8[3]/0.1*1000*-1, '%s' %color[3], label='Channel' + str(3+1))
plt.plot(t1[0],Vpcb2_8[4]/0.1*1000*-1, '%s' %color[4], label='Channel' + str(4+1))
plt.plot(t1[0],Vpcb2_8[5]/0.1*1000*-1, '%s' %color[5], label='Channel' + str(5+1))
plt.plot(t1[0],Vpcb2_8[6]/0.1*1000*-1, '%s' %color[6], label='Channel' + str(6+1))
plt.plot(t1[0],Vpcb2_8[7]/0.1*1000*-1, '%s' %color[7], label='Channel' + str(7+1))
#plt.plot(t1[0],Vpcb2_8[8]/0.1*1000*-1, '%s' %color[8], label='Channel' + str(8+1))
#plt.plot(t1[0],Vpcb2_8[9]/0.1*1000*-1, '%s' %color[9], label='Channel' + str(9+1))
plt.plot(t1[0],Vpcb2_8[10]/0.1*1000*-1, '%s' %color[10], label='Channel' + str(10+1))
plt.plot(t1[0],Vpcb2_8[11]/0.1*1000*-1, '%s' %color[11], label='Channel' + str(11+1))
plt.plot(t1[0],Vpcb2_8[12]/0.1*1000*-1, '%s' %color[12], label='Channel' + str(12+1))
plt.plot(t1[0],Vpcb2_8[13]/0.1*1000*-1, '%s' %color[13], label='Channel' + str(13+1))
#plt.plot(t1[0],Vpcb2_8[14]/0.1*1000*-1, '%s' %color[14], label='Channel' + str(14+1))
plt.plot(t1[0],Vpcb2_8[15]/0.1*1000*-1, '%s' %color[15], label='Channel' + str(15+1))
plt.title(label="Resistance Sample 8 after reflow (solder balls, Tresky)", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance [mΩ]',fontsize=34)
plt.show()


#Sample 9
#Remove CH 4, 11, 14, 15
ax=plt.figure()
plt.plot(t1[0],Vpcb2_9[0]/0.1*1000*-1, '%s' %color[0], label='Channel' + str(0+1))
plt.plot(t1[0],Vpcb2_9[1]/0.1*1000*-1, '%s' %color[1], label='Channel' + str(1+1))
plt.plot(t1[0],Vpcb2_9[2]/0.1*1000*-1, '%s' %color[2], label='Channel' + str(2+1))
#plt.plot(t1[0],Vpcb2_9[3]/0.1*1000*-1, '%s' %color[3], label='Channel' + str(3+1))
plt.plot(t1[0],Vpcb2_9[4]/0.1*1000*-1, '%s' %color[4], label='Channel' + str(4+1))
plt.plot(t1[0],Vpcb2_9[5]/0.1*1000*-1, '%s' %color[5], label='Channel' + str(5+1))
plt.plot(t1[0],Vpcb2_9[6]/0.1*1000*-1, '%s' %color[6], label='Channel' + str(6+1))
plt.plot(t1[0],Vpcb2_9[7]/0.1*1000*-1, '%s' %color[7], label='Channel' + str(7+1))
#plt.plot(t1[0],Vpcb2_9[8]/0.1*1000*-1, '%s' %color[8], label='Channel' + str(8+1))
#plt.plot(t1[0],Vpcb2_9[9]/0.1*1000*-1, '%s' %color[9], label='Channel' + str(9+1))
#plt.plot(t1[0],Vpcb2_9[10]/0.1*1000*-1, '%s' %color[10], label='Channel' + str(10+1))
#plt.plot(t1[0],Vpcb2_9[11]/0.1*1000*-1, '%s' %color[11], label='Channel' + str(11+1))
plt.plot(t1[0],Vpcb2_9[12]/0.1*1000*-1, '%s' %color[12], label='Channel' + str(12+1))
#plt.plot(t1[0],Vpcb2_9[13]/0.1*1000*-1, '%s' %color[13], label='Channel' + str(13+1))
plt.plot(t1[0],Vpcb2_9[14]/0.1*1000*-1, '%s' %color[14], label='Channel' + str(14+1))
#plt.plot(t1[0],Vpcb2_9[15]/0.1*1000*-1, '%s' %color[15], label='Channel' + str(15+1))
plt.title(label="Resistance Sample 9 after reflow (solder balls, Tresky)", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance [mΩ]',fontsize=34)
plt.show()


#Sample 10
#Remove CH 4, 11, 14, 15
ax=plt.figure()
plt.plot(t1[0],Vpcb2_10[0]/0.1*1000*-1, '%s' %color[0], label='Channel' + str(0+1))
plt.plot(t1[0],Vpcb2_10[1]/0.1*1000*-1, '%s' %color[1], label='Channel' + str(1+1))
plt.plot(t1[0],Vpcb2_10[2]/0.1*1000*-1, '%s' %color[2], label='Channel' + str(2+1))
plt.plot(t1[0],Vpcb2_10[3]/0.1*1000*-1, '%s' %color[3], label='Channel' + str(3+1))
plt.plot(t1[0],Vpcb2_10[4]/0.1*1000*-1, '%s' %color[4], label='Channel' + str(4+1))
plt.plot(t1[0],Vpcb2_10[5]/0.1*1000*-1, '%s' %color[5], label='Channel' + str(5+1))
plt.plot(t1[0],Vpcb2_10[6]/0.1*1000*-1, '%s' %color[6], label='Channel' + str(6+1))
plt.plot(t1[0],Vpcb2_10[7]/0.1*1000*-1, '%s' %color[7], label='Channel' + str(7+1))
plt.plot(t1[0],Vpcb2_10[8]/0.1*1000*-1, '%s' %color[8], label='Channel' + str(8+1))
plt.plot(t1[0],Vpcb2_10[9]/0.1*1000*-1, '%s' %color[9], label='Channel' + str(9+1))
#plt.plot(t1[0],Vpcb2_10[10]/0.1*1000*-1, '%s' %color[10], label='Channel' + str(10+1))
plt.plot(t1[0],Vpcb2_10[11]/0.1*1000*-1, '%s' %color[11], label='Channel' + str(11+1))
plt.plot(t1[0],Vpcb2_10[12]/0.1*1000*-1, '%s' %color[12], label='Channel' + str(12+1))
plt.plot(t1[0],Vpcb2_10[13]/0.1*1000*-1, '%s' %color[13], label='Channel' + str(13+1))
plt.plot(t1[0],Vpcb2_10[14]/0.1*1000*-1, '%s' %color[14], label='Channel' + str(14+1))
#plt.plot(t1[0],Vpcb2_10[15]/0.1*1000*-1, '%s' %color[15], label='Channel' + str(15+1))
plt.title(label="Resistance Sample 10 after reflow (solder balls, Tresky)", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance [mΩ]',fontsize=34)
plt.show()


#Sample 4
#Remove CH 4, 11, 14, 15
ax=plt.figure()
#plt.plot(t1[0],Vpcb2_4[0]/0.1*1000*-1, '%s' %color[0], label='Channel' + str(0+1))
plt.plot(t1[0],Vpcb2_4[1]/0.1*1000*-1, '%s' %color[1], label='Channel' + str(1+1))
plt.plot(t1[0],Vpcb2_4[2]/0.1*1000*-1, '%s' %color[2], label='Channel' + str(2+1))
plt.plot(t1[0],Vpcb2_4[3]/0.1*1000*-1, '%s' %color[3], label='Channel' + str(3+1))
plt.plot(t1[0],Vpcb2_4[4]/0.1*1000*-1, '%s' %color[4], label='Channel' + str(4+1))
plt.plot(t1[0],Vpcb2_4[5]/0.1*1000*-1, '%s' %color[5], label='Channel' + str(5+1))
plt.plot(t1[0],Vpcb2_4[6]/0.1*1000*-1, '%s' %color[6], label='Channel' + str(6+1))
plt.plot(t1[0],Vpcb2_4[7]/0.1*1000*-1, '%s' %color[7], label='Channel' + str(7+1))
plt.plot(t1[0],Vpcb2_4[8]/0.1*1000*-1, '%s' %color[8], label='Channel' + str(8+1))
plt.plot(t1[0],Vpcb2_4[9]/0.1*1000*-1, '%s' %color[9], label='Channel' + str(9+1))
#plt.plot(t1[0],Vpcb2_4[10]/0.1*1000*-1, '%s' %color[10], label='Channel' + str(10+1))
plt.plot(t1[0],Vpcb2_4[11]/0.1*1000*-1, '%s' %color[11], label='Channel' + str(11+1))
plt.plot(t1[0],Vpcb2_4[12]/0.1*1000*-1, '%s' %color[12], label='Channel' + str(12+1))
plt.plot(t1[0],Vpcb2_4[13]/0.1*1000*-1, '%s' %color[13], label='Channel' + str(13+1))
#plt.plot(t1[0],Vpcb2_4[14]/0.1*1000*-1, '%s' %color[14], label='Channel' + str(14+1))
#plt.plot(t1[0],Vpcb2_4[15]/0.1*1000*-1, '%s' %color[15], label='Channel' + str(15+1))
plt.title(label="Resistance Sample 4 after reflow (solder balls, Tresky)", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Resistance [mΩ]',fontsize=34)
plt.show()



## Temperature Vs. Time
#ax=plt.figure()
#plt.plot((ttotal[0]/3600),(T1total[0]), linewidth=2.0)
#plt.plot((ttotal[0]/3600),(T2total[0]), linewidth=2.0)
#ax.legend(fontsize=24)
#plt.xlabel('Time [hrs]', fontsize=34)
#plt.rcParams['xtick.labelsize']=34
#plt.rcParams['ytick.labelsize']=34
#plt.ylabel('Temperature [°C]',fontsize=34)
#plt.show()

