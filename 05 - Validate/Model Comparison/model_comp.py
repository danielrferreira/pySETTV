from sklearn.metrics import confusion_matrix, roc_curve, auc, mean_squared_error, log_loss
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns
import numpy as np
import math

class problem:
    def __init__(self, name_outcome, model_dict, y_actual, class_predicted=True, the_other_class=False, ds_list=['Train', 'Test']):
        """
        A class to define the problem

        Args:
            name_outcome: What we are trying to predict
            model_dict: Dictionary with model names, predictions and probabilities  for different data sets (e.g {'Logistic Regression 1': [[y_pred_train_1, y_prob_train_1], [y_pred_test_1, y_prob_test_1]], 'KNN':[[y_pred_train_2, y_prob_train_2], [y_pred_test_2, y_prob_test_2]]})
            y_actual: list with series for each data set, order should be the same as ds_list
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
        self.fit_stat_map = {'acc': 'Accuracy', 'precision_1': 'Precision: 1', 'precision_0': 'Precision: 0', 'recall_1': 'Recall 1', 'recall_0': 'Recall 0','f1_1': 'F1: 1','f1_0': 'F1: 0', 
                             'roc_auc': 'Area Under ROC', 'miss': 'Missclassification', 'ase': 'Average Squared Error','log_loss_value': 'Log Loss'}
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
        """"
        Transposing the table to have a better visualization and highlight best models
        """
        df = self.stat_table()
        pivoted_df = df.pivot(index='model_name', columns='ds')
        pivoted_df.columns = [f"{col[1]}_{col[0]}" for col in pivoted_df.columns]
        pivoted_df = pivoted_df.reset_index()
        cols = ['model_name'] + sorted([col for col in pivoted_df.columns if col != 'model_name'])
        pivoted_df = pivoted_df[cols]
        return pivoted_df
    
    def highlight_best(self, s):
        """
        If value is min or max, highlight the value in bold red. 
        """
        is_higher_better = s.name in self.high_col_ds
        is_lower_better = s.name in self.low_col_ds
        if is_higher_better:
            best_value = s.max()
        elif is_lower_better:
            best_value = s.min()
        else:
            return [''] * len(s)
        return ['color: red; font-weight: bold;' if v == best_value else '' for v in s]
    
    def show_fit_statistics_table(self):
        """"
        Show table with formatted values
        """
        df = self.stat_table_transposed()
        return df.style.apply(self.highlight_best, axis=0)
    
    def show_fit_statistics_graphs(self, ds):
        """"
        This function will show all models for each fit statistic

        Args:
            ds: Dataset you need to use
        """
        metrics = self.higher_better_columns + self.lower_better_columns
        df = self.stat_table()
        df = df[df['ds']==ds]
        df.drop('ds', axis=1)
        n_row = math.ceil(len(metrics) / 3)
        fig, axes = plt.subplots(nrows=n_row, ncols=3, figsize=(10, 10)) 
        axes=axes.flatten()
        palette = sns.color_palette('tab10', len(df['model_name'].unique()))
        hue_order = df['model_name'].unique()
        color_map = {model: color for model, color in zip(hue_order, palette)}
        for m, ax in zip(metrics, axes):
            min_value = df[m].min()  
            lower_padding = (df[m].max() - min_value) * 0.15 if min_value != 0 else 0
            higher_padding = (df[m].max() - min_value) * 0.15
            sns.barplot(x='model_name', y=m, data=df, ax=ax, hue='model_name', dodge=False, palette=color_map)
            ax.set_title(self.fit_stat_map[m])
            ax.set_xticks([])
            ax.set_xlabel('') 
            ax.set_ylabel('')
            ax.set_ylim(min_value - lower_padding, df[m].max() + higher_padding)
            for container in ax.containers:  
                for bar in container:
                    height = bar.get_height() 
                    x = bar.get_x() + bar.get_width() / 2
                    ax.text(x, height + higher_padding * 0.2, f'{height:.3f}',  ha='center', va='bottom', fontsize=10 )
        for ax in axes[len(metrics):]:
            ax.set_visible(False)
        legend_handles = [Patch(color=color, label=model) for model, color in color_map.items()]
        fig.legend(handles=legend_handles, loc='upper center', ncol=len(hue_order), title='Model Names', bbox_to_anchor=(0.5, 1))
        fig.suptitle(f"Fit Statistics for {ds} dataset - {self.name_outcome}", fontsize=16, y=1.03) 
        plt.tight_layout(rect=[0, 0, 1, 0.98])
        plt.show()

    def roc_data_model_ds(self,model,ds):
        """
        Creates data needed for ROC plot
        Args:
            model: model name 
            ds: Dataset
        """
        ds_index = self.ds_list.index(ds)
        y_prob = self.model_dict[model][1][ds_index]
        y_actual = self.y_actual[ds_index].map({self.the_other_class:0,self.class_predicted:1})
        fpr, tpr, thresholds = roc_curve(y_actual, y_prob)
        roc_auc = auc(fpr, tpr)
        n = len(fpr)
        return fpr, tpr, roc_auc, n
    
    def all_roc_table(self):
        """
        Appends data from all models and datasets
        """        
        results = pd.DataFrame()
        for ds in self.ds_list:
            temp = pd.DataFrame()
            temp['model'] = ['Baseline'] * 2 
            temp['ds'] = [ds] * 2
            temp['fpr'] = [0,1]
            temp['tpr'] = [0,1]
            results = pd.concat([results, temp], ignore_index=True)
        for m in self.model_list:
            for ds in self.ds_list:
                temp = pd.DataFrame()
                fpr, tpr, roc_auc, n = self.roc_data_model_ds(m,ds)
                temp['model'] = [m] * n 
                temp['ds'] = [ds] * n
                temp['fpr'] = fpr
                temp['tpr'] = tpr
                results = pd.concat([results, temp], ignore_index=True)
        return results
    
    def all_roc_plot(self, graph_size = 4):
        """
        Creates ROC Curve with all models + baseline
        Args:
            graph_size: Adjust total size of graph
        """
        df = self.all_roc_table()
        n_graphs = len(self.ds_list)
        fig, axes = plt.subplots(nrows = 1, ncols = n_graphs, figsize=(n_graphs*graph_size*0.9, graph_size)) 
        axes=axes.flatten()
        palette = sns.color_palette('tab10', len(df['model'].unique()))
        hue_order = df['model'].unique()
        color_map = {model: color for model, color in zip(hue_order, palette)}
        for ax, ds in zip(axes, self.ds_list):
            filtered = df[df['ds']== ds]
            sns.lineplot(data = filtered, x = 'fpr', y = 'tpr', ax=ax, hue = 'model', palette=color_map, legend=None)
            ax.set_title(ds)
        legend_handles = [Patch(color=color, label=model) for model, color in color_map.items()]
        fig.legend(handles=legend_handles, loc= 'center left', ncol=1, title='Model Names', bbox_to_anchor=(1.01, 0.5))
        fig.suptitle(f"Receiver Operating Characteristic - {self.name_outcome}", fontsize=16, y=0.95) 
        plt.tight_layout()
        plt.show()
    
    def show_roc_auc_table(self):
        """"
        Show table with ROC formatted values
        """
        df = self.stat_table_transposed()
        df = df[['model_name'] + [col for col in df.columns if 'roc_auc' in col]]
        return df.style.apply(self.highlight_best, axis=0)

    def roc_plot(self, model, ds):
        """
        Creates Indivual ROC Curve
        Args:
            model: model name 
            ds: Dataset
        """
        fpr, tpr, roc_auc, n = self.roc_data_model_ds(model,ds)
        plt.figure(figsize=(3, 3))
        plt.plot(fpr, tpr, color='darkorange', lw=2)
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0, 1])
        plt.ylim([0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'{model} - {ds}: AUC: {round(roc_auc,3)}')
        plt.show()