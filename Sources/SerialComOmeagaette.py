import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)
ser.write(b'E\r')
time.sleep(3)
ser.write(b'E\r')
time.sleep(1)
ser.write(b'P\r')
x=ser.read()
"""print(ord(x))"""
while x != 0:
	print(ord(x))
	x=ser.read()
	