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
import serial
voltageMax=1.8 #maximum voltage of the source, DO NOT go over, the chip WILL burn

filename="results"                                          #names the file in which the results are stored 
rm = pyvisa.ResourceManager()
polarisationVoltage=-4.096
polarisationCurrent=60                                      #polarisation current


ligne=["","","","","res"]

#########################################################
##                   begin setup                       ##
#########################################################  

keithley = rm.open_resource("GPIB::16::INSTR")               #create variable for instrument address
STM32= serial.Serial('COM8', 209700, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)#Opens stm32 com port
#########################################################
##                   end setup                         ##
#########################################################  

#########################################################
##                   begin experiment                  ##
#########################################################  
def PID(In, InPrev):
    Fs=250000
    Ts=1/Fs
    I=Fs*128/4096
    D=128*16384/Fs

    P=0.5
    N=3
    PIDOut=int(In)*(P+(I*Ts/InPrev)+D*N/(1+N*Ts/InPrev))
    if PIDOut>=256:
        PIDOut=256
    return PIDOut


def Experiment():
    #Keithley.SetCurrent(keithley, polarisationCurrent)
    InPrev=128
    i=0
    previousVoltage=0
    moduleTest.createfile(filename) 
    values=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while 1:
        
        for i in range(31):
            #print("i=",i)
            #TM32= serial.Serial('COM8', 209700, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)#Opens stm32 com port
            outComp=STM32.read()
            if outComp!=b'\x00':
                #if STM32Val==b'1':
                #    outComp=1
                #    print(outComp)
                #elif STM32Val==b'0':
                #    outComp=0
                #    print(outComp)
                #print(outComp)
            
                #########################################################
                ##                   begin PID                         ##
                ######################################################### 
                outPid=PID(outComp, InPrev)*0.000000001
                InPrev=outPid
                if InPrev<=0:
                    InPrev=1
                #print(outPid)
                values[i]=outPid
                #########################################################
                ##                    end PID                          ##
                ######################################################### 
                
                outCurrent=outPid*47
                Keithley.SetCurrent(keithley, outCurrent)
                returnKeithley=Keithley.MeasureAndReturn(keithley, 0)   #Takes measurment of current and voltage from the Keithley 236
                returnKeithley=returnKeithley[:24]                      #Eliminates the '\r\n' at the end of the data sent back by the Keithley 236
                ligne[2]=returnKeithley[13:]                            #fills the current box in the line that will be logged
                ligne[3]=returnKeithley[0:11]                           #fills the voltage box in the line that will be logged
                
                #valueVoltage=int(ligne[2][1:6])*10^int(ligne[2][9:10])
                val=float(ligne[2][1:6])
                exp=int(ligne[2][9:10])
                valueVoltage=float(val*(10**exp))
                #print("voltage: ", valueVoltage)


                '''
                if valueVoltage>1.8:
                    Keithley.SetVoltage(keithley,previousVoltage)
                    print("/!\ Overvoltage")
                else:
                    previousVoltage=valueVoltage
                #print(returnKeithley[0])'''
                i+=1
                moduleTest.inp(filename, ligne, i)                      #saves all the data in the "filename.csv" file 
            average=1
            for i in values:
                average=average+i
            average=average/32
            resistance=6000/average
            #print("resistance =",resistance)
    rm.close()
#########################################################
##                   end experiment                    ##
#########################################################  
#Keithley.MeasureAndPrint(A, 0.5, 10)

Experiment()