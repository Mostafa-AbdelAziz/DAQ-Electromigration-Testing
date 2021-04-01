# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:36:31 2020
@author: m8abdela
"""
# MIJO 34
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.io

#plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'

t = (0, 12, 24, 36, 48, 60, 72, 84,96,106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196, 201, 218, 227, 240, 250, 270, 300, 320, 330, 350)
area_void=(0,0,0,37.08411645,52.97730922,79.46596383,105.9546184,134.4808619,342.1111622,371.8599589,401.6087556,416.483154,416.483154,470.6830165,577.6564293,753.5003442,753.5003442,806.8851712,852.7309195,871.0692189,909.7834064,967.8546876,967.8546876,1006.568875,1025.925969,1064.640156,1099.075407,1202.177401,1316.282375,1324.228972,1344.808619,1363.758195,1457.691039,1532.063031,1532.063031)
length_crack = (0,0.657647322,0.881192374,1.106390528,1.352035502,1.534731247,1.593894601,1.60262285,1.606549097,1.672961446,1.771016657,1.939922679,1.992887353,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.769277884,2.937771264,2.937771264,2.937771264,2.937771264,2.996431211,2.996431211,3.083115308,3.083115308,3.205386092,4.053899357,4.306007431,4.343558449,4.343558449)
length_crack_corrected = [x*(100/3.9266)  for x in length_crack] 
# Resistance & Temperature Vs. Time (2 Different Scales)
# fig, ax1 = plt.subplots()
# ax1.set_xlabel('Time [h]', fontsize=38)
# ax1.set_ylabel('Crack length [μm]', color=color, fontsize=38)
# ax1.plot((t), length_crack_corrected,marker='o',markersize=10, linestyle='--', color=color, linewidth=2.0)
# ax1.tick_params(axis='y', labelcolor=color)
# ax2 = ax1.twinx()
# ax2.set_ylabel('Void diameter [μm]', color=color, fontsize=38)
# ax2.plot((t), area_void,marker='o',markersize=10, linestyle='--', color=color, linewidth=2.0)
# ax2.tick_params(axis='y', labelcolor=color)
# fig.tight_layout()
# plt.show()
# ax1.tick_params(labelsize=34)
# ax2.tick_params(labelsize=34)


import matplotlib.pylab as pylab
params = {'legend.fontsize': 'xx-large',
          'figure.figsize': (10, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'}
pylab.rcParams.update(params)

#increase speed
x = t
z = area_void
y = length_crack_corrected

fig, ax1 = plt.subplots(figsize=(20,12))
Writer = animation.writers['pillow']
writer = Writer(fps=6000, metadata=dict(artist='Me'), bitrate=1800)
#plt.xlim(0, 140)
color = 'tab:blue'
ax2 = ax1.twinx()
ax2.set_ylabel('Void Area [μm²]', color=color, fontsize=38)
ax2.tick_params(axis='y', labelcolor=color)

plt.xlim([0, 350])
ax1.set_ylim(0, 120)
ax2.set_ylim(0, 1700)

color = 'tab:green'
ax1.set_xlabel('Time [h]', fontsize=38)
ax1.set_ylabel('Crack length [μm]', color=color, fontsize=38)
ax1.tick_params(axis='y', labelcolor=color)

ax1.tick_params(axis='both', which='major', labelsize=35)
ax1.tick_params(axis='both', which='minor', labelsize=35)
ax2.tick_params(axis='both', which='major', labelsize=35)
ax2.tick_params(axis='both', which='minor', labelsize=35)

line1, = ax1.plot(x, y, color = "g",linewidth=3, label='Temp. Sensor Reading')
line2, = ax2.plot(x, z, color = "b",linewidth=3, label='Estimated Solder Joint Temperature')
def update(num, x, y, line1, line2):
    line1.set_data(x[:num], y[:num])
    line2.set_data(x[:num], z[:num])
    return [line1, line2]
ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line1, line2],
                  interval=50, blit=True)
#plt.show()
ani.save('RTV4temp.gif', writer=writer)



