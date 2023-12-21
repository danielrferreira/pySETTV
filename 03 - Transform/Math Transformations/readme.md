# Math Transformations
Utilizing mathematical transformations is a common practice to mitigate the influence of outliers and align with model assumptions. Examples include transformations such as log(x+1), and log, among others. This code will go through the following topics:
* Common transformations:
  - log(x): Reduces the impact of outliers and scales down large values.
  - log(x+1): Reduces the impact of outliers, scales down large values and avoid log(0).
  - sqrt(x): Similar to the logarithmic transformation, reduces the impact of large values.
  - x^2: Highlights differences among small values.
  - box-cox: Generic transformation that maximizes likelihood under normal assumption.
  - winsoring: replace outliers
* Functions to apply the same transformation to multiple variables
* Function to perform multiple transformations and plot original vs new distributions
