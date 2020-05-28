import serial
import time

comds=[b'N\r',b'O\r',b'Q\r', b'R\r', b'S\r', b'T\r', b'U\r',b'V\r', b'W\r', b'X\r', b'Y\r', b'Z\r']
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)
#ser.write(b'E\r')
#time.sleep(1)
ser.write(b'P\r')
#time.sleep(1)
"""for i in comds:
	ser.write(i)
	print(">>", i)
	time.sleep(5)
	"""
x=ser.read()
print(ord(x))
while x != '':
	print(ord(x))
	x=ser.read()
<<<<<<< HEAD
             # close port

"""
s = serial.Serial('/dev/ttyACM0')
s.write(b'P')
=======
"""             # close port
ser = serial.Serial('COM4', 9600, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)
ser.write(b'A\r')
>>>>>>> 37e9dd10be9e6950a3af561f6d96842466e9d7b4
res = s.read()
print(res)
"""