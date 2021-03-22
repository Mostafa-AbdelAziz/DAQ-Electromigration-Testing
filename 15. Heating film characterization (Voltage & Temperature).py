# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:35:03 2020
@author: m8abdela
Perform voltage stepping on heating film to characterize it
-> Amount of heating (temperature measurement) at various voltage values
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

import visa
import time
import matplotlib.pyplot as plt
import numpy as np
import scipy.io
from math import sqrt

#Convert Pt1000 Resistance value to a temperature reading
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
sampleName = 'Temperature Controller';
failureflag = 0;
A = 3.9083e-3;
B = -5.775e-7;
RTD0 = 1000;

t = [] 
T1 = []
Tread1 = []
Voltage = []
thold=300

fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename
#GPIB INITIALIZATION WITH PYVISA
rm = visa.ResourceManager()
rm.list_resources()
multimeter = rm.open_resource('USB0::0x0957::0x0A07::MY48005925::0::INSTR')
DCsource = rm.open_resource('USB0::0x05E6::0x2200::9050135::0::INSTR')

DCsource.write('*RST')
DCsource.write('*CLS')
DCsource.write('OUTPUT ON')
DCsource.write('CURR 1')
DCsource.write('VOLT 1')

Vlevels=[]
V=[]
#Vlevelsetup = range(0,6,1)  
Vlevelsetup = np.arange(0,6,0.5)  
for objects in range(len(Vlevelsetup)):
    Vlevels.append((Vlevelsetup[objects])) #List Vlevels store voltage levels for sweeping
tic = time.perf_counter()

for k in range(len(Vlevels)):
    DCsource.write('VOLT %s' % (Vlevels[k]))
    toc=time.perf_counter()
    
    while time.perf_counter()-toc<thold:
        temp_values1 = multimeter.query_ascii_values(':MEASure:SCALar:FRESistance?')
        opc1 = int(temp_values1[0])
        RR1 = roots(B*RTD0, A*RTD0, RTD0-float(opc1));
        T1.append(RR1)
        tValue=time.perf_counter()-tic
        t.append(tValue)
        temp_values = DCsource.query_ascii_values(':MEASure:VOLTage:DC?')
        VValue = temp_values[0]
        V.append(VValue)

        plt.ion()
        gg = plt.figure(1)
        plt.cla()
        plt.plot(t[max(0, len(t)-300):],T1[max(0, len(t)-300):])
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
        plt.plot(t[max(0, len(t)-300):],V[max(0, len(t)-300):])
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
        plt.plot(V[max(0, len(t)-300):],T1[max(0, len(t)-300):])
        plt.xlabel('Voltage [V]',fontsize=30)
        plt.ylabel('Temperature [°C]',fontsize=30)
        plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
        plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
        plt.show()
        gg.canvas.draw()
        gg.canvas.flush_events()     
        
        data = {}
        data['t'] = t
        data['T1'] = T1
        data['Vlevels'] = Vlevels
        data['VValue'] = VValue
        data['V'] = V

        saved = 0
        while saved == 0:
            try:
                scipy.io.savemat('%s.mat' % fname, data)
                saved = 1
            except:
                saved = 0
        time.sleep(5)
        maxlength2save = 10000
        if len(t) > maxlength2save:
            fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename  
            t = []
            T1 = []
            Voltage = []

multimeter.close()
DCsource.close()
rm.close()    