from sklearn.metrics import confusion_matrix, roc_curve, auc, mean_squared_error, log_loss
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class problem:
    def __init__(self, name_outcome, model_dict, y_actual, class_predicted=True, the_other_class=False, ds_list=['Train', 'Test']):
        """
        A class to define the problem

        Args:
            name_outcome: What we are trying to predict
            model_dict: Dictionary with model names, predictions and probabilities  for different data sets (e.g {'Logistic Regression 1': [[y_pred_train_1, y_prob_train_1], [y_pred_test_1, y_prob_test_1]], 'KNN':[[y_pred_train_2, y_prob_train_2], [y_pred_test_2, y_prob_test_2]]})
            y_actual: list with series for each data ser, order should be the same as ds_list
            class_predicted: The class you are trying to predict (e.g. True, 1 or any class name you are targeting)
            the_other_class: The other class (e.g. False, 0)
            ds_list: dataset where the fit statistics are calulated (e.g. ['Train', 'Test'])
        """
        self.name_outcome = name_outcome
        self.model_dict = model_dict
        self.y_actual = y_actual
        self.class_predicted = class_predicted
        self.the_other_class = the_other_class
        self.ds_list = ds_list
        self.model_list = list(model_dict.keys())
        self.predictions = list(model_dict.values())
        self.higher_better_columns = ['acc', 'precision_1', 'precision_0', 'recall_1', 'recall_0','f1_1','f1_0', 'roc_auc']
        self.lower_better_columns = ['miss', 'ase','log_loss_value']
        self.high_col_ds = [f"{ds}_{column}" for ds in ds_list for column in self.higher_better_columns]
        self.low_col_ds = [f"{ds}_{column}" for ds in ds_list for column in self.lower_better_columns]
    
    def stats_1_model_ds(self, y_actual, y_pred, y_prob_1, model_name, ds):
        """
        Creates stats for a specific model and dataset combination

        Args:
            y_actual: actual outcomes, it will be converted to pandas series.
            y_pred: predictions from model
            y_prob_1: probabilities of positive cases from model
            model_name: Name to appear in the graphs and tables
            ds: dataset where the fit statistics are calulated (e.g. Train, Test, Validation)
        """
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
        fpr, tpr, thresholds = roc_curve(y_actual, y_prob_1)
        roc_auc = auc(fpr, tpr)
        ase = mean_squared_error(y_actual, y_prob_1)
        log_loss_value = np.float64(log_loss(y_actual, y_prob_1))
        return {'model_name':model_name, 'ds':ds,
                'acc':acc, 'miss':miss, 
                'precision_1':precision_1, 'precision_0':precision_0, 
                'recall_1':recall_1, 'recall_0':recall_0, 
                'f1_1':f1_1, 'f1_0':f1_0,
                'roc_auc':roc_auc, 'ase':ase, 'log_loss_value':log_loss_value}
    
    def stat_table(self):
        """
        This will create a table with all models and datasets combination and all fit statistics
        """
        results = pd.DataFrame()
        for m in self.model_list:
            for j, ds in enumerate(self.ds_list):
                stats = self.stats_1_model_ds(self.y_actual[j], self.model_dict[m][0][j], self.model_dict[m][1][j], m, ds)
                results = pd.concat([results, pd.DataFrame([stats])], ignore_index=True)
        return results
    
    def stat_table_transposed(self):
        df = self.stat_table().sort_values('ds')
        pivoted_df = df.pivot(index='model_name', columns='ds')
        pivoted_df.columns = [f"{col[1]}_{col[0]}" for col in pivoted_df.columns]
        pivoted_df = pivoted_df.reset_index()
        cols = ['model_name'] + sorted([col for col in pivoted_df.columns if col != 'model_name'])
        pivoted_df = pivoted_df[cols]
        return pivoted_df
    
    def highlight_best(self, s):
        is_higher_better = s.name in self.high_col_ds
        is_lower_better = s.name in self.low_col_ds
        if is_higher_better:
            best_value = s.max()
        elif is_lower_better:
            best_value = s.min()
        else:
            return [''] * len(s)
        return ['color: red; font-weight: bold;' if v == best_value else '' for v in s]
    
    def show_table(self):
        df = self.stat_table_transposed()
        return df.style.apply(self.highlight_best, axis=0)