# -*- coding: utf-8 -*-
"""
@author: Mostafa AbdelAziz
Resistance measurements of 2 PCBs connected to Keithley 2700 MUX using 2 card edge connectors
Keithley 2700 Data Acquisition System and 7708 40-channel, Differential Multiplexer Module
Alo measuring temperature from 3 PT1000 sensors using 3 multiplexers
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

from itertools import chain
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
T2 = []
T3 = []
R = [[] for z in range(16)]
Vpcb1 = [[] for z in range(16)]
Vpcb2 = [[] for z in range(16)]
I = [[] for z in range(16)]
Tread1 = []
Tread2 = []
Tread3 = []

fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename
#GPIB INITIALIZATION WITH PYVISA
rm = visa.ResourceManager()
rm.list_resources()
multiplexer = rm.open_resource('GPIB0::24::INSTR')
multimeter1 = rm.open_resource('GPIB0::4::INSTR')
multimeter2 = rm.open_resource('GPIB0::5::INSTR')
multimeter3 = rm.open_resource('USB0::0x0957::0x0A07::MY48005925::0::INSTR')

#I am measuring the resistance of each channel in my first test vehicle (16 channels in total)
channel1=['@101','@102','@103','@104','@105','@106','@107','@108','@109','@110','@111','@112','@113','@114','@115','@116']
#I am measuring the resistance of each channel in my second test vehicle (16 channels in total)
channel2=['@201','@202','@203','@204','@205','@206','@207','@208','@209','@210','@211','@212','@213','@214','@215','@216']
#set a color which corresponds to each channel
color=['b','b--','g','g--','r','r--','c','c--','m','m--','y','y--','k','k--','b-.','b:']

tic = time.perf_counter()

while failureflag == 0:
        toc=time.perf_counter()
        t.append(toc-tic)
#        try:
        for j in range (16):
            dc1 = multiplexer.query(':MEASure:VOLTage:DC? (%s)' % (channel1[j]))
            cur = float(5)
            #The MUX saves the data with 'VDC' and other characters/symbols after the number. The following obtains the numbers only and removes all characters:
            sep = 'VDC'
            rest = dc1.split(sep, 1)[0]
            #If there is an open circuit, the MUX records +9.9E37 which gives an error and stops the code since it is expecting a number
            #This next part removes all charactes after the comma "," to prevent this error and still record values after an open circuit (for the other test vehicle) 
            sep1 = ','
            rest1 = rest.split(sep1, 1)[0]
            rest2 = float(rest1)
            Vpcb1[j].append(rest2)
            I[j].append(cur)

            #Repear voltage measurements but this time for second test vehicle
            dc2 = multiplexer.query(':MEASure:VOLTage:DC? (%s)' % (channel2[j]))
            rest3 = dc2.split(sep, 1)[0]
            rest4 = rest3.split(sep1, 1)[0]
            rest5 = float(rest4)
            Vpcb2[j].append(rest5)
            
            #Measure temperature using a multimeter and PT1000 temp. sensor. This is repeated thrice.
            temp_values1 = multimeter1.query_ascii_values(':MEASure:FRESistance? %s,%s' % ('DEF', 'MAX'))
            opc1 = int(temp_values1[0])
            RR1 = roots(B*RTD0, A*RTD0, RTD0-float(opc1));
            
            temp_values2 = multimeter2.query_ascii_values(':MEASure:FRESistance? %s,%s' % ('DEF', 'DEF'))
            opc2 = int(temp_values2[0])
            RR2 = roots(B*RTD0, A*RTD0, RTD0-float(opc2));
            
            temp_values3 = multimeter3.query_ascii_values(':MEASure:SCALar:FRESistance?')
            opc3 = int(temp_values3[0])
            RR3 = roots(B*RTD0, A*RTD0, RTD0-float(opc3));

        Tread1.append(RR1)
        Tread2.append(RR2)
        Tread3.append(RR3)

        ff = plt.figure(1)
        plt.cla()
        #In my case, I was getting problems with Channel 9 so I used 'chain' package to only include the channels I want to record
        list1= chain(range(1,5), range(7,10), range(15,16))
        for w in list1:
        #for w in [x for x in range(16) if x != 9]:
            plt.plot(t,Vpcb1[w], '%s' %color[w])
        plt.xlabel('Time [s]')
        plt.ylabel('Resistance [Ohm]')
        plt.ion()
        plt.show()
        ff.canvas.draw()
        ff.canvas.flush_events()

        ff = plt.figure(2)
        plt.cla()
        list2= chain(range(1,3), range(5,7), range(9,13))
        for w in list2:
        #for w in [x for x in range(16) if x != 11]:
            plt.plot(t,Vpcb2[w], '%s' %color[w])
        plt.xlabel('Time [s]')
        plt.ylabel('Resistance [Ohm]')
        plt.ion()
        plt.show()
        ff.canvas.draw()
        ff.canvas.flush_events()
            
        plt.ion()
        gg = plt.figure(3)
        plt.cla()
        #If let us say you only want Tread1, you can comment out lines 143 and 144
        plt.plot(t[max(0, len(t)-300):],Tread1[max(0, len(t)-300):])
        plt.plot(t[max(0, len(t)-300):],Tread2[max(0, len(t)-300):])
        plt.plot(t[max(0, len(t)-300):],Tread3[max(0, len(t)-300):])
        plt.xlabel('Time [s]')
        plt.ylabel('Temperature [℃]')
        plt.show()
        gg.canvas.draw()
        gg.canvas.flush_events()  
            
        data = {}
        data['t'] = t
        data['I'] = I    
        data['R'] = R
        data['T1'] = T1
        data['T2'] = T2
        data['T3'] = T3
        data['Tread1'] = Tread1
        data['Tread2'] = Tread2
        data['Tread3'] = Tread3              
        data['Vpcb1'] = Vpcb1
        data['Vpcb2'] = Vpcb2
        saved = 0
        while saved == 0:
            try:
                scipy.io.savemat('%s.mat' % fname, data)
                saved = 1
            except:
                saved = 0
        #time.sleep(5)
        maxlength2save = 10000
        if len(t) > maxlength2save:
            fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename  
            t = []
            T1 = []
            T2 = []
            T3 = []
            R = [[] for z in range(16)]
            V = [[] for z in range(16)]
            I = [[] for z in range(16)]
            Vpcb1 = [[] for z in range(16)]
            Vpcb2 = [[] for z in range(16)]

multiplexer.close()
multimeter1.close()
multimeter2.close()
multimeter3.close()
rm.close()    

