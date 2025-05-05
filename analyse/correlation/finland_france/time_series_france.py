import pandas as pd

average_anual_temperature = pd.read_csv(rf"..\..\..\base_de_donnees\France\Temp_Moyenne_mesurées_Beaune_1850_2024.csv")

Temp_data = average_anual_temperature.iloc[:,1].tolist()
Years_training = average_anual_temperature.iloc[:,0].tolist()

def vendage_data_maker():
    
    data = pd.read_csv(rf"..\..\..\base_de_donnees\France\Vendanges_beaune_1355_2018.csv")
    
    year = data.iloc[:, 0].tolist()
    doy = data.iloc[:, 1].tolist()
    
    training = []
    for i in range(len(data)):
        if year[i] in Years_training:
            training.append(doy[i])
            
    return doy,training,year

Vendange_data, Vendage_training_data, Years = vendage_data_maker()