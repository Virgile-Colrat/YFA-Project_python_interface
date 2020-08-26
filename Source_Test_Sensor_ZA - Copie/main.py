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
import random

filename="results"                                          #names the file in which the results are stored 

#########################################################
##           Begin experiement options                 ##
######################################################### 

#varaibleHumidity=1: humidity will vary throughtout the experiment
#variableTemperature=1: temperature will vary throughtout the experiment
variableHumidity=True
variableTemperature=True

tempConst=20                                                #maintains Temperature at value (in °C) if variableTemperature=False
HumidityConst=20                                            #maintains Humidity at this value (in %RH) if variableHumidity=False

temperatureMin=20
temperatureMax=50

humidityMin=20
humidityMax=60

#tempVariation=0: temp increseas from  temperatureMin to temperatureMax if variableTemperature=True
#tempVariation=1: temp decreseas from  temperatureMax to temperatureMin if variableTemperature=True
tempVariation=0    

#tempVariation=0: humidity increseas from  humidityMin to humidityMax if variableHumidity=True
#tempVariation=1: humidity decreseas from  humidityMax to humidityMin if variableHumidity=True
humidityVariation=0

#########################################################
##                 begin setup                         ##
#########################################################  
moduleTest.createfile(filename)                             #creates the results file in format .csv
numberMeasures=1


#########################################################
##                   begin experiment                  ##
#########################################################  
ligne=["","","","","","","","",""]
def Experiment():
    for i in range (100):
        
        ligne[3]=14.3+random.randrange(100)/1000
       
        moduleTest.inp(filename, ligne, i)                      #saves all the data in the "filename.csv" file '''
    for i in range (100,200):
        
        ligne[3]=25.6+random.randrange(100)/1000
       
        moduleTest.inp(filename, ligne, i)                      #saves all the data in the "filename.csv" file '''
    for i in range (200,300):
        
        ligne[3]=38.1+random.randrange(100)/1000
       
        moduleTest.inp(filename, ligne, i)                      #saves all the data in the "filename.csv" file '''
    for i in range (300,400):
        
        ligne[3]=50.9+random.randrange(100)/1000
       
        moduleTest.inp(filename, ligne, i)                      #saves all the data in the "filename.csv" file '''
    for i in range (400,500):
        
        ligne[3]=68+random.randrange(100)/1000
       
        moduleTest.inp(filename, ligne, i)                      #saves all the data in the "filename.csv" file '''
    for i in range (500,600):
        
        ligne[3]=85.7+random.randrange(100)/1000
       
        moduleTest.inp(filename, ligne, i)                      #saves all the data in the "filename.csv" file '''
     
    

Experiment()