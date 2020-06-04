import csv
from datetime import datetime
Header=["Time","Sample number","Temperature","Humidity","Sensor response", "PM response", "Temperature MFC", "Current (nanofiber)", "Voltage (nanofiber)"]

def inp(filename,line, i):
	filename=filename+'.csv'
	with open(filename,'a') as main:
		csv_writer=csv.writer(main, delimiter=",")
		line[0]=datetime.now()
		line[1]=i
		csv_writer.writerow(line)
def createfile(filename):
	filename=filename+'.csv'
	with open(filename,'w') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(Header)