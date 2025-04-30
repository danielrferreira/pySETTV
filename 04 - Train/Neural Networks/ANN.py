# Pre process
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
bat = pd.read_csv(folder+'/'+file, index_col=index)

train = bat[bat['year']==2021]
test = bat[bat['year']==2022]
y_train = train['hr_10'].copy()
X_train = train[['ab','exit_velocity_avg', 'batting_avg','r_total_stolen_base']].copy()
X_train['exit_velocity_avg'] = X_train['exit_velocity_avg'].fillna(X_train['exit_velocity_avg'].median())
y_test = test['hr_10'].copy()
X_test = test[['ab','exit_velocity_avg', 'batting_avg','r_total_stolen_base']].copy()
X_test['exit_velocity_avg'] = X_test['exit_velocity_avg'].fillna(X_test['exit_velocity_avg'].median())

# Default MLP
model1 = MLPClassifier()
model1.fit(X_train, y_train)
y_pred = model1.predict(X_test)

# You can change the number of hidden layers using hidden_layer_sizes, this example creates 2 hidden layers with 100 and 50 units each.
model2 = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=300, random_state=42)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
accuracy_score(y_test, y_pred2)

# 100 units is a very complex network, let's simplify it
model3 = MLPClassifier(hidden_layer_sizes=(4,4), max_iter=300, random_state=42)
model3.fit(X_train, y_train)
y_pred3 = model2.predict(X_test)
accuracy_score(y_test, y_pred3)

# We can also add Regularization to avoid overfit
model4 = MLPClassifier(hidden_layer_sizes=(50,), max_iter=200, alpha=0.01, random_state=42)
model4.fit(X_train, y_train)
y_pred4 = model4.predict(X_test)
accuracy_score(y_test, y_pred4)

# By default, the activation function is Rectified Linear Unit, a very simple (max(0,x)) and efficient activation, but for more classic ANN implementations, we used tanh:
# This model also uses learning rate and changed the solver algorithm.
model5 = MLPClassifier(hidden_layer_sizes=(100,), activation='tanh', solver='sgd', learning_rate_init=0.01, max_iter=300, random_state=42)
model5.fit(X_train, y_train)
y_pred5 = model5.predict(X_test)
accuracy_score(y_test, y_pred5)
