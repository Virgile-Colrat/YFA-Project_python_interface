import csv
def inp(line):
	with open('menuse.csv','w') as main:
		csv_writer=csv.writer(main, delimiter=",")
		csv_writer.writerow(line)