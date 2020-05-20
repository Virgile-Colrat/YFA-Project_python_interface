import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)
ser.write(b'A\r')
