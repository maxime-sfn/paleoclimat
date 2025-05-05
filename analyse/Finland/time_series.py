import pandas as pd

average_may_temperature = pd.read_csv(fr"..\..\base_de_donnees\Finland\temperature\data.csv")

Temp_data = average_may_temperature.iloc[:,1].tolist()
Years_training = average_may_temperature.iloc[:,0].tolist()

def lake_data_maker():
    
    data = pd.read_csv(rf"..\..\base_de_donnees\Finland\Lake\data.csv")
    
    year = data.iloc[:, 2].tolist() # Convert the first column to a list
    month = data.iloc[:, 3].tolist()
    day = data.iloc[:, 4].tolist()
    
    doy = []
    
    for i in range(len(month)):
        days = 0
        if month[i] == 4 :
            days = 31 + 28 + 31 + day[i]
        if month[i] == 5 :
            days = 31 + 28 + 31 + 30 + day[i]
        if month[i] == 6 :
            days = 31 + 28 + 31 + 30 + 31 + day[i]
        if year[i] % 4 == 0: # Si année bisextile
            days += 1
        doy.append(days)
        
    training_data = []
        
    for i in range(len(year)):
        if year[i] in Years_training:
            training_data.append(doy[i])
        
    return doy,training_data,year

Lake_data,Lake_training_data,Years = lake_data_maker()