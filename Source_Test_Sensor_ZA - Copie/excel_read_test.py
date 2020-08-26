import pandas as pd
import csv

data = pd.read_excel ('results-076.2-variable_temp_LED_2.30-bckp.xlsx') 
df = pd.DataFrame(data, columns= ['Temperature (°C)'])
current=pd.DataFrame(data, columns= ['Nanofiber current (A)'])
temp=21.2
sommeCumul=0
#print (current.iloc[0]['Nanofiber current (A)'])
j=0

def save(temp, val):
    line=["",""]
    filename='average.csv'
    with open(filename,'a', newline='') as main:
            csv_writer=csv.writer(main, delimiter=",")
            line[0]=temp
            line[1]=val
            csv_writer.writerow(line)

def createfile(filename):
	with open(filename,'w', newline='') as main:
		csv_writer=csv.writer(main, delimiter=",")
createfile('average.csv')

for i in range(3001): 
    #print(i)
    trueTemp=int(df.iloc[i]['Temperature (°C)']*10)
    actTemp=float(trueTemp)/10
    #print('temp ',temp)
    temp=float(int(temp*10))/10
    print('actTemp ', actTemp)
    print('temp ',temp)
    if temp==23.5 or temp==24.0 or temp==25.0 or temp==29.0 or temp==33.4 or temp==35.2 or temp==40.6 or temp==46.4 or temp==46.9 or temp==47.4 or temp==49.1 or temp==49.4 or temp==51.8 or temp==52.3 or temp==56.8:
        temp=temp+0.1
    elif temp==31.8:
        temp=temp+0.2
    else:
        pass
    if  actTemp==temp:
        #print('ok')
        #print (current.iloc[i]['Nanofiber current (A)'])
        sommeCumul=sommeCumul+current.iloc[i]['Nanofiber current (A)']
        #print(sommeCumul)
        j=j+1
    elif j==0:
        print('o_o')
    
    
    else:
        #print(sommeCumul/j)
        save(actTemp, sommeCumul/j)
        sommeCumul=0
        temp=temp+0.1
        #print('temp ',temp)
        j=0
