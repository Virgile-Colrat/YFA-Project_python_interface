import csv
from datetime import datetime
Header=["Time","Sample number","Temperature","Humidity","Sensor response", "PM response", "Temperature MFC"]

def inp(line, i):
	with open('results.csv','a') as main:
		csv_writer=csv.writer(main, delimiter=",")
		line[0]=datetime.now()
		line[1]=i
		csv_writer.writerow(line)
def createfile():
	with open('results.csv','w') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(Header)