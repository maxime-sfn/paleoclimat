import pandas as pd

def timeSeries():
    
    CherryData = pd.read_csv(rf"..\..\..\base_de_donnees\Japon\CherryBlossomFloweringDates\data.csv")

    TemperatureData = pd.read_csv(rf"..\..\..\base_de_donnees\Japon\Temperature\Kyoto\data.csv")

    KyotoMeanTemperature = []

    i = 0
    for date in TemperatureData['Date']:
        if date[0] == "3" : # Tous les dates de mars
            KyotoMeanTemperature.append(TemperatureData["Kyoto"][i])
        i += 1
        
    res = []
    for i in range(len(KyotoMeanTemperature)//31):
        sum = 0
        for j in range(31):
            sum += KyotoMeanTemperature[i*31 + j]
        res.append(sum/31)
        
    x = CherryData.iloc[:,1].tolist()[1143:-1]
    y = res
    
    return x,y

def filterd_cherry_data():
    CherryData = pd.read_csv(rf"..\..\..\base_de_donnees\Japon\CherryBlossomFloweringDates\data.csv")
    X = CherryData.iloc[:,1].tolist()
    years = CherryData.iloc[:,0].tolist()

    for i in range(len(years)-1,0,-1):
        if X[i] == 0 : 
            X.pop(i)
            years.pop(i)
    
    return X,years

CherryDataTest, KyotoTemperature = timeSeries()
CherryData, Years = filterd_cherry_data()