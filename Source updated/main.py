#-------------------------------------------------------------------
#Created by Virgile Colrat - LNIS 05/8/2020 
#
#This python scripts execute the experiment using:
#   -   Keithley 236 as power source and current measurment
#   -    
#Keithley 236 instument using a KUSB-488A GPIB adapter. To function properly,
#it is needed to install the following python packages: 
#   -   pyvisa (Detailed instruction on how to install pyvisa
#       on MAC, Windows or linux https://pyvisa.readthedocs.io/en/1.8/getting.html)
#   -   time
#A detailed list of all the commands available to the Keithley 236
#instrument can be found here:
#https://www.tek.com/manual/model-236-237-238-source-measure-units-operators-manual-rev-e-13-mb
#There is 2 types of function in this module, the basic function (found in instrument
# documentation) and "advance" function that are a combination of basic function and are used
#to simplify the use of the instrument in this experiment
#-------------------------------------------------------------------



import pyvisa
import time                                      #import python time functionality
import Keithley_Control as Keithley
import serial
import binascii
import moduleTest
import Omeagaette_Control
filename="results"
rm = pyvisa.ResourceManager()
#begin setup
keithley = rm.open_resource("GPIB::16::INSTR")                  #create variable for instrument address
Keithley.SetVoltage(keithley, 5)
omegaette=Omeagaette_Control.OpenOmegaette()
moduleTest.createfile(filename)
numberMeasures=100
#end setup
for i in range(numberMeasures):
    ligne=Omeagaette_Control.MeasureAndReturn(omegaette)
    returnKeithley=Keithley.MeasureAndReturn(keithley, 1)
    returnKeithley=returnKeithley[:24]
    ligne[7]=returnKeithley[13:]#current
    ligne[8]=returnKeithley[0:11]#voltage
    #print(returnKeithley[0])
    print("measure Keithley unit: "+str(returnKeithley))
    print("measure humidity: "+str(ligne[3]))
    print("measure temperature: "+str(ligne[2]))
    moduleTest.inp(filename, ligne, i)

#Keithley.MeasureAndPrint(A, 0.5, 10)