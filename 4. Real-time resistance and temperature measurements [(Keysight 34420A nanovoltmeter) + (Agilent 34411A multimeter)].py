# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:52:42 2020
@author: Mostafa AbdelAziz
Measuring voltage using a nanovoltmeter and temperature using a multimeter and PT1000 temp. sensor
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

import visa
import time
import matplotlib.pyplot as plt
import scipy.io
from math import sqrt

def roots(a,b,c):
    disc = b**2 - 4*a*c
    if disc >= 0:
        if ((-b + sqrt(disc))/(2*a))<300 and ((-b + sqrt(disc))/(2*a))>0:
            return (-b + sqrt(disc))/(2*a)
        elif ((-b - sqrt(disc))/(2*a))<300 and ((-b - sqrt(disc))/(2*a))>0:
            return (-b - sqrt(disc))/(2*a)
    else:
        return -10000000
    
plt.close('all')

RealTimeReadings = 1;
sampleName = 'Resistance Measurements of SAC305 flip chip';
SetCurrent = 5;
failureflag = 0;

A = 3.9083e-3;
B = -5.775e-7;
RTD0 = 1000;

t = [] 
T1 = []
R = []
V = []
Tread1 = []

fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename
#GPIB INITIALIZATION WITH PYVISA
rm = visa.ResourceManager()
rm.list_resources()
multimeter = rm.open_resource('GPIB0::20::INSTR')
nanovoltmeter = rm.open_resource('GPIB0::23::INSTR')

tic = time.perf_counter()

while failureflag == 0:
    toc=time.perf_counter()
    t.append(toc-tic)

    temp_values = nanovoltmeter.query_ascii_values(':MEASure:VOLTage:DC? %s,%s' % ('DEF', 'DEF'))
    measurement = temp_values[0]

    #Using 4-wire resistance to measure temperature. Use quadratic formula and PT1000 formula to convert resistance to temperature in degC    
    temp_values1 = multimeter.query_ascii_values(':MEASure:FRESistance? %s,%s' % ('DEF', 'MAX'))
    opc1 = int(temp_values1[0])
    RR1 = roots(B*RTD0, A*RTD0, RTD0-float(opc1));
    Tread1.append(RR1)
    
    ff = plt.figure(1)
    plt.cla()
    plt.plot(t,V)
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [mV]')
    plt.ion()
    plt.show()
    ff.canvas.draw()
    ff.canvas.flush_events()
        
    plt.ion()
    gg = plt.figure(2)
    plt.cla()
    plt.plot(t[max(0, len(t)-300):],Tread1[max(0, len(t)-300):])
    plt.xlabel('Time [s]')
    plt.ylabel('Temperature [℃]')
    plt.show()
    gg.canvas.draw()
    gg.canvas.flush_events()  
    
    data = {}
    data['t'] = t
    data['R'] = R
    data['T1'] = T1
    data['Tread1'] = Tread1
    data['V'] = V
    saved = 0
    while saved == 0:
        try:
            scipy.io.savemat('%s.mat' % fname, data)
            saved = 1
        except:
            saved = 0
    maxlength2save = 10000000
    if len(t) > maxlength2save:
        fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename  
        t = []
        T1 = []
        R = []
        V = []

multimeter.close()
nanovoltmeter.close()
rm.close()    
