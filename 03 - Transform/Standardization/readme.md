## Standardization
Standardization is a crucial consideration in algorithmic processes. Many algorithms assume consistent column scales, yet this is rarely the reality. In practice, each variable typically possesses its own distinct scale. For instance, while the height of a person might be measured in meters, their income could be in thousands of dollars. Understanding and addressing these varying scales is essential for accurate and meaningful algorithmic computations. These code provides 3 methods:

- Minmax: (X-min)/(max-min)
- Standard Normalization: (X-mean)/std
- Robust: (X-Q1)/(Q3-Q1)

The code provides the sklearn method but also shows how to quickly create your own function.
