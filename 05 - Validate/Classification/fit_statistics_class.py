# Fit a logistic regression model to the training data
model1 = LogisticRegression()
model1.fit(X_train, y_train)
pred_test = model1.predict(X_test)

# Simple Accuracy and Misclassification
accuracy = accuracy_score(y_test, pred_test)
missclass = 1-accuracy 
print('Accuracy:', round(accuracy,4))
print('Missclassification:', round(missclass,4))

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
