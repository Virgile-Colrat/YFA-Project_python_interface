#import pyvisa
#import time
#rm = pyvisa.ResourceManager()
#print(rm.list_resources())
#inst = rm.open_resource('GPIB0::16::INSTR')
#print(inst.query("*IDN?"))
import pyvisa
import time                                      #import python time functionality
rm = pyvisa.ResourceManager()

A = rm.open_resource("GPIB::16::INSTR")                  #create variable for instrument address
time.sleep(2)
#A.write("*rst; status:preset; *cls")
A.write("N1")
#A.write("Q1,Virgile Colrat")
#A.write("R1")
#A.write("J2X")