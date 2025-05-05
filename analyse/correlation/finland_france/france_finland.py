from regression_FINLAND import temperature_reconstruite as temperature_reconstruite_finland
from regression_france import temperature_reconstruite as temperature_reconstruite_france
import pandas as pd

france = pd.Series(temperature_reconstruite_france)
finland = pd.Series(temperature_reconstruite_finland)

print(f"Corrélation {finland.corr(france)}")
print(f"Corrélation {france.corr(finland)}")