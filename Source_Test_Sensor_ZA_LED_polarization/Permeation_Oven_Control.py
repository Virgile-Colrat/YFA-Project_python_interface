#-------------------------------------------------------------------
#Created by Virgile Colrat - LNIS 06/10/2020 
#
#This python module gathers the function usefull for the control of the 
#VICI Dynacalibrator 500 permeation oven using a USB->serial adapter.
# To function properly it is needed to install the following python packages: 
#   -   pyvisa (Detailed instruction on how to install pyvisa
#       on MAC, Windows or linux https://pyvisa.readthedocs.io/en/1.8/getting.html)
#	-	serial
#A detailed list of all the commands available to the equipment used in the experiment
#can be found here:
#https://www.vici.com/support/manuals/dyna500.pdf
#-------------------------------------------------------------------
import serial

def OpenVici(comPort):
	ser = serial.Serial(comPort, 115200, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)
	return ser

def setTemperature(comPort, temp):
    comPort.write("TS="+temp+"\r\n")

def readSetTemperature(comPort, temp):
    comPort.write("TS\r\n")
    value=['','','','','','']
    for i in range(6):
        x=comPort.read()
        value[i]=str(x)
def readTemperature(comPort):
    comPort.write(b"TR\n")
    value=['','','','','','','','','']
    x=""
    for i in range(9):
        x=x+ord(comPort.read())
        value[i]=str(x)
    var=""
    for u in value:
        var = var+u.decode('utf-8')
    print(x)

def startDataLog(comPort):
    comPort.write("L+\r\n")

def stopDataLog(comPort):
    comPort.write("L-\r\n")

#To set the chamber temperature to 50°C, type “TS=50” and press <ENTER>.
# To read the set point, type “TS” and press <ENTER>.
# To read the current chamber temperature, type “TR” and press <ENTER>.
# To start data logging, type “L+” and press <ENTER>. 
# To stop data  logging, type “L-” and press <ENTER>. 
