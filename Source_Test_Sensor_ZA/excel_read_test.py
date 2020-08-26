import pandas as pd

data = pd.read_excel ('resultsTest.xlsx') 
df = pd.DataFrame(data, columns= ['Temperature (°C)'])
current=pd.DataFrame(data, columns= ['Nanofiber current (mA)'])
temp=20.9
sommeCumul=0
for i in range(6): 
    if  df.iloc[i]['Temperature (°C)']==temp:
        print (current.iloc[1]['Nanofiber current (mA)'])
        sommeCumul=current.iloc[1]['Nanofiber current (mA)']
    else:
        
        temp=temp+0.1