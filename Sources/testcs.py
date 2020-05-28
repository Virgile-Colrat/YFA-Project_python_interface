import csv
from datetime import datetime 
import random
Header=["Time","Sample number","Temperature","Humidity","Sensor response", "PM response", "Temperature MFC"]
dataLine=["","","","","","",""]
with open('main.csv','w') as main:
	csv_writer=csv.writer(main, delimiter=",")
	csv_writer.writerow(Header)
	#csv_writer.writerow(lined)
	i=0
	while i < 10000:
		dataLine[0]=datetime.now()
		dataLine[1]=i
		dataLine[2]=random.randint(0, 40)
		dataLine[3]=random.randint(15, 90)
		dataLine[4]=random.randint(0, 100)
		dataLine[5]=random.randint(0, 100)
		dataLine[6]=random.randint(0, 40)
		csv_writer.writerow(dataLine)
		i=i+1
#with  open('main.csv','r') as main:
#	csv_reader=csv
	#for ligne in csv_writer:
	#	print(ligne)
	