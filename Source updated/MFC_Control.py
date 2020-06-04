import serial

def OpenMFC(comPort):
	ser = serial.Serial(comPort, 19200, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)
	return ser
def MeasureAndReturn(comPort):
    comPort.write(b'A\r\n')
    