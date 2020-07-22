import serial
from datetime import datetime
prevTime=datetime.now()
STM32= serial.Serial('COM8', 209700, timeout=10, rtscts=0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False)#Opens stm32 com port
while 1:
    print(datetime.now())
    
    