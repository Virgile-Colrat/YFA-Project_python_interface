import serial
import time
import binascii
import moduleTest
comds=[b'N\r',b'O\r',b'Q\r', b'R\r', b'S\r', b'T\r', b'U\r',b'V\r', b'W\r', b'X\r', b'Y\r', b'Z\r']
ligne=["","","","","","","","",""]#["Time","Sample number","Temperature","Humidity","Sensor response", "PM response", "Temperature MFC", "Current (nanofiber)", "Voltage (nanofiber)"] 9 arguments
data=["","","","","","","","","",""]

def OpenOmegaette():
	ser = serial.Serial('COM4', 9600, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)
	return ser

#ser.write(b'E\r')
#time.sleep(1)

def conversion(MSB, LSB):
	result=(MSB*255+LSB)/10
	return result

def NewLine():
	ligne=["","","","","","",""]

def MeasureAndPrint(ser):
	NewLine()
	ser.write(b'A\r')

def MeasureAndReturn(ser):
	NewLine()
	ser.write(b'A\r')
	for i in range(10):
		x=ser.read()
		#print(x)
		data[i]=ord(x)
	ligne[2]=conversion(data[5], data[6])
	ligne[3]=conversion(data[3], data[4])
	return ligne
#r=0
#while r<5:
#	ser.write(b'A\r')
#	#time.sleep(1)
#	"""for i in comds:
#		ser.write(i)
#		print(">>", i)
#		time.sleep(5)
#	"""	
#	#x=ser.read()
#	#print(ord(x))
#	i=0
#	while i != 10:
#		x=ser.read()
#		#print(ord(x))
#		
#		data[i]=ord(x)
#		#print(binascii.a2b_uu(ord(x)))
#		i=i+1
#	#print(r)
#	ligne[2]=conversion(data[5], data[6])
#	ligne[3]=conversion(data[3], data[4])
#	r=r+1
#	moduleTest.inp(ligne, r)
#	time.sleep(1)
#print("Done")
