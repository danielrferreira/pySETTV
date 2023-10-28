# This function can help plot multiple count plots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def count_plots(data, columns, drop_hc=True, max_card=20, scale_graph=9, n_cols=3, aspect_ratio=2/3):
    '''Create multiple count plots using a subset of variables specified.
    
    Args:
        data: Input data-frame containing variables we wish to plot.
        columns: Listing of column-names we wish to plot (must be contained within data).
        drop_hc: Drop columns with high-cardinality.
        max_card: If drop_hc=True, max_card control the number of categories threshold to be called High Cardinality.
        scale_graph: Adjust the total size of the graph.
        n_cols: Adjust how many graphs we have on each row.
        aspect_ratio: Adjust the aspect ratio of each individual graph. For squared graphs use 1/1.
    '''
    # Droping High Cardinality
    col_to_use = columns.copy()
    if drop_hc:
        for x in col_to_use:
            card = data[x].nunique()
            if card > max_card:
                col_to_use.remove(x)
                print(f'WARNING: Column {x} removed due to high-cardinality ({card} unique elements)')

    # Adjusting how many rows the grid will have and proper sizes
    n_rows = len(col_to_use)//n_cols+(len(col_to_use)%n_cols>0) 
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(scale_graph, (scale_graph/n_cols)*aspect_ratio*n_rows))

    # Plotting
    fig.suptitle('Countplot for each categorical variable in our data',y=1, size=15)
    if len(col_to_use)==0:
        print('No graphs generated, please check drop_hc or max_card arguments')
    elif len(col_to_use)==1:
        sns.countplot(data=data, x=col_to_use[0], ax=axes)
    else:
        axes=axes.flatten()
        for i,feature in enumerate(col_to_use):
            sns.countplot(data=data, x=feature, ax=axes[i])
        plt.tight_layout()

#%%
# Calling the function
# You can find this table in the Reference part of this repositorie
bat = pd.read_csv('player_batting_enriched.csv')
cat_c = ['team_name','division', 'league', 'avg_220', 'avg_240', 'avg_260',
       'avg_280', 'avg_300', 'hr_10', 'hr_20', 'hr_30', 'hr_40', 'sb_05',
       'sb_10', 'sb_15', 'sb_20']

count_plots(data=bat, columns=cat_c)

# In this case, one column was removed due to high cardinality. If you want to better understand this column you can use the same function tweaking the arguments:
count_plots(data=bat, columns=['team_name'], drop_hc=False, n_cols=1, aspect_ratio=1/4)
