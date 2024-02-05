# Classification Models Assessment
Once a model has been executed, the immediate concern revolves around its performance. The pivotal question emerges: How effective is your model? The response to this query is contingent upon the ultimate purpose of your model:
- **Pure Classification:** In scenarios where the primary objective is accurate make guesses, metrics such as accuracy, misclassification rate, recall, precision, and F1 Score serve as crucial indicators to comprehend the overall quality of the model.
- **Probability Estimation:** When the model's output serves as an input for subsequent calculations, Average Squared Error proves to be more discerning, especially when striving for proximity to ideal values of 1 and 0.
- **Ranking:** For models tasked with ranking cases, Kolmogorov-Smirnov Statistic (KS) and Area Under the Curve (AUC) become invaluable measures to assess the model's ability to discriminate between different classes by comparing the cumulative distributions of the positive and negative cases (After Ranking based on your prediction).
 
