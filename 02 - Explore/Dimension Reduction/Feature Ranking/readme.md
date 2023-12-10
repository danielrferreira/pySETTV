# Feature Ranking 
Feature ranking accros different types of variables is tricky. You can categorize numerical variables, but the ranges used can change the results and is not fair to compare a categorical variable with a arbitraly categorized numerical one. This code will present a code to rank numerical columns and another one to rank categorical columns. 

I am also including a more advanced way of ranking features using Random Forest. Random Forest have impurity-based feature importances. The higher, the more important the feature. The importance of a feature is computed as the (normalized) total reduction of the criterion brought by that feature. It is also known as the Gini importance.
