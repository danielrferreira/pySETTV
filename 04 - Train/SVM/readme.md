# Support Vector Machine

SVC understanding can be splitted in 3 main areas:
1) Kernel Functions & Trick: How SVC move data to higher dimensions?
2) Support Vector Classifier: How SVC finds an optimal hyperplane that splits data.
3) All Linear Algebra and Calculus that supports 1 & 2.

We are not getting deeper in the theory, but the main idea is that SV Classifier (#2) is the linear combination of the inputs that we can use to split the data. Just like decision trees, but now the line wouldn't be parallel to one of the axis. Kernel functions (#1) are a math trick to create additional dimensions where the data can be easily splitted. All this math uses concepts from Linear Algebra and Calculus (#3). For instance, to find the optimal classifier, we need to understand vector projections and to understand radial basis kernel, we need to understand Taylor expansions.

This code will only touch on practical cases and how to fine tune your model to avoid underfitting/overfitting.
