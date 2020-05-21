"""import pyvisa
rm = pyvisa.ResourceManager()
rm.list_resources()
inst = rm.open_resource('GPIB0::12::INSTR')
print(inst.query("*IDN?"))
"""
import serial
i=0
ser = serial.Serial('/dev/ttyACM0', baudrate=19200, timeout=0, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=0)
ser.write('C@=W\n\r')
ser.write('C20\n\r')
while i < 100:
	ser.write('A@=W\r\n')
	i+=1
print("fin !")
