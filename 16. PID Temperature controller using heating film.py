"""
Created on Tue Jul 28 13:29:14 2020

@author: m8abdela
#Temperature Controller using 34411A Multimeter (for temp. sensor), 2200-26-5 Keithley Power Supply for 
#Icstation 12V 12W Flexible Polyimide Heater Plate Adhesive PI Heating Film 10mmx93mm (Pack of 4)
Use "U3606 Multimeter DC Power Supply" manual from "Keysight Command Expert"

"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

from itertools import chain
import visa
import time
import matplotlib.pyplot as plt
import scipy.io
from math import sqrt
from simple_pid import PID

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
V1 = []

fname=time.strftime("%y%m%d%H%M%S",time.localtime()) + sampleName #filename
#GPIB INITIALIZATION WITH PYVISA
rm = visa.ResourceManager()
rm.list_resources()
multimeter = rm.open_resource('USB0::0x0957::0x0A07::MY48005925::0::INSTR')
DCsource = rm.open_resource('USB0::0x05E6::0x2200::9050135::0::INSTR')

tic = time.perf_counter()
DCsource.write('*RST')
DCsource.write('*CLS')
DCsource.write('OUTPUT ON')
DCsource.write('CURR 1')
DCsource.write('VOLT 1')
#DCsource.write('OUTPUT OFF')

class FilmHeater:
    def __init__(self):
        self.film_temp = 40
    def update(self, powersupply_voltage):
        voltage_reading = DCsource.query_ascii_values('MEASure:VOLTage:DC?')
        powersupply_voltage = voltage_reading  
        if powersupply_voltage > 0:
            temp_values1 = multimeter.query_ascii_values(':MEASure:SCALar:FRESistance?')
            opc1 = int(temp_values1[0])
            RR1 = roots(B*RTD0, A*RTD0, RTD0-float(opc1));
            Tread1.append(RR1)           
            self.film_temp = RR1
            return self.film_temp
 
while failureflag == 0:
    vol = -10000;
    cur = -10000;
    while vol == -10000 or cur == -10000:
        toc=time.perf_counter()
        t.append(toc-tic)
        try:
            try:
                temp_values1 = multimeter.query_ascii_values(':MEASure:SCALar:FRESistance?')
                opc1 = int(temp_values1[0])
                RR1 = roots(B*RTD0, A*RTD0, RTD0-float(opc1));
                Tread1.append(RR1)
                if (RR1) > 40: #50C=1194.00ohm, 60C=1232.40ohm, 70C=1270.80ohm
                    DCsource.write('VOLT 1.5')
                elif (RR1) < 40:
                    DCsource.write('VOLT 4')
#                    DCsource.write('VOLT %s' % (voltage))
                voltage_readings = DCsource.query_ascii_values('MEASure:VOLTage:DC?')
                voltage_V = voltage_readings[0]

                boiler = FilmHeater()
                film_temp = boiler.film_temp                   
                pid = PID(100, 10, 5, setpoint=film_temp)
                pid.output_limits = (0, 100)
                power = pid(film_temp)
                film_temp = boiler.update(power)
                #The problem is that I want my setpoint to be 40C, not to control the voltage, how do I make it clear that PID should act on voltage based on temperature
#                v = FilmHeater.update(0)
#                while True:
#                    temp_values1 = multimeter.query_ascii_values(':MEASure:SCALar:FRESistance?')
#                    opc1 = int(temp_values1[0])
#                    RR1 = roots(B*RTD0, A*RTD0, RTD0-float(opc1));
#                    Tread1.append(RR1)
#                    temperature = RR1   
#                    # compute new ouput from the PID according to the systems current value
#                    control = pid(temperature)
#                    # feed the PID output to the system and get its current value
#                    v = FilmHeater.update(control)                   
##                    voltage_reading = DCsource.write('MEASure:CURRent[:DC]?')
##                    voltage = voltage_reading           
##                    # compute new ouput from the PID according to the systems current value
##                    control = pid(voltage)
##                    # feed the PID output to the system and get its current value
##                    v = FilmHeater.update(control)
            except:
                Tread = [];
                print("error")
            T1.append(RR1)
            V1.append(voltage_V)
            data = {}
            data['t'] = t
            data['T1'] = T1
            data['power'] = power
            data['powersupply_voltage'] = powersupply_voltage
            data['V1']= V1

            #data['film_temp'] = film_temp
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
                V1 = []
        except:
            vol = -10000;
            cur = -10000;
        plt.ion()
        gg = plt.figure(1)
        plt.cla()
        plt.plot(t[max(0, len(t)-300):],T1[max(0, len(t)-300):])
        plt.xlabel('Time [s]')
        plt.ylabel('Temperature [℃]')
        plt.show()
        gg.canvas.draw()
        gg.canvas.flush_events()  

        plt.ion()
        gg = plt.figure(2)
        plt.cla()
        plt.plot(t[max(0, len(t)-300):],V1[max(0, len(t)-300):])
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [V]')
        plt.show()
        gg.canvas.draw()
        gg.canvas.flush_events()  
multimeter.close()
DCsource.close()
rm.close()    