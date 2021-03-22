# import TestModbusScript

"""
HANMATEK HM310P Power Supply
This code was taken from the following link, with minor modifications
to allow current stepping:
https://sourceforge.net/projects/dc-power-supply-software/files/

For the code to work, you need to install the power supply driver and connect
the USB cable
Identify the port number, start the .exe file and change the number accordingly
e.g. COM7
Press connect
Submit Voltage value (use 32 V)
Submit Current value (start at 0 A)
For output, press "ON"
The .exe file will seem like it crashes but it will start working
Check current level on power supply to verify it is working!
"""
from itertools import chain
import pyvisa
import scipy.io
import numpy as np
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from pymodbus.client.sync import ModbusSerialClient
import time
from time import sleep

"""Window Definition"""

device = []
connection = False


class MyWindow(Frame):
    unit_id = 1
    method = "rtu"
    baudrate = 9600
    bytesize = 8
    parity = "N"
    stopbits = 1
    timeout = 0.25

    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)
        """definitions"""

        self.connectedText = StringVar()
        self.connectedText.set("Not Connected")
#        self.tkValueVoltageRead = StringVar()
#        self.tkValueVoltageRead.set("0.0")
#        self.tkValueCurrentRead = StringVar()
#        self.tkValueCurrentRead.set("0.0")
#        self.tkValuePowerRead = StringVar()
#        self.tkValuePowerRead.set("0.0")
        self.tkValueVoltageWrite = StringVar()
        self.tkValueVoltageWrite.set("32.0")
        self.tkValueCurrentWrite = StringVar()
        self.tkValueCurrentWrite.set("0.1")
        self.tkValuePowerWrite = StringVar()
        self.tkValuePowerWrite.set("0.0")

        """COM Port Fields"""
        comport_label = Label(self, bd=5, width=40, text="COM Port")
        self.tkCOMPort = StringVar(self)
        self.tkCOMPort.set("COM11")
        comport_entry = OptionMenu(self, self.tkCOMPort, "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8",
                                   "COM8",
                                   "COM9", "COM10", "COM11", "COM12", "COM13", "COM14", "COM15", "COM16")
        connect_button = Button(self, bd=5, text="Connect", command=self.connect_device)
        disconnect_button = Button(self, bd=5, text="Disconnect", command=self.disconnect_device)
        self.connectedText.set("Disconnected")
        self.connected_label = Label(self, bd=5, width=40, bg="red", textvariable=self.connectedText)

        """Controller"""
        controlledValues_label = Label(self, bd=5, width=40, text="Controllable Values")
        controlledVoltage_label = Label(self, bd=5, width=20, text="Voltage")
        self.voltage_value_write = Entry(self, textvariable=self.tkValueVoltageWrite)          
        voltage_submit = Button(self, bd=5, text="Submit", command=self.submit_voltage)
        controlledCurrent_label = Label(self, bd=5, width=20, text="Current")
        self.current_value_write = Entry(self, textvariable=self.tkValueCurrentWrite)
        current_submit = Button(self, bd=5, text="Submit", command=self.submit_current)
        """Output Control"""
        self.output_label = Label(self, bd=5, width=20, bg="red", text="Output")
        output_button_on = Button(self, bd=5, text="On", command=self.output_on)
        output_button_off = Button(self, bd=5, text="Off", command=self.output_off)
        exit_button = Button(self, bd=5, text="Exit", command=self.quit_program)
#        """Reader"""
#        self.readValues_label = Label(self, bd=5, width=40, text="Read Values")
#        readVoltage_label = Label(self, bd=5, width=20, text="Voltage")
#        self.voltage_value_read = Entry(self, state="readonly", textvariable=self.tkValueVoltageRead)
#        readCurrent_label = Label(self, bd=5, width=20, text="Current")
#        self.current_value_read = Entry(self, state="readonly", textvariable=self.tkValueCurrentRead)
#        power_label = Label(self, bd=5, width=20, text="Power")
#        self.power_value_read = Entry(self, state="readonly", textvariable=self.tkValuePowerRead)

        """Windows Format"""
        """COM Port"""
        comport_label.grid(row=0, column=0, columnspan=3, sticky="WE")
        comport_entry.grid(row=1, column=0, sticky="WE")
        connect_button.grid(row=1, column=1, sticky="WE")
        disconnect_button.grid(row=1, column=2, sticky="WE")
        ttk.Separator(self, orient=HORIZONTAL).grid(row=2, column=0, columnspan=3, sticky="WE")
        self.connected_label.grid(row=3, column=0, columnspan=3, sticky="WE")
        ttk.Separator(self, orient=HORIZONTAL).grid(row=4, column=0, columnspan=3, sticky="WE")
        """Controller"""
        controlledValues_label.grid(row=5, column=0, columnspan=3, sticky="WE")
        controlledVoltage_label.grid(row=6, column=0, sticky="WE")
        self.voltage_value_write.grid(row=6, column=1, sticky="WE")
        voltage_submit.grid(row=6, column=2, sticky="WE")
        controlledCurrent_label.grid(row=7, column=0, sticky="WE")
        self.current_value_write.grid(row=7, column=1, sticky="WE")
        current_submit.grid(row=7, column=2, sticky="WE")
        self.output_label.grid(row=8, column=0, sticky="WE")
        output_button_on.grid(row=8, column=1, sticky="WE")
        output_button_off.grid(row=8, column=2, sticky="WE")
        ttk.Separator(self, orient=HORIZONTAL).grid(row=9, column=0, columnspan=3, sticky="WE")
#        """Reader"""
#        self.readValues_label.grid(row=10, column=0, columnspan=3, sticky="WE")
#        readVoltage_label.grid(row=11, column=0, sticky="WE")
#        self.voltage_value_read.grid(row=11, column=1, sticky="WE")
#        readCurrent_label.grid(row=12, column=0, sticky="WE")
#        self.current_value_read.grid(row=12, column=1, sticky="WE")
#        power_label.grid(row=13, column=0, sticky="WE")
#        self.power_value_read.grid(row=13, column=1, sticky="WE")
#        ttk.Separator(self, orient=HORIZONTAL).grid(row=14, column=0, columnspan=3, sticky="WE")
#        exit_button.grid(row=15, column=0, columnspan=3, sticky="WE")

#    def shortIO(self):
#        device.write_register(address=int('1', 16), count=1, value=1, unit=1)
#        time.sleep(0.25)
#        device.write_register(address=int('1', 16), count=1, value=0, unit=1)

    def connect_device(self):
        global device
        global connection
        device = ModbusSerialClient(method=self.method, port=self.tkCOMPort.get(),
                                    stopbits=self.stopbits, bytesize=self.bytesize,
                                    parity=self.parity, baudrate=self.baudrate,
                                    timeout=self.timeout)
        connection = device.connect()

        if not connection:
            messagebox.showerror("Error", "Problems connecting to COM port. \n"
                                          "Please check the port.")
        else:
            self.connectedText.set("Connected")
            self.connected_label.config(bg="green")
            device.write_register(address=int('1', 16), count=1, value=1, unit=1)

    def disconnect_device(self):
        global device
        global connection
        try:
            self.output_off()
            device.close()
            device = []
            connection = False
            self.connectedText.set("Disconnected")
            self.connected_label.config(bg="red")
        except AttributeError:
            messagebox.showerror("Error", "COM Port is disconnected!!!")

    def submit_voltage(self):
        try:
            voltageString4 = 3200
            transferString = int(voltageString4)
            device.write_register(address=int('30', 16), count=1, value=transferString, unit=1)
        except AttributeError:
            messagebox.showerror("Error", "COM Port is disconnected!!!")

    def submit_current(self):
        try:
            Ilevels=[]
            I=[]
            
            #This is the part responsible for the current stepping
            #Go from 0 mA to 10.3 A by 200 mA intervals 
            
            Ilevelsetup = np.arange(0,10300,200)  
            for objects in range(len(Ilevelsetup)):
                Ilevels.append((Ilevelsetup[objects]))
            n = 1
            ele = float(0)
            list(chain(*[Ilevels[i:i+n] + [ele] if len(Ilevels[i:i+n]) == n else Ilevels[i:i+n] for i in range(0, len(Ilevels), n)]))        
            for x in range(51):
                    device.write_register(address=int('31', 16), count=1, value=Ilevels[x], unit=1)
                    #Current on time
                    time.sleep(10)
                    device.write_register(address=int('31', 16), count=1, value=int(0), unit=1)
                    #Current off time
                    time.sleep(10)
        except AttributeError:
            messagebox.showerror("Error", "COM Port is disconnected!!!")

    def output_on(self):
        try:
            device.write_register(address=int('1', 16), count=1, value=1, unit=1)
            self.output_label.config(bg="green")
        except AttributeError:
            messagebox.showerror("Error", "COM Port is disconnected!!!")

    def output_off(self):
        try:
            device.write_register(address=int('1', 16), count=1, value=0, unit=1)
            self.output_label.config(bg="red")
        except AttributeError:
            messagebox.showerror("Error", "COM Port is disconnected!!!")

    def quit_program(self):
        if connection:
            self.disconnect_device()
        self.quit()

    def updateVoltage(self, voltage):
        self.tkValueVoltageRead.set(voltage)

    def updateCurrent(self, current):
        self.tkValueCurrentRead.set(current)

    def updatePower(self, power):
        self.tkValuePowerRead.set(power)

def read_data(my_label):
    global device
    resultU = []
    resultI = []
    resultP = []
    if hasattr(device, "read_holding_registers"):
        result = device.read_holding_registers(address=16, count=4, unit=1)
        if hasattr(result, "unit_id"):
            voltageString1 = float(result.registers[0])
            voltageString2 = voltageString1 / 100.0
            transferString = str(voltageString2)
            my_label.updateVoltage(transferString)
            currentString1 = float(result.registers[1])
            currentString2 = currentString1 / 1000.0
            transferString = str(currentString2)
            my_label.updateCurrent(transferString)
            powerString1 = float(result.registers[2] + result.registers[3])
            powerString2 = powerString1 / 1000.0
            transferString = str(powerString2)
            my_label.updatePower(transferString)
    my_label.after(500, read_data, my_label)

def main():
    window = Tk()
    my_label = MyWindow(window)
    window.title("Power Supply Controller")
    read_data(my_label)
    my_label.pack(side=TOP)
    window.mainloop()

if __name__ == '__main__':
    main()
