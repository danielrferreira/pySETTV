# Pre-Process
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score
bat = pd.read_csv('player_batting_enriched.csv', index_col='player_id')
outcome = bat[bat['year']==2023]['batting_avg']
bat_22 = bat[bat['year']==2022].copy()
bat_22['y_2023_avg'] = outcome
bat_22 = bat_22[bat_22['y_2023_avg'].isna()==False] # Those who weren't in 2023 MBL
bat_22 = bat_22.drop(['team_id','hp_to_1b'], axis=1)
cols = ['team_name','division','league']
for x in cols:
    bat_22[x] = bat_22[x].fillna('Free-Agent')
bat_22['sprint_speed'] = bat_22['sprint_speed'].fillna(bat_22['sprint_speed'].mean())
inputs = ['player_age','ab', 'hit', 'home_run', 'k_percent','batting_avg','sprint_speed']
X = bat_22[inputs]
y = bat_22['y_2023_avg']

#%%
# The default ...
from sklearn.ensemble import GradientBoostingRegressor
model1 = GradientBoostingRegressor()
model1.fit(X,y)
pred = model1.predict(X)
print(explained_variance_score(y,pred))
