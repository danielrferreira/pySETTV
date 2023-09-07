# Data Partition
To avoid overfitting we usually split our data into training and validation/test. The default of the code is to split 50/50 Train/Validation. If your modeling method uses the Validation to select model, I encourage you to use Test as well, so you can have an unbiased estimation of the fit statistic.

The function used pandas sample method, you can find a notebook in this folder with an alternative (using numpy and pandas) and the comparison between the two functions performances. 
