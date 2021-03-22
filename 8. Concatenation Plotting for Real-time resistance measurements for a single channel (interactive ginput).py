# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 02:43:03 2020
@author: Mostafa
"""
import scipy.io
import matplotlib.pyplot as plt 
import numpy as np

test1 = scipy.io.loadmat('200813134150Temperature Controller')
print(type(test1))
#test2 = scipy.io.loadmat('200602152922Resistance Measurements of SAC305 flip chip_Test2')
#test3 = scipy.io.loadmat('200602181655Resistance Measurements of SAC305 flip chip_Test3')

t=test1['t']
T1=test1['T1']
V1 = test1['V1']
#power = test1['power']

plt.ion()
gg = plt.figure(1)
plt.cla()
plt.plot(t[0],T1[0], color='black')
plt.xlabel('Time [s]',fontsize=30)
plt.ylabel('Temperature [°C]',fontsize=30)
plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
plt.show()
gg.canvas.draw()
gg.canvas.flush_events()  


plt.ion()
gg = plt.figure(2)
plt.cla()
plt.plot(t[0],V1[0], color='black')
plt.xlabel('Time [s]',fontsize=30)
plt.ylabel('Voltage [V]',fontsize=30)
plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
plt.show()
gg.canvas.draw()
gg.canvas.flush_events()     


plt.ion()
gg = plt.figure(3)
plt.cla()
plt.plot(t[0],power[0], color='black')
plt.xlabel('time [t]',fontsize=30)
plt.ylabel('Power [W]',fontsize=30)
plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
plt.show()
gg.canvas.draw()
gg.canvas.flush_events()   
