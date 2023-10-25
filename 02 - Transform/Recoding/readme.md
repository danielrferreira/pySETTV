# Recoding Columns
Many times our variables/features/columns need recoding. Let's cover some of the cases where recoding would be benefit for your ML Model:
* Categorical columns need to be transformed into numerical columns to be used in formula-based algorithms (Regressions, NN, SVM, k-NN and many others)
  - One-Hot Encodding: Binary Dummies for each category
  - Label Encoding: Simple Mapping of values (A -> 1, B -> 2)
* Categorical columns have huge cardinality (Too many categories) and grouping them can be beneficial to avoid curse of dimensionality.
* Numerical input features have complex relantionships with outcome and categorizing them before one-hot encoding can simplify things
* Windowing: Imputation of outliers
