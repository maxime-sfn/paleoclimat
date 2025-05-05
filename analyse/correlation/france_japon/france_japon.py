from regression_JAPAN import temperature_reconstruite as temperature_reconstruite_japon
from regression_france import temperature_reconstruite as temperature_reconstruite_france
import pandas as pd

france = pd.Series(temperature_reconstruite_france)
japon = pd.Series(temperature_reconstruite_japon)

print(f"Corrélation {japon.corr(france)}")
print(f"Corrélation {france.corr(japon)}")