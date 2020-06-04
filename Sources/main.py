import pyvisa
import time                                      #import python time functionality
import Keithley_Commands as Keithley
import serial
import binascii
import moduleTest

rm = pyvisa.ResourceManager()

A = rm.open_resource("GPIB::16::INSTR")                  #create variable for instrument address
Keithley.SetVoltage(A, 5)
#Keithley.MeasureAndPrint(A, 0.5, 10)