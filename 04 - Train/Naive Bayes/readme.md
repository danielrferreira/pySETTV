# Naive Bayes
Some of the simplest yet effective algorithms in machine learning are categorized as Naive Bayes. Its fundamental concept involves calculating the probability of each category based on input data. These algorithms are a straightforward application of Bayes' Theorem, where through prioris estimation, we determine the posterior probability for each potential category. The observation is then classified under the category with the highest posterior probability.

Due to its inherent simplicity, Naive Bayes stands out as ones of the most scalable algorithms in machine learning. This code will show 3 Naive Bayes methods available in sklearn.naive_bayes module:

- Multinominal: All input variables are required to be categorical in nature but the algorithm can handle discrete data. The data still needs to be numeric, but it needs to be representions of categories.The prioris are calculated using simple proportions.
- Bernoulli: All input variables are required to be binary/boolean. If encoding is needed, consider utilizing pd.get_dummies(). The prioris are calculated using simple proportions.
- Gaussian: When you have quantitative inputs, this methods assumes normal distribution (with same mean and std) to calculate the prioris.
