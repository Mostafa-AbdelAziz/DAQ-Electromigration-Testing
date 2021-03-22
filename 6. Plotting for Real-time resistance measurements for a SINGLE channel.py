# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:36:31 2020
@author: m8abdela

Plotting .mat file obtained from 'Real-time resistance measurements using multimeter.py'
"""
# MIJO 34
#import python packages
from itertools import chain
import scipy.io
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.patches as mpatches

#import .mat file (both this file and '201227135015Cancinotech_PCB_SAC305_Sample1_Current_Fusing_LeftPCB.mat' need to be in the same directory/folder for it to work)
test1 = scipy.io.loadmat('201227135015Cancinotech_PCB_SAC305_Sample1_Current_Fusing_LeftPCB.mat')

#Test 1
t=test1['t']
V=test1['V']

#Plotting
#Sample 1
ax=plt.figure()
#plotting voltage versus time
plt.plot(t[0],V[0])
plt.title(label="Change title", fontsize=20, color="black") 
ax.legend(fontsize=24)
plt.xlabel('Time [s]', fontsize=34)
plt.rcParams['xtick.labelsize']=34
plt.rcParams['ytick.labelsize']=34
plt.ylabel('Voltage [mV]',fontsize=34)
plt.show()

