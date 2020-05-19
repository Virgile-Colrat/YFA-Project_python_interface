import pySerial

ser = serial.Serial('/dev/ttyUSB', 9600, timeout=0,parity=serial.PARITY_EVEN, rtscts=1)
