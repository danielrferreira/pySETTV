# Data Partition
To avoid overfitting we usually split our data into training and validation/test. The default of the code is to split 50/50 Train/Validation. If your modeling method uses the Validation to select model, I encourage you to use Test as well, so you can have an unbiased estimation of the fit statistic.

The function used pandas sample method, you can find a notebook in this folder with an alternative (using numpy and pandas) and the comparison between the two functions performances. 

Important to note that many people like to split their data into y and x (e.g. y_train, x_train, y_test, x_test). Youn can use this code and slice the result later, or also use [train_test_split method from sklearn.model_selection](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).
