# Boosting Techniques for Classification
Boosting is also a family of Ensemble methods (like random forests) that uses multiple models to make a prediction. The difference is that Boosting use sequential models, instead of running multiple models in parallel mode. It works by iteratively training new models to address the shortcomings of previous models, gradually improving overall performance.

This code go through:
- AdaBoostClassifier: Fits weaker models (tree stumps by defaul) and then reweight the observations so the missclassified can have more weight for the next model. The weights of misclassified observations are increased multiplying the previous weight by exp(amount of say). The correctly classified are decreased by multiplying by exp(-amount of say). Amount of say is a function of errors the tree made (sum of weights of missclassified observations).
- GradientBoostingClassifier: For binary classification problems,  and loss function = ‘log_loss’, the model fits one tree per boosting iteration and uses the logistic sigmoid function (expit) as inverse link function to compute the predicted positive class probability.
- HistGradientBoostingClassifier: A much faster estimator for large datasets (n > 10000)

