import numpy as np
import pandas as pd

class Correlateur:
    
    def __init__(self, x, y):
        '''
        Avec x et y deux série temporelles.
        '''
        self.x = x
        self.y = y
        
    def correlation(self, start, end):
        # Covariance compris entre -1 et 1, plus on est proche de 0 plus les séries temporelles x et y sont indépendantes.
        # Si on est proche de 1 alors les deux séries temporelles sont très corrélés i.e si x auguemente alors y auguemente.
        # Si on est proche de -1 alors les deux séries temporelles sont très corrélés mais i.e. si x auguemente alors y décroit.

        if end == -1:

            x = self.x[start:]
            y = self.y[start:]
            
        else :

            x = self.x[start:end]
            y = self.y[start:end]

        xb=np.mean(x)
        yb=np.mean(y)
        xc=x-xb
        yc=y-yb
        
        aux1= 0
        aux2= 0
        aux3= 0
        
        for n in range(len(xc)):
            aux1 += xc[n] * yc[n]
            aux2 += xc[n]**2
            aux3 += yc[n]**2
        
        c= aux1/np.sqrt(aux2*aux3)
        print(c)
        return c
    
def CherryBlossomCorrelations():
    
    CherryData = pd.read_csv(rf"..\base_de_donnees\Japon\CherryBlossomFloweringDates\data.csv")

    TemperatureData = pd.read_csv(rf"..\base_de_donnees\Japon\Temperature\Kyoto\data.csv")

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
        
    x = res
    y = CherryData.iloc[:,0].tolist()[1143:-1]


    myCorrelateur = Correlateur(x,y)

    myCorrelateur.correlation(0,-1)
    
