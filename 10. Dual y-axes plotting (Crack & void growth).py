# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 02:59:10 2020

@author: Mostafa
"""

import scipy.io
import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.patches as mpatches

#Note: Micrographs were still being taken when the test was stopped & restarted, need to correct for that time
t = (0, 12, 24, 36, 48, 60, 72, 84,96,106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196, 201, 218, 227, 240, 250, 270, 300, 320, 330)
area_void=(0,0,0,37.08411645,52.97730922,79.46596383,105.9546184,134.4808619,342.1111622,371.8599589,401.6087556,416.483154,416.483154,470.6830165,577.6564293,753.5003442,753.5003442,806.8851712,852.7309195,871.0692189,909.7834064,967.8546876,967.8546876,1006.568875,1025.925969,1064.640156,1099.075407,1202.177401,1316.282375,1324.228972,1344.808619,1363.758195,1457.691039,1532.063031)
length_crack = (0,0.657647322,0.881192374,1.106390528,1.352035502,1.534731247,1.593894601,1.60262285,1.606549097,1.672961446,1.771016657,1.939922679,1.992887353,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.937771264,2.937771264,2.937771264,2.937771264,2.996431211,2.996431211,3.083115308,3.083115308,3.205386092,4.053899357,4.306007431,4.343558449)
#length_crack_corrected = length_crack*(100/3.9266)
length_crack_corrected = [x*(100/3.9266)  for x in length_crack] 

"""
Old Measurements
t = (0, 33, 60, 90, 120, 150, 180, 240, 292)
length_crack = (0, 11.94212711, 21.73138828, 43.42765496, 43.42765496, 50.31201263, 54.89529809, 66.07393669, 105.1461101)
diameter_void = (0, 0, 0, 0, 16.89677844, 17.68573307, 17.68573307, 22.74819198, 30.63773833)
area_void = (0, 68.84421519, 68.84421519, 114.7403587, 137.6884304, 240.9547532, 642.5460085, 917.9228692, 1239.195873)
"""

# Resistance & Temperature Vs. Time (2 Different Scales)
fig, ax1 = plt.subplots()
color = 'tab:green'
ax1.set_xlabel('Time [h]', fontsize=38)
ax1.set_ylabel('Crack length [μm]', color=color, fontsize=38)
ax1.plot((t), length_crack_corrected,marker='o',markersize=10, linestyle='--', color=color, linewidth=2.0)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Void diameter [μm]', color=color, fontsize=38)
ax2.plot((t), area_void,marker='o',markersize=10, linestyle='--', color=color, linewidth=2.0)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()
ax1.tick_params(labelsize=34)
ax2.tick_params(labelsize=34)


#t = (0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285)


#
## Resistance & Temperature Vs. Time (2 Different Scales)
#fig, ax1 = plt.subplots()
#color = 'tab:green'
#ax1.set_xlabel('Time [hrs]', fontsize=38)
#ax1.set_ylabel('Crack length [μm]', color=color, fontsize=38)
#ax1.plot((t), length_crack, color=color, linewidth=4.0)
#ax1.tick_params(axis='y', labelcolor=color)
#ax2 = ax1.twinx()
#color = 'tab:orange'
#ax2.set_ylabel('Void area [μm\u00b2]', color=color, fontsize=38)
#ax2.plot((t), area_void, color=color, linewidth=4.0)
#ax2.tick_params(axis='y', labelcolor=color)
#fig.tight_layout()
#plt.show()
#ax1.tick_params(labelsize=34)
#ax2.tick_params(labelsize=34)