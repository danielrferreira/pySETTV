# This function splits the data into Train/Validation/Test

def data_partition(data, train_ratio=0.5, val_ratio=0.5, test_ratio=0, seed=420):
    '''This function splits the data into train, validation and test, it return 2 data frames if test_ratio=0 or 3 data frames if test_ratio>0'''
    data_shuffle = data.sample(frac=1, random_state=seed).reset_index(drop=True)
    if test_ratio==0:
        train_size = int(train_ratio * len(data))
        val_size = len(data) - train_size
        return data_shuffle[:train_size],data_shuffle[train_size:train_size + val_size]
    else:
        train_size = int(train_ratio * len(data))
        val_size = int(val_ratio * len(data))
        test_size = len(data) - train_size - val_size
        return data_shuffle[:train_size], data_shuffle[train_size:train_size + val_size], data_shuffle[train_size + val_size:]

# Examples
import pandas as pd
baseball = pd.read_csv('baseball_stats_batting_2020_2023.csv')
bb_train, bb_val = data_partition(baseball) # For 50/50 Train/Validation
bb_train, bb_val = data_partition(baseball,seed=12345) # For 50/50 Train/Validation, different seed
bb_train, bb_val = data_partition(baseball,train_ratio=0.7,val_ratio=0.3) #For 70/30 Train/Validation
bb_train, bb_val, bb_test = data_partition(baseball,train_ratio=0.7,val_ratio=0.15,test_ratio=0.15) #0.7/0.15/0.15 T/V/T

