import pyvisa
import time                                      #import python time functionality
import Keithley_Commands as Keithley
rm = pyvisa.ResourceManager()

A = rm.open_resource("GPIB::16::INSTR")                  #create variable for instrument address
