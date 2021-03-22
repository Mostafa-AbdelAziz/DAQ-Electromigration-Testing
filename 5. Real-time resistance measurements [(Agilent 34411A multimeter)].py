# -*- coding: utf-8 -*-
"""
Created on December 27, 2020
@author: m8abdela

Measure 2-wire voltage using a multimeter (e.g. Agilent 34411A, hp 34401A)
"""
#import python modules (use anaconda prompt e.g. type 'pip install pyvisa' to install pyvisa)
import pyvisa #if does not work, import 'visa' instead
import time
import matplotlib.pyplot as plt
import scipy.io 

#close plots from previous sessions
plt.close('all')
RealTimeReadings = 1;
sampleName = 'Cancinotech_PCB_SAC305_Sample1_Current_Fusing_LeftPCB';
failureflag = 0;

#variables time, temperature, resistance, voltage and current
t = []
T = []
R = []
V = []
I = []

#set file name based on time
fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename
#GPIB INITIALIZATION WITH 
#Install 'Keysight connection expert' and 'IO Libraries Suite' to determine GPIB/USB address
rm = pyvisa.ResourceManager()
rm.list_resources()
multimeter = rm.open_resource('USB0::0x0957::0x0A07::MY48005925::0::INSTR')

tic = time.perf_counter()#start timer
        
while failureflag == 0:
    toc=time.perf_counter()
    t.append(toc-tic)
    
    #use keysight command expert to obtain instrument-specific commands 
    temp_values = multimeter.query_ascii_values(':MEASure:VOLTage:DC? %s,%s' % ('DEF', 'DEF'))
    measurement = temp_values[0]*1000
    V.append(measurement)
    
    #real-time plotting (voltage versus time, only updates last 300 points to avoid crashing)
    plt.ion()
    ff = plt.figure(1)
    plt.cla()
    plt.plot(t[max(0, len(t)-300):],V[max(0, len(t)-300):])
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [mV]')
    plt.show()
    ff.canvas.draw()
    ff.canvas.flush_events()  

    #save variables as a mat file
    data = {}
    data['t'] = t
    data['V'] = V
    data['I'] = I    
    data['R'] = R
    data['T'] = T
    scipy.io.savemat('%s.mat' % fname, data)
    time.sleep(0.1)

#close instruments     
multimeter.close()
rm.close()    