import pandas as pd
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, make_scorer

# Setup
folder = '../../06 - Utility & References/Data'
file = 'batting_2021_2024.csv'
index = 'player_id'
bat = pd.read_csv(folder+'/'+file, index_col=index)
X = bat[['ab', 'batting_avg']].copy()
bat['hr_10'] = (bat['home_run']>10)
y = bat['hr_10'].copy()
model = LogisticRegression()

# Perform cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scorer = make_scorer(accuracy_score)
scores = cross_val_score(model, X, y, cv=cv, scoring=scorer)

# Output results
print("Cross-validation accuracy scores:", scores)
print("Mean cross-validation accuracy:", scores.mean())