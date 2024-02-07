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
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, pred_test)
missclass = 1-accuracy 
print('Accuracy:', round(accuracy,4))
print('Missclassification:', round(missclass,4))

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

#%%
# Or you can use classification report
from sklearn.metrics import classification_report
print(classification_report(y_test, pred_test))

# This function can help with simple fit statistics
from sklearn.metrics import accuracy_score, classification_report, roc_curve, auc

def accuracy_report(model,values_list):
    '''This function will assess model performance. Given a sklearn model it will Predict, and measure performance for both Test and Train Data'''
    #Train
    print('Train Data:\n-----------')
    pred_train = model.predict(X_train)
    accuracy_train = accuracy_score(y_train, pred_train)
    print('Accuracy:', round(accuracy_train,4))
    print(classification_report(y_train, pred_train))
    roc_plot(model,X_train,y_train,values_list)
    #Test
    print('Test Data:\n----------')
    pred_test = model.predict(X_test)
    accuracy_test = accuracy_score(y_test, pred_test)
    print('Accuracy:', round(accuracy_test,4))
    print(classification_report(y_test, pred_test))
    roc_plot(model,X_test,y_test,values_list)
def roc_plot(model,X_data,y_data,values_list):
    y_scores = model.predict_proba(X_data)[:, 1]
    y_data = y_data.map({values_list[0]:0,values_list[1]:1})
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
