#-------------------------------------------------------------------
#Created by Virgile Colrat - LNIS 05/8/2020 
#
#This python scripts execute the experiment using:
#   -   Keithley 236 as power source and current measurment
#   -   MFCs: EW-32907-55,EW-32907-59, EW-32907-69 
#Keithley 236 instument using a KUSB-488A GPIB adapter.
#The MFCs are pluged directly in the 
#To function properly,
#it is needed to install the following python packages: 
#   -   pyvisa (Detailed instruction on how to install pyvisa
#       on MAC, Windows or linux https://pyvisa.readthedocs.io/en/1.8/getting.html)
#   -   serial
#   -   time
#A detailed list of all the commands available to the Keithley 236
#instrument can be found here:
#https://www.tek.com/manual/model-236-237-238-source-measure-units-operators-manual-rev-e-13-mb
#There is 2 types of function in this module, the basic function (found in instrument
# documentation) and "advance" function that are a combination of basic function and are used
#to simplify the use of the instrument in this experiment
#-------------------------------------------------------------------



import pyvisa                                               #import python pyvisa functionality for NI PXI cards
import time                                        
import Keithley_Control as Keithley
import serial
import binascii
import moduleTest
import Omeagaette_Control
import MFC_Control
import Permeation_Oven_Control
from alicat import FlowController

filename="results-054"                                          #names the file in which the results are stored 
rm = pyvisa.ResourceManager()
polarisationVoltage=7                                 #7V ?!
numberMeasures=10

#########################################################
##                   begin setup                       ##
#########################################################  

keithley = rm.open_resource("GPIB::16::INSTR")              #create variable for instrument address
Keithley.SetVoltage(keithley, polarisationVoltage)          #sets the voltage of the Keithley unit at "polarisationVoltage"
omegaette=Omeagaette_Control.OpenOmegaette()                #opens the serial com with the Omegaette HH314 (humidty and temperature measurments)
moduleTest.createfile(filename)                             #creates the results file in format .csv
flow_controller_A = FlowController(port='COM16', address='A') ##opens the serial com with the MFC
flow_controller_A.set_flow_rate(0)                          #Closes the MFC (flowrate=0)

#########################################################
##                   end setup                         ##
#########################################################  

#########################################################
##                   begin experiment                  ##
#########################################################  

def Experiment():
    print("MFC openned")
    time.sleep(300)
    for i in range(numberMeasures):
        flow_controller_A.set_flow_rate(100)
        ligne=Omeagaette_Control.MeasureAndReturn(omegaette)    #Takes measurment of humidity and tempertaure from the Omegaette instrument
        returnKeithley=Keithley.MeasureAndReturn(keithley, 0)   #Takes measurment of current and voltage from the Keithley 236
        returnKeithley=returnKeithley[:24]                      #Eliminates the '\r\n' at the end of the data sent back by the Keithley 236
        ligne[6]=float(flow_controller_A.get()["temperature"])           #fills the MFC temperature box in the line that will be logged
        
        
        ligne[7]=returnKeithley[13:]                            #fills the current box in the line that will be logged

        ligne[8]=returnKeithley[0:11]                           #fills the voltage box in the line that will be logged
        ligne[4]=float(float(returnKeithley[1:11])/float(returnKeithley[14:]))
        #time.sleep(1)
        #print(ligne[7])
        #print(ligne[8])
        #print(ligne[4])
        #print(returnKeithley[0])
        print(i*100/numberMeasures,"%")
        '''
        print(i)
        print("measure MFC temperature"+str(MFC1.get()["temperature"]))
        print("measure Keithley unit: "+str(returnKeithley))    #print voltage and current for debug
        print("measure humidity: "+str(ligne[3]))               #print humidity for debug
        print("measure temperature: "+str(ligne[2]))            #print temperature for debug'''
        moduleTest.inp(filename, ligne, i)                      #saves all the data in the "filename.csv" file '''
    rm.close()
    flow_controller_A.set_flow_rate(0)
    print("Experiment finnished, MFC closed")
#########################################################
##                   end experiment                    ##
#########################################################  

Experiment()