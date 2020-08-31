import csv
from datetime import datetime
Header=["Time","Sample number","Temperature (°C)","Humidity (%RH)","Sensor response (Ohm)", "PM response", "Temperature MFC (°C)", "Nanofiber current (A)", "Nanofiber voltage (V)"]

def inp(filename,line, i):
	filename=filename+'.csv'
	with open(filename,'a', newline='') as main:
		csv_writer=csv.writer(main, delimiter=",")
		line[0]=datetime.now()
		line[1]=i
		csv_writer.writerow(line)
def createfile(filename):
	filename=filename+'.csv'
	with open(filename,'w', newline='') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(Header)