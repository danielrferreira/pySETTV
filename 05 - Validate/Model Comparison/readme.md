# Model Comparison

This section is a bit different from the earlier ones. I noticed a gap when moving from SAS Miner to R and Python, so I decided to create a class with some functions to compare models. It focuses on categorical outcomes but can be adapted for quantitative variables if needed.

The py file contains a class called problem and the notebook show how to import and use it. There are functions to:
- Show all fit statistics accross all models and datasets (e.g. Train, Validation, Test), formatted to highlight best models
- Graph with all fit statistics by model and datasets
- ROC curve comparison + Area under curve