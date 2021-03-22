# -*- coding: utf-8 -*-
"""
Created on December 27, 2020
@author: m8abdela

Measure 4-wire resistance using two nanovoltmeters (e.g. Keysight 34420A)
"""
import pyvisa
import time
import matplotlib.pyplot as plt
import scipy.io 

plt.close('all')
RealTimeReadings = 1;
sampleName = 'Cancinotech_PCB_SAC305_Sample30_Grinding';
failureflag = 0;

t = []
T = []
R = []
V1 = []
V2 = []
V3 = []
I = []

fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename
#GPIB INITIALIZATION WITH PYVISA
rm = pyvisa.ResourceManager()
rm.list_resources()
nanovoltmeter1 = rm.open_resource('GPIB0::23::INSTR')
nanovoltmeter2 = rm.open_resource('GPIB0::22::INSTR')

tic = time.perf_counter()#start timer-----
        
while failureflag == 0:
    toc=time.perf_counter()
    t.append(toc-tic)

    """
    Due to the configuration of my test vehicle, I could not measure the resistance
    of two channels at the same time. An easy fix is to measure the 4-wire resistance
    of once channel, save the value, switch to voltage (not actually measuring anything)
    then measure the 4-wire resistance of the other channel and save its value
    In this case:
        V1 = resistance across first channel
        V2 = resistance across second channel
        V3 = useless
    """
    temp_values = nanovoltmeter1.query_ascii_values(":MEASure:FRESistance? DEF,DEF")
    measurement = temp_values[0]*1000
    V1.append(measurement)

    tempAB = nanovoltmeter1.query_ascii_values(":MEASure:VOLTage:DC? DEF,DEF")
    measurement1234 = tempAB[0]*1000
    V3.append(measurement1234)

    # plotting resistance across first channel
    plt.ion()
    ff = plt.figure(1)
    plt.cla()
    plt.plot(t,V1)
    plt.xlabel('Time [s]')
    plt.ylabel('Resistance [mohm]')
    plt.show()
    ff.canvas.draw()
    ff.canvas.flush_events()  

    temp_valuess = nanovoltmeter2.query_ascii_values(":MEASure:FRESistance? DEF,DEF")
    measurement2 = temp_valuess[0]*-1000
    V2.append(measurement2)

    tempA = nanovoltmeter2.query_ascii_values(":MEASure:VOLTage:DC? DEF,DEF")
    measurement123 = tempA[0]*1000
    V3.append(measurement123)

    # plotting resistance across second channel
    plt.ion()
    ff = plt.figure(2)
    plt.cla()
    plt.plot(t,V2)
    plt.xlabel('Time [s]')
    plt.ylabel('Resistance [mohm]')
    plt.show()
    ff.canvas.draw()
    ff.canvas.flush_events()  
    
    data = {}
    data['t'] = t
    data['V1'] = V1
    data['V2'] = V2
    data['I'] = I    
    data['R'] = R
    data['T'] = T
    scipy.io.savemat('%s.mat' % fname, data)
    time.sleep(0.1)
     
nanovoltmeter1.close()
nanovoltmeter2.close()
rm.close()    