# -*- coding: utf-8 -*-
"""
@author: Mostafa AbdelAziz
Resistance measurements of 2 PCBs using 2 card edge connectors connected to 
(Agilent Technologies 34980A Multifunction Switch) + (34921A, 40-channel multiplexer module)
Mesuring temperature using 4 PT1000 sensors (also connected to MUX in 4-wire configuration)
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

from itertools import chain
import pyvisa as visa
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
sampleName = 'Resistance Measurements of SAC305 flip chip_started_Nov25_samples 1 and 2_100°C_December19,2020';
SetCurrent = 5;
failureflag = 0;

A = 3.9083e-3;
B = -5.775e-7;
RTD0 = 1000;

t = [] 
T1 = []
T2 = []
T3 = []
T4 = []
R = [[] for z in range(16)]
Vpcb1 = [[] for z in range(16)]
Vpcb2 = [[] for z in range(16)]
Tread1 = []
Tread2 = []
Tread3 = []
Tread4 = []

fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename
#GPIB INITIALIZATION WITH PYVISA
rm = visa.ResourceManager()
rm.list_resources()
multiplexer = rm.open_resource('USB0::0x0957::0x0507::MY45000023::0::INSTR')

channel1=['@2001','@2002','@2003','@2004','@2005','@2006','@2007','@2008','@2009','@2010','@2011','@2012','@2013','@2014','@2015','@2016']
channel2=['@2021','@2022','@2023','@2024','@2025','@2026','@2027','@2028','@2029','@2030','@2031','@2032','@2033','@2034','@2035','@2036']
color=['b','b--','g','g--','r','r--','c','c--','m','m--','y','y--','k','k--','b-.','b:']

tic = time.perf_counter()

while failureflag == 0:
        toc=time.perf_counter()
        t.append(toc-tic)
#        try:
        for j in range (16):
            dc1 = multiplexer.query(':MEASure:SCALar:VOLTage:DC? (%s)' % (channel1[j]))
            cur = float(5)
            sep = 'VDC'
            rest = dc1.split(sep, 1)[0]
            sep1 = ','
            rest1 = rest.split(sep1, 1)[0]
            rest2 = float(rest1)
            Vpcb1[j].append(rest2)

            dc2 = multiplexer.query(':MEASure:SCALar:VOLTage:DC? (%s)' % (channel2[j]))
            rest3 = dc2.split(sep, 1)[0]
            rest4 = rest3.split(sep1, 1)[0]
            rest5 = float(rest4)
            Vpcb2[j].append(rest5)
            
            temp_values1 = multiplexer.query_ascii_values(':MEASure:SCALar:FRESistance? (%s)' %('@4001'))
            opc1 = int(temp_values1[0])
            RR1 = roots(B*RTD0, A*RTD0, RTD0-float(opc1));
            
            temp_values2 = multiplexer.query_ascii_values(':MEASure:SCALar:FRESistance? (%s)' %('@4002'))
            opc2 = int(temp_values2[0])
            RR2 = roots(B*RTD0, A*RTD0, RTD0-float(opc2));
            
            temp_values3 = multiplexer.query_ascii_values(':MEASure:SCALar:FRESistance? (%s)' %('@4003'))
            opc3 = int(temp_values3[0])
            RR3 = roots(B*RTD0, A*RTD0, RTD0-float(opc3));

            temp_values4 = multiplexer.query_ascii_values(':MEASure:SCALar:FRESistance? (%s)' %('@4004'))
            opc4 = int(temp_values4[0])
            RR4 = roots(B*RTD0, A*RTD0, RTD0-float(opc4));
            
        Tread1.append(RR1)
        Tread2.append(RR2)
        Tread3.append(RR3)
        Tread4.append(RR4)

        ff = plt.figure(1)
        plt.cla()
        #list1= chain(range(1,5), range(7,8), range(14,16))
        list1= chain(range(1,13), range(14,16))
        for w in list1:
            plt.plot(t,Vpcb1[w], '%s' %color[w])
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.ion()
        plt.show()
        ff.canvas.draw()
        ff.canvas.flush_events()

        ff = plt.figure(2)
        plt.cla()
        #list2= chain(range(1,5), range(7,8), range(14,16))
        list2= chain(range(1,16))
        for w in list2:
            plt.plot(t,Vpcb2[w], '%s' %color[w])
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [mV]')
        plt.ion()
        plt.show()
        ff.canvas.draw()
        ff.canvas.flush_events()
            
        plt.ion()
        gg = plt.figure(3)
        plt.cla()
        plt.plot(t[max(0, len(t)-300):],Tread1[max(0, len(t)-300):])
        plt.plot(t[max(0, len(t)-300):],Tread2[max(0, len(t)-300):])
        plt.plot(t[max(0, len(t)-300):],Tread3[max(0, len(t)-300):])
        plt.plot(t[max(0, len(t)-300):],Tread4[max(0, len(t)-300):])
        plt.xlabel('Time [s]')
        plt.ylabel('Temperature [℃]')
        plt.show()
        gg.canvas.draw()
        gg.canvas.flush_events()  

            
        data = {}
        data['t'] = t
        data['R'] = R
        data['T1'] = T1
        data['T2'] = T2
        data['T3'] = T3
        data['T4'] = T4
        data['Tread1'] = Tread1
        data['Tread2'] = Tread2
        data['Tread3'] = Tread3  
        data['Tread4'] = Tread4
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
        maxlength2save = 10000000
        if len(t) > maxlength2save:
            fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename  
            t = []
            T1 = []
            T2 = []
            T3 = []
            T4 = []
            R = [[] for z in range(16)]
            V = [[] for z in range(16)]
            Vpcb1 = [[] for z in range(16)]
            Vpcb2 = [[] for z in range(16)]

multiplexer.close()
rm.close()    
