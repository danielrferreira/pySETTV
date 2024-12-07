
from sklearn.metrics import confusion_matrix, roc_curve, auc, mean_squared_error, log_loss
import pandas as pd
import matplotlib.pyplot as plt

class problem:
    def __init__(self, outcome, name_outcome, class_predicted, the_other_class):
        """
        A class to define the problem

        Args:
            outcome: actual outcomes pandas series of booleans, usually from test datasets
            name_outcome: What we are trying to predict
            class_predicted: The class you are trying to predict (e.g. True, 1 or any class name you are targeting)
            the_other_class: The other class (e.g. False, 0)
        """
        self.outcome = outcome
        self.name_outcome = name_outcome
        self.class_predicted = class_predicted
        self.the_other_class = the_other_class
    class problem_ds:
        def __init__(self, y_actual, datasets = ['Train','Test']):
            """
            A class for the type of data sets you have

            Args:
                y_actual: list of pandas series with actual values, if you have Train and Test you need a list with two series
                datasets: list of dataset types
            """
            self.y_actual = y_actual
            self.datasets = datasets
        class models:
            def __init__(self, model_names, y_preds, y_probs_1):
                """
                Last class with models information
                Args:
                    model_names: List with models you are testing
                    y_preds: list with pandas series with categorical predictions
                    y_probs_1: list with probabilities estimated by models
                """
                self.model_names = model_names
                self.y_preds = y_preds
                self.y_probs_1 = y_probs_1
            def classification_stats(self, y_actual, y_pred):
                y_actual = pd.Series(y_actual).map({self.the_other_class:0,self.class_predicted:1})
                y_pred = pd.Series(y_pred).map({self.the_other_class:0,self.class_predicted:1})
                cm = confusion_matrix(y_actual, y_pred)
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
                return [acc,miss,precision_1, precision_0, recall_1, recall_0, f1_1, f1_0]
            def classification_stats_all(self):
                for ds, actual in zip(self.datasets,self.y_actual):
                    print(f'{ds}\n')
                    y = actual
                    for m, pred in zip(self.model_names, self.y_preds):
                        print(f'{m}\n')
                        classification_stats(self,y,pred)
                    




    # def stats_print(self, pred):
    #     """
    #     Prints common classification stats

    #     Args:
    #         pred: numpy.ndarray boolean prediction from model
    #     """
    #     cm = confusion_matrix(self.outcome, pred)
    #     acc = (cm[0,0]+cm[1,1])/cm.sum()
    #     miss = 1-acc
    #     TP = cm[1,1] 
    #     FP = cm[0,1]
    #     TN = cm[0,0]
    #     FN = cm[1,0]
    #     precision_1 = TP / (TP+FP)
    #     precision_0 = TN / (TN+FN)
    #     recall_1 = TP / (TP+FN)
    #     recall_0 = TN / (TN+FP)
    #     metrics = [acc,miss,precision_1,precision_0,recall_1,recall_0]
    #     for i, metric_name in zip(metrics, ['Accuracy', 'Miss Rate', 'Precision (Class 1)', 'Precision (Class 0)', 'Recall (Class 1)', 'Recall (Class 0)']):
    #         print(f'{metric_name}: {round(i,3)}')
     
    # def roc_plot(self,y_prob, y_data):
    #     """
    #     Creates ROC Curve
    #     Args:
    #         y_prob: probability of outcome to happen from model
    #         y_data: categorical actual values 
    #     """
    #     y_data = y_data.map({self.the_other_class:0,self.class_predicted:1})
    #     fpr, tpr, thresholds = roc_curve(y_data, y_prob[:,1])
    #     roc_auc = auc(fpr, tpr)
    #     plt.figure(figsize=(3, 2))
    #     plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    #     plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    #     plt.xlim([0, 1])
    #     plt.ylim([0, 1.05])
    #     plt.xlabel('False Positive Rate')
    #     plt.ylabel('True Positive Rate')
    #     plt.title(f'Receiver Operating Characteristic - {self.name_outcome} - {self.class_predicted}')
    #     plt.legend(loc="lower right")
    #     plt.show()

    # def accuracy_report(model):
    #     '''WIP - This function will assess model performance. Given a sklearn model it will Predict, and measure performance for both Test and Train Data'''
    #     #Train
    #     print('Train Data:\n-----------')
    #     pred_train = model.predict(X_train)
    #     accuracy_train = accuracy_score(y_train, pred_train)
    #     print('Accuracy:', round(accuracy_train,4))
    #     print(classification_report(y_train, pred_train))
    #     roc_plot(model,X_train,y_train)
    #     #Test
    #     print('Test Data:\n----------')
    #     pred_test = model.predict(X_test)
    #     accuracy_test = accuracy_score(y_test, pred_test)
    #     print('Accuracy:', round(accuracy_test,4))
    #     print(classification_report(y_test, pred_test))
    #     roc_plot(model,X_test,y_test)

    # def all_stats(self, y_pred, y_prob, y_data):
    #     """
    #     Gets all stats from 1 model and one dataset

    #     Args:
    #         y_pred: categorical prediction from model
    #         y_prob: probability of outcome to happen from model
    #         y_data: categorical actual values 
    #     """
    #     y_data = pd.Series(y_data).map({self.the_other_class:0,self.class_predicted:1})
    #     y_pred = pd.Series(y_pred).map({self.the_other_class:0,self.class_predicted:1})
    #     fpr, tpr, thresholds = roc_curve(y_data, y_prob[:,1])
    #     roc_auc = auc(fpr, tpr)
    #     cm = confusion_matrix(y_data, y_pred)
    #     acc = (cm[0,0]+cm[1,1])/cm.sum()
    #     miss = 1-acc
    #     TP = cm[1,1] 
    #     FP = cm[0,1]
    #     TN = cm[0,0]
    #     FN = cm[1,0]
    #     precision_1 = TP / (TP+FP)
    #     precision_0 = TN / (TN+FN)
    #     recall_1 = TP / (TP+FN)
    #     recall_0 = TN / (TN+FP)
    #     f1_1 = 2 * (precision_1 * recall_1) / (precision_1 + recall_1)
    #     f1_0 = 2 * (precision_0 * recall_0) / (precision_0 + recall_0)
    #     ase = mean_squared_error(y_data, y_prob[:,1])
    #     log_loss_value = log_loss(y_data, y_prob[:,1])
    #     return [roc_auc, acc, miss, precision_1, precision_0, recall_1, recall_0, f1_1, f1_0, ase, log_loss_value]

import pandas as pd
from sklearn.metrics import confusion_matrix

class Problem:
    def __init__(self, outcome, name_outcome, class_predicted, the_other_class):
        """
        A class to define the problem.

        Args:
            outcome: actual outcomes pandas series of booleans, usually from test datasets.
            name_outcome: What we are trying to predict.
            class_predicted: The class you are trying to predict (e.g., True, 1).
            the_other_class: The other class (e.g., False, 0).
        """
        self.outcome = outcome
        self.name_outcome = name_outcome
        self.class_predicted = class_predicted
        self.the_other_class = the_other_class


class ProblemDS:
    def __init__(self, y_actual, datasets=['Train', 'Test']):
        """
        A class for the type of datasets you have.

        Args:
            y_actual: List of pandas series with actual values.
            datasets: List of dataset types.
        """
        self.y_actual = y_actual
        self.datasets = datasets


class Models:
    def __init__(self, model_names, y_preds, y_probs_1, class_predicted, the_other_class):
        """
        A class for models information.

        Args:
            model_names: List of models you are testing.
            y_preds: List of pandas series with categorical predictions.
            y_probs_1: List of probabilities estimated by models.
            class_predicted: The class you are trying to predict.
            the_other_class: The other class.
        """
        self.model_names = model_names
        self.y_preds = y_preds
        self.y_probs_1 = y_probs_1
        self.class_predicted = class_predicted
        self.the_other_class = the_other_class

    def classification_stats(self, y_actual, y_pred):
        y_actual = pd.Series(y_actual).map({self.the_other_class: 0, self.class_predicted: 1})
        y_pred = pd.Series(y_pred).map({self.the_other_class: 0, self.class_predicted: 1})
        cm = confusion_matrix(y_actual, y_pred)
        acc = (cm[0, 0] + cm[1, 1]) / cm.sum()
        miss = 1 - acc
        TP = cm[1, 1]
        FP = cm[0, 1]
        TN = cm[0, 0]
        FN = cm[1, 0]
        precision_1 = TP / (TP + FP)
        precision_0 = TN / (TN + FN)
        recall_1 = TP / (TP + FN)
        recall_0 = TN / (TN + FP)
        f1_1 = 2 * (precision_1 * recall_1) / (precision_1 + recall_1)
        f1_0 = 2 * (precision_0 * recall_0) / (precision_0 + recall_0)
        return [acc, miss, precision_1, precision_0, recall_1, recall_0, f1_1, f1_0]

    def classification_stats_all(self, datasets, y_actual):
        results = {}
        for ds, actual in zip(datasets, y_actual):
            dataset_results = {}
            for m, pred in zip(self.model_names, self.y_preds):
                stats = self.classification_stats(actual, pred)
                dataset_results[m] = stats
            results[ds] = dataset_results
        return results