# Stratified Sample

This code can be used to draw stratified samples, so the randomization happens whitin categories of a choosen variable. In real business settings, we usually need to draw samples before creating pandas DataFrames (mostly SQL codes directly in databases), but there are times that only after exploration of data, we conclude that stratification is needed.

This code can also be used to balance samples, because some modelling techniques are sensitive to unbalenced data. K-NN and Decision Trees combined with a sample that only has 1% of cases as positives, will probally lead to models that predicts almost all cases as negatives. Balancing the sample can improve the model. If you balance the sample, you need to think about the bias the probablity estimates have.





