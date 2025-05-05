from regression_FINLAND import temperature_reconstruite as temperature_reconstruite_finland
from regression_JAPAN import temperature_reconstruite as temperature_reconstruite_japan  
import pandas as pd

japan = pd.Series(temperature_reconstruite_japan)
finland = pd.Series(temperature_reconstruite_finland)

print(f"Corrélation {finland.corr(japan)}")
print(f"Corrélation {japan.corr(finland)}")