

#  Curve trace program for Keithley 236/237/238 Source Measure Units (SMUs)
#  SMU A controls the drain of a FET   SMU B controls the gate
#

#from pyvisa import *                                      #import NI Virtual Instrument Software Architecture
import pyvisa
import time                                      #import python time functionality
rm = pyvisa.ResourceManager()

A = rm.open_resource("GPIB::16::INSTR")                  #create variable for instrument address
A.write("*rst; status:preset; *cls")
#B = visa.instrument("GPIB::17") 
                                                                 #variable for voltage

stepvoltage = -1.0
sweeploopcount = 16
steploopcount = 5
sweepresults = []                                     # create list to store measurements
A.write("F0,0X")                                 # Force Force V measure I
A.write("H0X")                                   # Immediate trigger
A.write("G5,2,0X")                               # source and measure
#B.write("F0,0X")                                 # Force Force V measure I
#B.write("H0X")                                   # Immediate trigger
#B.write("G5,2,0X") 
                                                 #Bias voltage , auto range, no delay
#B.write("N1X")  

for j in range(steploopcount):  
    sweepvoltage = 0   
    stepvoltage = stepvoltage + 1.0
    #B.write("B" +str(stepvoltage) +",0,0X") 
    for i in range(sweeploopcount):                             #loop variable and loop count
        A.write("B" +str(sweepvoltage) +",0,0X")          #Bias voltage , auto range, no delay
        A.write("N1X")                               # Operate (output on)
        sweepvoltage = sweepvoltage + 1                      #increment voltage
        time.sleep(0.05)                             # Wait
        sweepresults.append(A.read())                     # read measurement from SMU
        time.sleep(0.05)                             # Wait

# print results[i]                             #print measurement to console
A.write("N0X")                                   # Standby (output off)
#B.write("N0X") 
print ("Rdg","Voltage","   Current")
print (" ")
for i in range(sweeploopcount*steploopcount):
    print (i,sweepresults[i])                           #print list of measurements
time.sleep(5) 

