#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:51:20 2024

@author: danielferreira
"""
# Pre-Process
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
import os
folder = '../../06 - Utility & References/Data'
file = 'player_batting_enriched.csv'
index = 'player_id'
os.chdir(folder)
bat = pd.read_csv(file, index_col=index)
train = bat[bat['year']==2021]
test = bat[bat['year']==2022]
y_train = train['hr_10'].copy()
X_train = train[['ab','exit_velocity_avg', 'batting_avg','r_total_stolen_base']].copy()
X_train['exit_velocity_avg'] = X_train['exit_velocity_avg'].fillna(X_train['exit_velocity_avg'].median())
y_test = test['hr_10'].copy()
X_test = test[['ab','exit_velocity_avg', 'batting_avg','r_total_stolen_base']].copy()
X_test['exit_velocity_avg'] = X_test['exit_velocity_avg'].fillna(X_test['exit_velocity_avg'].median())

#%%
# Simple Logistic Regression
model1 = LogisticRegression()
model1.fit(X_train, y_train)
pred_test = model1.predict(X_test)

#%%
# Pure Classification

#%%

#%%
# Simple Accuracy and Misclassification
accuracy = accuracy_score(y_test, pred_test)
missclass = 1-accuracy 
print('Accuracy:', round(accuracy,4))
print('Missclassification:', round(missclass,4))

#%%
# Because Accuracy and Missclassification can hide problems in one of the categories, we might use confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, pred_test)
plt.figure(figsize=(4, 3))
sns.heatmap(cm, annot=True, fmt="d", cbar=False, cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

#%%
# You can use confusion matrix object to calculate accuracy, precision,...
from sklearn.metrics import confusion_matrix
def stats_v1(y_test, pred_test):
    cm = confusion_matrix(y_test, pred_test)
    acc = (cm[0,0]+cm[1,1])/cm.sum()
    miss = 1-acc
    TP = cm[1,1] 
    FP = cm[0,1]
    TN = cm[0,0]
    FN = cm[1,0]
    precision_1 = TP / (TP+FP)
    precision_0 = TN / (TN+FN)
    recall_1 = TP / (TP+FN)
    recall_0 = TN / (TN+FP)
    metrics = [acc,miss,precision_1,precision_0,recall_1,recall_0]
    for i, metric_name in zip(metrics, ['Accuracy', 'Miss Rate', 'Precision (Class 1)', 'Precision (Class 0)', 'Recall (Class 1)', 'Recall (Class 0)']):
        print(f'{metric_name}: {i}')
stats_v1(y_test,pred_test)

#%%
# Or you can use classification report
print(classification_report(y_test, pred_test))

#%%
# To understand the differennce across different thresholds, this code can calculate fit stats for different thresholds:
def stats_v2(y_test, pred_test):
    cm = confusion_matrix(y_test, pred_test)
    acc = (cm[0,0]+cm[1,1])/cm.sum()
    miss = 1-acc
    TP = cm[1,1] 
    FP = cm[0,1]
    TN = cm[0,0]
    FN = cm[1,0]
    precision_1 = TP / (TP+FP)
    precision_0 = TN / (TN+FN)
    recall_1 = TP / (TP+FN)
    recall_0 = TN / (TN+FP)
    return acc, miss, precision_1, precision_0, recall_1, recall_0
prob_test = model1.predict_proba(X_test)
min_p, max_p = np.min(prob_test), np.max(prob_test)
thre = min_p
pred_test_min = (prob_test[:,1] > thre)
acc, miss, precision_1, precision_0, recall_1, recall_0 = stats_v2(y_test, pred_test_min)
fit_stats = pd.DataFrame({'thre':thre, 'acc':acc, 'miss':miss, 'precision_1':precision_1, 'precision_0':precision_0, 'recall_1':recall_1, 'recall_0':recall_0},index=[0])
ind = 1
for thre in np.arange(min_p+0.01,max_p,0.01):
    pred_test_temp = (prob_test[:,1] > thre)
    acc, miss, precision_1, precision_0, recall_1, recall_0 = stats_v2(y_test, pred_test_temp)
    temp_df = pd.DataFrame({'thre':thre, 'acc':acc, 'miss':miss, 'precision_1':precision_1, 'precision_0':precision_0, 'recall_1':recall_1, 'recall_0':recall_0},index=[ind])
    ind +=1
    fit_stats = pd.concat([fit_stats,temp_df])

#%%
# You can plot any of these stats
fit_stats.plot(x='thre',y='acc')
plt.title('Accuracy by Threshold')
plt.show()
max_acc_thre = fit_stats[fit_stats['acc']==np.max(fit_stats['acc'])][['thre','acc']]
print(max_acc_thre)

#%%
# Recall of 1 and 0:
fit_stats.plot(x='thre',y=['recall_0','recall_1'])
plt.title('Recall by Threshold')
plt.show()
# If you want to find the intersection:
fit_stats['recall_diff'] = abs(fit_stats['recall_0']-fit_stats['recall_1'])
inter = fit_stats[fit_stats['recall_diff']==np.min(fit_stats['recall_diff'])]
print(f'Intersection:\n{inter["thre"]}')

#%%
# Precision vs Recall:
fit_stats.plot(x='thre',y=['precision_1','recall_1'])
plt.title('Precision vs Recall by Threshold')
plt.show()

#%%
# Probability Estimation

#%%

#%%
# When you need probabilities and the method supports probabilities generation, predict_proba() can help
prob_test = model1.predict_proba(X_test) # probabilities will follow the order of model1.classes_
prob_test # It contains all classes probabilities (presented in a numpy multi dimensional array)

#%%
# MSE, RMSE and MAE can help
mae = abs(y_test-prob_test[:,1]).mean()
print(f'Mean Absolute Value = {mae}')
mse = ((y_test-prob_test[:,1])**2).mean()
print(f'Mean Squared Value = {mse}')
rmse=np.sqrt(mse)
print(f'Root Mean Squared Value = {rmse}')

#%%
# Ranking 

#%%

#%%
# Area Under ROC Curve
from sklearn.metrics import roc_auc_score
area_uc_v1 = roc_auc_score(y_test, prob_test[:,1])
print(f'AUROCC = {area_uc_v1}')

#%%
# roc_curve creates everything needed for a ROC Curve
from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, prob_test[:,1])
area_uc_v2 = auc(fpr, tpr)
print(f'AUROCC = {area_uc_v2}')

#%%
# You can draw the graphs with the new objects created by roc_curve
plt.figure(figsize=(6, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.show()

#%%
# Function to draw roc curve
def roc_plot(model,X_data,y_data):
    y_scores = model.predict_proba(X_data)[:, 1]
    y_data = y_data.map({(list(model.classes_))[0]:0,(list(model.classes_))[1]:1})
    fpr, tpr, thresholds = roc_curve(y_data, y_scores)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(3, 3))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()
    
#%%
# Calling the function
roc_plot(model1,X_test,y_test)

#%%
# Some people also like to see the percentage of 1's captured by percentile (after ranking by the model)
plt.title('True Positive Rate by percentile')
pd.Series(tpr).plot()
plt.axhline(y=0.5)
plt.show()   

#%%
# Bonus: This function can help with simple fit statistics for both test and train
from sklearn.metrics import accuracy_score, classification_report, roc_curve, auc

def accuracy_report(model):
    '''This function will assess model performance. Given a sklearn model it will Predict, and measure performance for both Test and Train Data'''
    #Train
    print('Train Data:\n-----------')
    pred_train = model.predict(X_train)
    accuracy_train = accuracy_score(y_train, pred_train)
    print('Accuracy:', round(accuracy_train,4))
    print(classification_report(y_train, pred_train))
    roc_plot(model,X_train,y_train)
    #Test
    print('Test Data:\n----------')
    pred_test = model.predict(X_test)
    accuracy_test = accuracy_score(y_test, pred_test)
    print('Accuracy:', round(accuracy_test,4))
    print(classification_report(y_test, pred_test))
    roc_plot(model,X_test,y_test)
def roc_plot(model,X_data,y_data):
    y_scores = model.predict_proba(X_data)[:, 1]
    y_data = y_data.map({(list(model.classes_))[0]:0,(list(model.classes_))[1]:1})
    fpr, tpr, thresholds = roc_curve(y_data, y_scores)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(3, 2))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()

#%%
# Calling the function
accuracy_report(model1)

#%% Function for all stats
def all_stats(y_pred, y_prob, y_data, class_predicted, the_other_class):
    """
    Gets all stats from 1 model and one dataset

    Args:
        y_pred: categorical prediction from model
        y_prob: probability of outcome to happen from model
        y_data: categorical actual values 
        class_predicted: The class you want to predict
        the_other_class: The other class
    """
    y_data = pd.Series(y_data).map({the_other_class:0,class_predicted:1})
    y_pred = pd.Series(y_pred).map({the_other_class:0,class_predicted:1})
    fpr, tpr, thresholds = roc_curve(y_data, y_prob[:,1])
    roc_auc = auc(fpr, tpr)
    cm = confusion_matrix(y_data, y_pred)
    acc = (cm[0,0]+cm[1,1])/cm.sum()
    miss = 1-acc
    TP = cm[1,1] 
    FP = cm[0,1]
    TN = cm[0,0]
    FN = cm[1,0]
    precision_1 = TP / (TP+FP)
    precision_0 = TN / (TN+FN)
    recall_1 = TP / (TP+FN)
    recall_0 = TN / (TN+FP)
    f1_1 = 2 * (precision_1 * recall_1) / (precision_1 + recall_1)
    f1_0 = 2 * (precision_0 * recall_0) / (precision_0 + recall_0)
    ase = mean_squared_error(y_data, y_prob[:,1])
    log_loss_value = log_loss(y_data, y_prob[:,1])
    return [roc_auc, acc, miss, precision_1, precision_0, recall_1, recall_0, f1_1, f1_0, ase, log_loss_value]