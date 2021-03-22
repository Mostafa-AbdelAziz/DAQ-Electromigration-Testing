# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 00:14:07 2019

@author: Anna & Mostafa

Instruments Used: 
    DCsource: E3649A Agilent Power Supply
    Multiplexer: Keithley 2700 multiplexer
    Nanovolt: 34420A Nano voltmeter
    Oven: Omegalux
    Tempmeter: 34401A
"""

##Reset All
from IPython import get_ipython
get_ipython().magic('reset -sf')

##Import packages required for this code
import visa
import time
import matplotlib.pyplot as plt
import scipy.io
from math import sqrt

#Variables for PT1000 Temperature Sensor
def roots(a,b,c): 
    disc = b**2 - 4*a*c 
    if disc >= 0:
        if ((-b + sqrt(disc))/(2*a))<300 and ((-b + sqrt(disc))/(2*a))>-1:
            return (-b + sqrt(disc))/(2*a)
        elif ((-b - sqrt(disc))/(2*a))<300 and ((-b - sqrt(disc))/(2*a))>-1:
            return (-b - sqrt(disc))/(2*a)
    else:
        return -10000000
    
##Close all plotting windows     
plt.close('all')

##File Name
sampleName = 'BGA_PCB_SAC305_Accelerated Temp & Power Characterization';
fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #Filename

##Initialize Variables
thold = 10                  #holding time
RealTimeReadings = 300      #Real time plotting that only show a window of this number of values 
A = 3.9083e-3;
B = -5.775e-7;
RTD0 = 1000;

"""
The current levels of range(2,500,2) is from 0.02A to 5A, with a current stepping of 0.02A
"""
    
#GPIB INITIALIZATION WITH PYVISA
rm = visa.ResourceManager()
rm.list_resources()
DCsource = rm.open_resource('GPIB0::26::INSTR')
multiplexer = rm.open_resource('GPIB0::24::INSTR')
#nanovolt = rm.open_resource('GPIB0::22::INSTR') 
tempmeter=rm.open_resource('GPIB0::4::INSTR') 

multiplexer.write('*RST')
multiplexer.write('*CLS')
multiplexer.write('CONFigure:VOLTage')
#Close channels due to the Keithley 2700 multiplexer configurations 
#multiplexer.write('rout:mult:clos (@123,124,125)') 

##Instrument Initialization
#nanovolt.write('*RST')
#nanovolt.write('*CLS')
#nanovolt.write('CONFigure:FRESistance')   
#nanovolt.write('SENSe:FRESistance:OCOMpensated ON')

tempmeter.write('*RST')
tempmeter.write('*CLS')
tempmeter.write('CONFigure:FRESistance')

DCsource.write('*RST')
DCsource.write('*CLS') #NEED TO CANCEL LIMIT

##Initialize lists 
t = [] 
T = [] 
V = [[] for y in range(16)] 
I = [[] for y in range(16)] 
R = [[] for y in range(16)] 
P = [[] for y in range(16)]

R_RP=[[] for y in range(16)] 
I_RP=[[] for y in range(16)] 
V_RP=[[] for y in range(16)] 
t_RP=[]
P_RP=[[] for y in range(16)] 

R_RT=[[] for y in range(16)] 
T_RT=[] 
t_RT=[]

Ilevels=[] 
channel=['@101','@102','@103','@104','@105','@106','@107','@108','@109','@110','@111','@112','@113','@114','@115','@116']
color=['b','b--','g','g--','r','r--','c','c--','m','m--','y','y--','k','k--','b:','b--']
#Ilevelsetup = range(2,140,5)
Ilevelsetup = range(2,140,20)  
for objects in range(len(Ilevelsetup)):
    Ilevels.append((Ilevelsetup[objects])/100) #List Ilevels store current levels for sweeping

#tTempStage=[120,180,240]
#tWaitStage=[95,155,215]
#tRTStage=[100,160,220]
#tRPStage=[120,180,240]
#
tTempStage=[35*60,70*60]
tWaitStage=[30*60,65*60]
tRTStage=[35*60,70*60]
#tTempStage=[35,70]
#tWaitStage=[30,65]
#tRTStage=[35,70]
tic = time.perf_counter()#start timer-----

##Saving lists as arrays to .mat files
  #%% R-P tests
DCsource.write(':APPLy 5, 0.1')
DCsource.write(':OUTPut:STATe %d' % (1))  
  
  
#wait for 70mins, run RP once, run RT for the entire time
#plot I-t,P-T the entire time
while time.perf_counter()-tic< 70*60:
#while time.perf_counter()-tic< 70:
    for j in range (16):
        ##Multiplexing
        multiplexer.write(':ROUTe:OPEN:all') # Open all channels
        multiplexer.write(':ROUTe:CLOSe (%s)' % (channel[j])) #close a channel for reading
        rawstr = multiplexer.query('read?')
        index=rawstr.find('VDC')
        volStr = rawstr[0:index]
        IValue=float(DCsource.query(':MEASure:SCALar:CURRent:DC?'))
        I[j].append(IValue)
        R[j].append(float(volStr)/IValue)
        P[j].append(float(volStr)*IValue)

        
    tempvalue=float(tempmeter.query('read?'))
    T.append(roots(B*RTD0, A*RTD0, RTD0-tempvalue))
    ##Append current execution time
    t.append(time.perf_counter()-tic)
    
    ####Plot R-t, R-P graphs
    plt.ion()
    q = plt.figure(1)
#            plt.cla() #clear the plots for real time readings
    #Real time plotting
    for k in range (16):  
        plt.plot(t[max(0, len(t)-RealTimeReadings):],R[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
    plt.xlabel('Time [s]',fontsize=30)
    plt.ylabel('Resistance [Ohm]',fontsize=30)
    plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
    plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
    plt.show()
    #Flush the data for the real time plotting window
    q.canvas.draw()
    q.canvas.flush_events() 
    
    plt.ion()
    q = plt.figure(2)
#            plt.cla() #clear the plots for real time readings
    #Real time plotting
    plt.plot(t[max(0, len(t)-RealTimeReadings):],T[max(0, len(t)-RealTimeReadings):], 'b')
    plt.xlabel('Time [s]',fontsize=30)
    plt.ylabel('Temperature [°C]',fontsize=30)
    plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
    plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
    plt.show()
    #Flush the data for the real time plotting window
    q.canvas.draw()
    q.canvas.flush_events() 
    ##Saving lists as arrays to .mat files
    
    plt.ion()
    q = plt.figure(3)
#            plt.cla() #clear the plots for real time readings
    #Real time plotting
    for k in range (16):  
        plt.plot(t[max(0, len(t)-RealTimeReadings):],I[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
    plt.xlabel('Time [s]',fontsize=30)
    plt.ylabel('Current [A]',fontsize=30)
    plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
    plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
    plt.show()
    #Flush the data for the real time plotting window
    q.canvas.draw()
    q.canvas.flush_events() 
    
    
    data = {}
    data['I'] = I
    data['Ilevels'] = Ilevels
    data['thold'] = thold
    data['R'] = R
    data['t'] = t
    data['T'] = T
    data['Ilevels'] = Ilevels
    data['thold'] = thold
    data['R_RT'] = R_RT
    data['T_RT'] = T_RT
    data['t_RT'] = t_RT
    data['tTempStage'] = tTempStage
    data['tWaitStage'] = tWaitStage
    data['tRTStage'] = tRTStage
    data['R_RP'] = R_RP
    data['I_RP'] = I_RP
    data['V_RP'] = V_RP
    data['t_RP'] = t_RP
    data['P_RP'] = P_RP
    data['V'] = V
    scipy.io.savemat('%s.mat' % fname, data)
#end of while
    
#RP
for k in range(len(Ilevels)):
    DCsource.write(':APPLy 5,%G' % (Ilevels[k]))
    DCsource.write(':OUTPut:STATe %d' % (1))
    toc=time.perf_counter()

##The while loop of monitoring resistance at each current level for the holding time
    while time.perf_counter()-toc<thold:

        #For loop multiplexing through each channel to record its data
        for j in range (16):
            multiplexer.write(':ROUTe:OPEN:all') # Open all channels
            multiplexer.write(':ROUTe:CLOSe (%s)' % (channel[j])) #close a channel for reading
            rawstr = multiplexer.query('read?')
            index=rawstr.find('VDC')
            volStr = rawstr[0:index]
            VValue=float(volStr)
            V[j].append(VValue)
            V_RP[j].append(VValue)
             
            IValue=float(DCsource.query(':MEASure:SCALar:CURRent:DC?'))
            I[j].append(IValue)
            I_RP[j].append(IValue)
            
            
            #R=V/I
            R[j].append(VValue/IValue)
            R_RP[j].append(VValue/IValue)
            #P=V*I
            P[j].append(VValue*IValue)
            P_RP[j].append(VValue*IValue)
            
        ##Append current execution time
        tValue=time.perf_counter()-tic
        t.append(tValue)
        t_RP.append(tValue)
        
        tempvalue=float(tempmeter.query('read?'))
        TValue=roots(B*RTD0, A*RTD0, RTD0-tempvalue)
        T.append(TValue)
        
            
        ####Plot R-t, R-P graphs
        plt.ion()
        q = plt.figure(1)
#                        plt.cla() #clear the plots for real time readings
        #Real time plotting
        for k in range (16):  
            plt.plot(t[max(0, len(t)-RealTimeReadings):],R[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
        plt.xlabel('Time [s]',fontsize=30)
        plt.ylabel('Resistance [Ohm]',fontsize=30)
        plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
        plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
        plt.show()
        #Flush the data for the real time plotting window
        q.canvas.draw()
        q.canvas.flush_events() 
        
        plt.ion()
        q = plt.figure(2)
#            plt.cla() #clear the plots for real time readings
        #Real time plotting
        plt.plot(t[max(0, len(t)-RealTimeReadings):],T[max(0, len(t)-RealTimeReadings):], 'b')
        plt.xlabel('Time [s]',fontsize=30)
        plt.ylabel('Temperature [°C]',fontsize=30)
        plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
        plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
        plt.show()
        #Flush the data for the real time plotting window
        q.canvas.draw()
        q.canvas.flush_events() 
        
        plt.ion()
        q = plt.figure(3)
    #            plt.cla() #clear the plots for real time readings
        #Real time plotting
        for k in range (16):  
            plt.plot(t[max(0, len(t)-RealTimeReadings):],I[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
        plt.xlabel('Time [s]',fontsize=30)
        plt.ylabel('Current [A]',fontsize=30)
        plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
        plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
        plt.show()
        #Flush the data for the real time plotting window
        q.canvas.draw()
        q.canvas.flush_events() 
        
        q = plt.figure(4)
#                        plt.cla() #clear the plots for real time readings
        #Real time plotting
        for k in range (16):  
            plt.plot(P[k][max(0, len(t)-RealTimeReadings):],R[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
        plt.xlabel('Power [W]',fontsize=30)
        plt.ylabel('Resistance [Ohm]',fontsize=30)
        plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
        plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
        plt.show()
        #Flush the data for the real time plotting window
        q.canvas.draw()
        q.canvas.flush_events() 
        
        plt.ion()
        q = plt.figure(5)
        for k in range (16):  
            plt.plot(t[max(0, len(t)-RealTimeReadings):],I[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
        plt.xlabel('Time [s]',fontsize=30)
        plt.ylabel('Current [A]',fontsize=30)
        plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
        plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
        plt.show()
        #Flush the data for the real time plotting window
        q.canvas.draw()
        q.canvas.flush_events()
        data = {}
        data['I'] = I
        data['Ilevels'] = Ilevels
        data['thold'] = thold
        data['R_RP'] = R_RP
        data['I_RP'] = I_RP
        data['V_RP'] = V_RP
        data['t_RP'] = t_RP
        data['P_RP'] = P_RP
        data['R_RT'] = R_RT
        data['T_RT'] = T_RT
        data['t_RT'] = t_RT
        data['tTempStage'] = tTempStage
        data['tWaitStage'] = tWaitStage
        data['tRTStage'] = tRTStage
        data['V'] = V
        data['R'] = R
        data['t'] = t
        data['P'] = P
        data['T'] = T
        scipy.io.savemat('%s.mat' % fname, data)    
    
    
toe = time.perf_counter()
DCsource.write(':APPLy 5,%G' % (0.1))
DCsource.write(':OUTPut:STATe %d' % (1))  
while time.perf_counter()-toe< 5*60:
#while time.perf_counter()-toe< 60:
    # Measurements
    for j in range (16):
        ##Multiplexing
        multiplexer.write(':ROUTe:OPEN:all') # Open all channels
        multiplexer.write(':ROUTe:CLOSe (%s)' % (channel[j])) #close a channel for reading
        rawstr = multiplexer.query('read?')
        index=rawstr.find('VDC')
        volStr = rawstr[0:index]
        RValue=float(volStr)/0.1
        R[j].append(RValue)
        R_RT[j].append(RValue)
        IValue=float(DCsource.query(':MEASure:SCALar:CURRent:DC?'))
        I[j].append(IValue)
        P[j].append(float(volStr)*IValue)
        
    tempvalue=float(tempmeter.query('read?'))
    TValue=roots(B*RTD0, A*RTD0, RTD0-tempvalue)
    T.append(TValue)
    T_RT.append(TValue)
    ##Append current execution time
    tValue=time.perf_counter()-tic
    t.append(tValue)
    t_RT.append(tValue)
    
    
    ####Plot R-t, R-P graphs
    plt.ion()
    q = plt.figure(1)
#            plt.cla() #clear the plots for real time readings
    #Real time plotting
    for k in range (16):  
        plt.plot(t[max(0, len(t)-RealTimeReadings):],R[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
    plt.xlabel('Time [s]',fontsize=30)
    plt.ylabel('Resistance [Ohm]',fontsize=30)
    plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
    plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
    plt.show()
    #Flush the data for the real time plotting window
    q.canvas.draw()
    q.canvas.flush_events() 
    
    plt.ion()
    q = plt.figure(2)
#            plt.cla() #clear the plots for real time readings
    #Real time plotting
    plt.plot(t[max(0, len(t)-RealTimeReadings):],T[max(0, len(t)-RealTimeReadings):], 'b')
    plt.xlabel('Time [s]',fontsize=30)
    plt.ylabel('Temperature [°C]',fontsize=30)
    plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
    plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
    plt.show()
    #Flush the data for the real time plotting window
    q.canvas.draw()
    q.canvas.flush_events() 
    
    plt.ion()
    q = plt.figure(3)
#            plt.cla() #clear the plots for real time readings
    #Real time plotting
    for k in range (16):  
        plt.plot(t[max(0, len(t)-RealTimeReadings):],I[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
    plt.xlabel('Time [s]',fontsize=30)
    plt.ylabel('Current [A]',fontsize=30)
    plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
    plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
    plt.show()
    #Flush the data for the real time plotting window
    q.canvas.draw()
    q.canvas.flush_events() 
    
    
    data = {}
    data['I'] = I
    data['Ilevels'] = Ilevels
    data['thold'] = thold
    data['R_RT'] = R_RT
    data['T_RT'] = T_RT
    data['t_RT'] = t_RT
    data['tTempStage'] = tTempStage
    data['tWaitStage'] = tWaitStage
    data['tRTStage'] = tRTStage
    data['R'] = R
    data['t'] = t
    data['T'] = T
    scipy.io.savemat('%s.mat' % fname, data)      
too = time.perf_counter()        
i=-1
while i<1:
    i=i+1 
    while time.perf_counter()-too< tTempStage[i]:
        while time.perf_counter()-too< tWaitStage[i]:
            for j in range (16):
                ##Multiplexing
                multiplexer.write(':ROUTe:OPEN:all') # Open all channels
                multiplexer.write(':ROUTe:CLOSe (%s)' % (channel[j])) #close a channel for reading
                rawstr = multiplexer.query('read?')
                index=rawstr.find('VDC')
                volStr = rawstr[0:index]
                IValue=float(DCsource.query(':MEASure:SCALar:CURRent:DC?'))
                I[j].append(IValue)
                P[j].append(float(volStr)*IValue)
                R[j].append(float(volStr)/IValue)
                
            tempvalue=float(tempmeter.query('read?'))
            T.append(roots(B*RTD0, A*RTD0, RTD0-tempvalue))
            ##Append current execution time
            t.append(time.perf_counter()-tic)
            
            ####Plot R-t, R-P graphs
            plt.ion()
            q = plt.figure(1)
#            plt.cla() #clear the plots for real time readings
            #Real time plotting
            for k in range (16):  
                plt.plot(t[max(0, len(t)-RealTimeReadings):],R[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
            plt.xlabel('Time [s]',fontsize=30)
            plt.ylabel('Resistance [Ohm]',fontsize=30)
            plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
            plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
            plt.show()
            #Flush the data for the real time plotting window
            q.canvas.draw()
            q.canvas.flush_events() 
            
            plt.ion()
            q = plt.figure(2)
#            plt.cla() #clear the plots for real time readings
            #Real time plotting
            plt.plot(t[max(0, len(t)-RealTimeReadings):],T[max(0, len(t)-RealTimeReadings):], 'b')
            plt.xlabel('Time [s]',fontsize=30)
            plt.ylabel('Temperature [°C]',fontsize=30)
            plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
            plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
            plt.show()
            #Flush the data for the real time plotting window
            q.canvas.draw()
            q.canvas.flush_events() 
            ##Saving lists as arrays to .mat files
            plt.ion()
            q = plt.figure(3)
        #            plt.cla() #clear the plots for real time readings
            #Real time plotting
            for k in range (16):  
                plt.plot(t[max(0, len(t)-RealTimeReadings):],I[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
            plt.xlabel('Time [s]',fontsize=30)
            plt.ylabel('Current [A]',fontsize=30)
            plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
            plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
            plt.show()
            #Flush the data for the real time plotting window
            q.canvas.draw()
            q.canvas.flush_events() 
            
            data = {}
            data['I'] = I
            data['Ilevels'] = Ilevels
            data['thold'] = thold
            data['R'] = R
            data['t'] = t
            data['T'] = T
            data['Ilevels'] = Ilevels
            data['thold'] = thold
            data['R_RT'] = R_RT
            data['T_RT'] = T_RT
            data['t_RT'] = t_RT
            data['tTempStage'] = tTempStage
            data['tWaitStage'] = tWaitStage
            data['tRTStage'] = tRTStage
            data['R_RP'] = R_RP
            data['I_RP'] = I_RP
            data['V_RP'] = V_RP
            data['t_RP'] = t_RP
            data['P_RP'] = P_RP
            data['V'] = V
            scipy.io.savemat('%s.mat' % fname, data)
        #end of while
        
        #%% R-T tests
        while time.perf_counter()-too< tRTStage[i]:
            # Measurements
            for j in range (16):
                ##Multiplexing
                multiplexer.write(':ROUTe:OPEN:all') # Open all channels
                multiplexer.write(':ROUTe:CLOSe (%s)' % (channel[j])) #close a channel for reading
                rawstr = multiplexer.query('read?')
                index=rawstr.find('VDC')
                volStr = rawstr[0:index]
                RValue=float(volStr)/0.1
                R[j].append(RValue)
                R_RT[j].append(RValue)
                IValue=float(DCsource.query(':MEASure:SCALar:CURRent:DC?'))
                I[j].append(IValue)
                P[j].append(float(volStr)*IValue)
                
            tempvalue=float(tempmeter.query('read?'))
            TValue=roots(B*RTD0, A*RTD0, RTD0-tempvalue)
            T.append(TValue)
            T_RT.append(TValue)
            ##Append current execution time
            tValue=time.perf_counter()-tic
            t.append(tValue)
            t_RT.append(tValue)
            
            
            ####Plot R-t, R-P graphs
            plt.ion()
            q = plt.figure(1)
        #            plt.cla() #clear the plots for real time readings
            #Real time plotting
            for k in range (16):  
                plt.plot(t[max(0, len(t)-RealTimeReadings):],R[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
            plt.xlabel('Time [s]',fontsize=30)
            plt.ylabel('Resistance [Ohm]',fontsize=30)
            plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
            plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
            plt.show()
            #Flush the data for the real time plotting window
            q.canvas.draw()
            q.canvas.flush_events() 
            
            plt.ion()
            q = plt.figure(2)
        #            plt.cla() #clear the plots for real time readings
            #Real time plotting
            plt.plot(t[max(0, len(t)-RealTimeReadings):],T[max(0, len(t)-RealTimeReadings):], 'b')
            plt.xlabel('Time [s]',fontsize=30)
            plt.ylabel('Temperature [°C]',fontsize=30)
            plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
            plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
            plt.show()
            #Flush the data for the real time plotting window
            q.canvas.draw()
            q.canvas.flush_events() 
            
            plt.ion()
            q = plt.figure(3)
        #            plt.cla() #clear the plots for real time readings
            #Real time plotting
            for k in range (16):  
                plt.plot(t[max(0, len(t)-RealTimeReadings):],I[k][max(0, len(t)-RealTimeReadings):], '%s' %color[k])
            plt.xlabel('Time [s]',fontsize=30)
            plt.ylabel('Current [A]',fontsize=30)
            plt.rcParams['xtick.labelsize']=32 #Set the font size of x-axis
            plt.rcParams['ytick.labelsize']=32 #Set the font size of y-axis
            plt.show()
            #Flush the data for the real time plotting window
            q.canvas.draw()
            q.canvas.flush_events() 

            
            data = {}
            data['I'] = I
            data['Ilevels'] = Ilevels
            data['thold'] = thold
            data['R_RT'] = R_RT
            data['T_RT'] = T_RT
            data['t_RT'] = t_RT
            data['tTempStage'] = tTempStage
            data['tWaitStage'] = tWaitStage
            data['tRTStage'] = tRTStage
            data['R'] = R
            data['t'] = t
            data['T'] = T
            scipy.io.savemat('%s.mat' % fname, data) 
            
            
            
      
#    i=i+1        
##Close all GPIB Connections and Power off Vantek Power Supply
#ch=subprocess.Popen("Vantek.exe -off -com12",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
multiplexer.close()
DCsource.close()
tempmeter.close()
rm.close() 
