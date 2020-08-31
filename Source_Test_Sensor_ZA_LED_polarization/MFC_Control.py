#-------------------------------------------------------------------
#Created by Virgile Colrat - LNIS 09/20/2020 
#
#This python module gathers the function usefull for the control of the 
#MFCs instument using a USB->serial adapter. To function properly,
#it is needed to install the following python packages: 
#   -   pyvisa (Detailed instruction on how to install pyvisa
#       on MAC, Windows or linux https://pyvisa.readthedocs.io/en/1.8/getting.html)
#	-	serial
#A detailed list of all the commands available to the MFCs used in the experiment
#can be found here:
#https://documents.alicat.com/manuals/Gas_Flow_Controller_Manual.pdf
#There are 2 types of function in this module, the basic function (found in instrument
# documentation) and "advance" function that are a combination of basic function and are used
#to simplify the use of the instrument in this experiment
#-------------------------------------------------------------------


import serial
#########################################################
##                 basic functions                     ##
##  The following functions are the direct application ##
##  of the functions described in the EW-32907-XX      ##
##  documentation                                      ##
#########################################################  

#OpenMFC: opens up the port on which the instrument is connected
def OpenMFC(comPort):
	ser = serial.Serial(comPort, 19200, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)
	return ser

#MeasureAndReturnPoll: does one measurment and returns it immediatly
def MeasureAndReturnPoll(comPort, iD):
	message=iD+"\r\n"
	res =''.join(format(ord(i), 'b') for i in message)
	comPort.write(res)
	return(comPort.read())

#BeginStream: start the streaming of the data, the MFC send continuously data to the computer, the data has to be polled in the main function
def BeginStream(comPort, iD):
	message=iD+"@=@\r\n"
	res =''.join(format(ord(i), 'b') for i in message)
	comPort.write(res)

#StopStream: stops the streaming of data
def StopStream(comPort, iD):
	message="@@="+iD+"\r\n"
	res =''.join(format(ord(i), 'b') for i in message)
	comPort.write(res)

#SetStreamInterval: sets the time interval between 2 measurment (in milliseconds) in streaming mode
def SetStreamInterval(comPort, iD, timeInterval):
	message=iD+" w91="+str(timeInterval)+"\r\n"
	res =''.join(format(ord(i), 'b') for i in message)
	comPort.write(res)

#SetSetpoint: sets the flow at which the MFC should work
def SetSetpoint(comPort, flowSetpoint):
	message="as"+str(flowSetpoint)
	res =''.join(format(ord(i), 'b') for i in message)
	#res=serialcmd.encode()
	res=str.encode(message)
	comPort.write(res)

def ChangeId(comPort):
	string="A@=B"
	res=string.encode()
	arr = bytes(string, 'utf-8')
	arr2 = bytes(string, 'ascii')
	arr3 = bytes(string, 'ansi')
	comPort.write(res)
	comPort.write(arr)
	comPort.write(arr2)
	comPort.write(arr3)
	comPort.write(b'A@=B')
	print("ok ?")
#########################################################
##               Advanced functions                    ##
#########################################################  

def streamData(comPort, iD, timeInterval, flowSetpoint):
	SetStreamInterval(comPort, iD, timeInterval)
	BeginStream(comPort, iD)
	SetSetpoint(comPort, flowSetpoint)

