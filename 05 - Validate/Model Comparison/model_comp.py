
from sklearn.metrics import confusion_matrix

class model_comparison:
    def __init__(self, outcome, name_outcome):
        """
        Initialize the Model Comparison

        Args:
            outcome: actual outcomes, usually from test datasets
            name_outcome: What we are trying to predict
        """
        self.outcome = outcome
        self.name_outcome = name_outcome

    def stats_v1(self, pred):
        cm = confusion_matrix(self.outcome, pred)
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
            print(f'{self.name_outcome} - {metric_name}: {round(i,3)}')