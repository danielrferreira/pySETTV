# pySETTV
Codes to Sample, Explore, Transform, Train Models and Validate Models. 

This repository is a collection of code snippets I created while studying Python and translating methods I previously used with SAS and R. It also reflects some of my professional experience working with these techniques.

Please note that this is not a Python package but rather a supplementary resource to the official documentation for libraries like scikit-learn, pandas, and NumPy. Each section typically includes a README file and a Python script with examples. In some cases, I've also added a Jupyter Notebook to demonstrate the functions and methods in action.

The README files usually explain the underlying technique, its practical applications, and guidance on when and how to tweak parameters for better results.

This resource is not focused on deep learning. Instead, it is better suited for scenarios where staying in touch with the data, exploring it, interpreting relationships, and building statistical models is the priority. It follows a structured framework:

- Sample: Access the data.
- Explore and Transform: Iterate within this loop to understand and prepare the data.
- Train: Build models.
- Validate: Assess and refine results.

## [01 - Sample](https://github.com/danielrferreira/pySETTV/tree/main/01%20-%20Sample)
- [Filter](https://github.com/danielrferreira/pySETTV/tree/main/01%20-%20Sample/Filter)
- [Simple Random Sample](https://github.com/danielrferreira/pySETTV/tree/main/01%20-%20Sample/Simple%20Random)
- [Stratified Sample](https://github.com/danielrferreira/pySETTV/tree/main/01%20-%20Sample/Stratified)
- [Data Partition (Train, Validation, Test)](https://github.com/danielrferreira/pySETTV/tree/main/01%20-%20Sample/Data%20Partition)
## [02 - Explore](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore)
* [Table Overall Structure](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Overall%20Structure)
* [Univariate](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Univariate):
  - [Missing Report](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Univariate/Missing)
  - [Categorical](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Univariate/Categorical)
  - [Quantitative](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Univariate/Quantitative)
  - [Skewed Quantitative](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Univariate/Skewed%20Quantitative)
* [Bivariate, pair-wise Analysis](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Bivariate):
  - [Categorical Outcome vs](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Bivariate/Categorical%20Outcome):
    - [Categorical Inputs](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Bivariate/Categorical%20Outcome/Categorical%20Inputs)
    - [Quantitative Inputs](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Bivariate/Categorical%20Outcome/Quantitative%20Inputs)
  - [Quantitative Outcome vs](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Bivariate/Quantitative%20Outcome):
    - [Categorical Inputs](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Bivariate/Quantitative%20Outcome/Categorical%20Inputs)
    - [Quantitative Inputs](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Bivariate/Quantitative%20Outcome/Quantitative%20Inputs) 
* [Cluster Analysis](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Cluster)
* [Dimension Reduction]():
  - [Feature Ranking](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Dimension%20Reduction/Feature%20Ranking)
  - [Principal Components](https://github.com/danielrferreira/pySETTV/tree/main/02%20-%20Explore/Dimension%20Reduction/PCA)
## [03 - Transform](https://github.com/danielrferreira/pySETTV/tree/main/03%20-%20Transform)
- [Merge and Append Tables](https://github.com/danielrferreira/pySETTV/tree/main/03%20-%20Transform/Merge%20and%20Append)
- [Aggregate Functions](https://github.com/danielrferreira/pySETTV/tree/main/03%20-%20Transform/Aggregate)
- [Variable Recoding](https://github.com/danielrferreira/pySETTV/tree/main/03%20-%20Transform/Recode)
- [Standardization](https://github.com/danielrferreira/pySETTV/tree/main/03%20-%20Transform/Standardization)
- [Math Transformations](https://github.com/danielrferreira/pySETTV/tree/main/03%20-%20Transform/Math%20Transformations)
- [Missing Handling](https://github.com/danielrferreira/pySETTV/tree/main/03%20-%20Transform/Missing%20Handling)
- [String Cleaning for Text Categorization](https://github.com/danielrferreira/pySETTV/tree/main/03%20-%20Transform/String%20Cleaning)
## [04 - Train Models](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train)
- [Linear Regression](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Linear%20Regression)
- [Generalized Linear Models](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Generalized%20Linear%20Regression)
- [Logistic Regression](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Logistic%20Regression)
- [Decision Trees](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Decision%20Tree)
- [Regression Trees](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Regression%20Tree)
- [Random Forest](https://github.com/danielrferreira/pySETTV/blob/main/04%20-%20Train/Random%20Forest/readme.md)
- [Boosting For Classification](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Boosting%20Classifiers)
- [Gradient Boosting For Quantification](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Gradient%20Boosting)
- [Neural Networks](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Neural%20Networks)
- [Support Vector Machine](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/SVM)
- [Naive Bayes](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Naive%20Bayes)
- [K-Nearest Neighbors](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/KNN)
- [Time Series](https://github.com/danielrferreira/pySETTV/tree/main/04%20-%20Train/Time%20Series)
## [05 - Validate Models](https://github.com/danielrferreira/pySETTV/tree/main/05%20-%20Validate)
- [Fit Statistics & Graphs for Quantitative Outcome](https://github.com/danielrferreira/pySETTV/tree/main/05%20-%20Validate/Quantitative)
- [Fit Statistics & Graphs for Categorical Outcome](https://github.com/danielrferreira/pySETTV/tree/main/05%20-%20Validate/Classification)
- [Linear Regressions Assumptions Check](https://github.com/danielrferreira/pySETTV/tree/main/05%20-%20Validate/Linear%20Regression%20Assumptions)
- [Model Comparison](https://github.com/danielrferreira/pySETTV/tree/main/05%20-%20Validate/Model%20Comparison)
- [Cross-Validation](https://github.com/danielrferreira/pySETTV/tree/main/05%20-%20Validate/Cross%20Validation)
## [06 - Utility & References](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References)
* [File Import](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20&%20References/File%20Import):
  - [Simple csv import](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20&%20References/File%20Import/Simple%20CSV%20Import)
  - [Function that allow multiple data formats](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20&%20References/File%20Import/Multiple%20Formats)
  - [Import from scratch](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20&%20References/File%20Import/Import%20from%20scratch)
* [File Export](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/File%20Export):
  - [Graphs](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/File%20Export/Graphs)
  - [Tables](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/File%20Export/Tables)
* [Reference](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference):
  - [Conditional and Loop Statements](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/Conditional%20and%20Loops)
  - [Lists, Tuples and Dictionaries](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/Lists%20Tuples%20and%20Dictionaries)
  - [Functions](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/Functions)
  - [Files](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/Files)
  - [Modules and Packages](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/Modules%20and%20Packages)
  - [Errors](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/Errors)
  - [OOP Topics](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/OOP)
  - [NumPy](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/NumPy)
  - [pandas](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Reference/pandas)

* [Data](https://github.com/danielrferreira/pySETTV/tree/main/06%20-%20Utility%20%26%20References/Data)
