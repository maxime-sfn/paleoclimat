import numpy as np
import pandas as pd



def correlation(x,y):
    # Covariance compris entre -1 et 1, plus on est proche de 0 plus les séries temporelles x et y sont indépendantes.
    # Si on est proche de 1 alors les deux séries temporelles sont très corrélés i.e si x auguemente alors y auguemente.
    # Si on est proche de -1 alors les deux séries temporelles sont très corrélés mais i.e. si x auguemente alors y décroit.

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
    return c