import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os
import scipy.stats as stats
from statsmodels.graphics.tsaplots import plot_acf

folder = '/Users/danielferreira/Documents/git/pySETTV/06 - Utility & References/Data'
file = 'bat_22_clean.csv'
index = 'player_id'
os.chdir(folder)
bat_22 = pd.read_csv(file, index_col=index)
X = np.array(bat_22['batting_avg']).reshape(-1,1) # reshape is needed because sklearn always expect 2D arrays (for multiple linear regression)
y = bat_22['y_2023_avg']
model2 = LinearRegression()
model2.fit(X,y) # Fits model
y_pred = model2.predict(X) # Create predictions
residuals = y - y_pred

# 1) Homocedasticity
# We’ll plot residuals against predicted values. If the variance of residuals is constant (no clear pattern), the assumption holds.
plt.scatter(y_pred, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Values')
plt.show()

# What to look for:
# Points should be randomly scattered around the horizontal line at 0.
# If you see a cone shape or clear pattern, it violates homoscedasticity.

# 2) Normality of Residuals
# We’ll check if the residuals follow a normal distribution using a histogram and a Q-Q plot.
# Histogram of residuals
sns.histplot(residuals, kde=True)
plt.title('Histogram of Residuals')
plt.xlabel('Residuals')
plt.show()
# Q-Q Plot
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot of Residuals')
plt.show()

# What to look for:
# Histogram: Residuals should resemble a bell curve.
# Q-Q plot: Residuals should fall roughly along the diagonal line.

# 3) Error Independence. This one is tricky, you have to think if the errors have any correlation, for cases that the order of the table makes sense you can see if the errors have correlation.
# We’ll calculate and plot the autocorrelation of residuals using a correlogram. This ensures no correlation between residuals.
# Plot autocorrelation of residuals
plot_acf(residuals)
plt.title('Autocorrelation of Residuals')
plt.show()
# What to look for:
# Residual autocorrelations should be close to zero for all lags.
# Significant correlations indicate a violation of independence.

# 4) Linearity
# We’ll check if the relationship between the predictors and the outcome is linear. A residuals vs. predictor plot helps confirm this.
# Plot residuals vs predictor
plt.scatter(X, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('Predictor (X)')
plt.ylabel('Residuals')
plt.title('Residuals vs Predictor')
plt.show()
# What to look for:
# No clear pattern (e.g., curve, funnel shape) should appear.
# If a pattern exists, the assumption of linearity is violated.