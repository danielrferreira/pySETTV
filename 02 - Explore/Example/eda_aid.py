import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy.stats import chi2_contingency
import numpy as np
from sklearn.ensemble import RandomForestClassifier

sns.set_theme(style="darkgrid", palette="deep")

class eda_aid:
    def __init__(self, df: pd.DataFrame):
        """ 
        Initialize the problem

        Args:
            df: DataFrame to be analyzed
        """
        self.df = df
        self.n_rows = self.df.shape[0]
        self.n_cols = self.df.shape[1]
        self.numeric_list = list(self.df.select_dtypes(include=['number']).columns)
        self.categorical_list = list(self.df.select_dtypes(include=['object']).columns)
        self.boolean_list = list(self.df.select_dtypes(include=['bool']).columns)
        self.datetime_list = list(self.df.select_dtypes(include=['datetime64[ns]', 'datetime64[ns, UTC]']).columns)
        self.missing_list = self.df.columns[self.df.isna().any()].tolist()
        self.non_missing_list = list(set(self.df.columns) - set(self.missing_list))
        print(f"EDA Aid initialized with {self.n_rows} rows and {self.n_cols} columns:\n - Numeric: {len(self.numeric_list)}\n - Object: {len(self.categorical_list)}\n - Boolean: {len(self.boolean_list)}\n - Datetime: {len(self.datetime_list)}")

    def missingness(self) -> pd.DataFrame:
        """
        Calculate the count and proportion of missing values in each column of the DataFrame.

        Returns:
            pd.DataFrame: A DataFrame with the count and proportion of missing values for each column.
        """
        missing_count = self.df.isna().sum()
        missings = pd.DataFrame({
            'missing_count': missing_count,
            'missing_proportions': round(missing_count / len(self.df),3)
        })
        return missings
    
    def columns_df(self) -> pd.DataFrame:
        """
        Create a DataFrame with column names, their types (numeric or object), and missing values information.

        Returns:
            pd.DataFrame: DataFrame with columns - 'name', 'type', 'count', and 'proportions'.
        """
        columns = self.numeric_list + self.categorical_list + self.boolean_list + self.datetime_list
        types = ['numeric'] * len(self.numeric_list) + ['object'] * len(self.categorical_list) + ['boolean'] * len(self.boolean_list) + ['datetime'] * len(self.datetime_list)
        df_columns = pd.DataFrame({'name': columns, 'type': types})
        missings = self.missingness().reset_index().rename(columns={'index': 'name'})
        unique_values = self.df[columns].nunique().reset_index().rename(columns={'index': 'name', 0: 'unique_values'})
        merged_df = pd.merge(df_columns, missings, on='name', how='left')
        merged_df['non_missing_count'] = self.n_rows - merged_df['missing_count']
        merged_df = pd.merge(merged_df, unique_values, on='name', how='left')
        merged_df.set_index('name', inplace=True)
        return merged_df
        
    def missingness_chi_whitin(self) -> None:
        """
        This function shows the p-value of chi-square test of all columns with missing value. 0 means percfect association. 
        Larger values means independence of missingness.
        """
        p_values = pd.DataFrame(index = self.missing_list, columns=self.missing_list)
        for col1 in self.missing_list:
            for col2 in self.missing_list:
                if col1 == col2:
                    p_values.loc[col1, col2] = 0
                else:
                    contingency_table = pd.crosstab(self.df[col1].isna(), self.df[col2].isna())
                    _, p, _, _ = chi2_contingency(contingency_table)
                    p_values.loc[col1, col2] = p
        plt.figure(figsize=(8, 6))
        sns.heatmap(round(p_values.astype(float),5), annot=True, cmap='coolwarm_r', cbar_kws={'label': 'p-value'}, annot_kws={"size": 10})
        plt.title(f'Chi-Square Test p-value for Missing Values Associations')
        plt.show()

    def random_forest_importance(self, outcome, inputs, ax=None) -> plt.Axes:
        """ 
        Creates a bar plot of variable importance to predict an outcome.
        
        Args:
        outcome (pd.Series): Outcome variable (binary).
        inputs (list): List of input column names to be used.
        ax (plt.Axes, optional): Axis to draw the plot. Creates a new one if not provided.
        
        Returns:
        plt.Axes: Axis object containing the bar plot.
        """
        X = self.df[inputs]
        X = pd.get_dummies(X, drop_first=True)
        rank_model = RandomForestClassifier(n_estimators=100, random_state=42)
        rank_model.fit(X, outcome)
        feature_importances = pd.Series(rank_model.feature_importances_, index=rank_model.feature_names_in_)
        feature_importances = feature_importances.sort_values()
        if ax is None:
            fig, ax = plt.subplots(figsize=(8, len(feature_importances) * 0.3))
        ax.barh(feature_importances.index, feature_importances)
        ax.set_title("Feature Importance")
        ax.set_xlabel("Importance Score")
        ax.set_ylabel("Features")
        return ax
    
    def missingness_association(self, inputs=None, max_c=50) -> None:
        """ 
        Get all bar plots of variable importance to predict missingness.
        
        Args:
            inputs (list): List of input column names to be used. If None, all non missing numeric, boolean or object with low cardinality will be used.
            max_c: maximun value of unique categories in object variable
        
        """
        if inputs is None:
            inputs = [
                var for var in self.non_missing_list
                if pd.api.types.is_numeric_dtype(self.df[var])
                or (pd.api.types.is_object_dtype(self.df[var]) and self.df[var].nunique() < max_c)
                or pd.api.types.is_bool_dtype(self.df[var])
            ]
        n_graphs = len(self.missing_list)
        n_rows = math.ceil(n_graphs / 2)
        fig, axes = plt.subplots(nrows=n_rows, ncols=2, figsize=(12, n_rows * 6.6))
        axes = axes.flatten()
        fig.suptitle('Missigness Association', fontsize=20, y=1.0025)
        for var, ax in zip(self.missing_list, axes):
            outcome = self.df[var].isna()
            self.random_forest_importance(outcome, inputs, ax=ax)
            ax.set_title(var)
        for ax in axes[n_graphs:]:
            ax.axis("off")
        plt.tight_layout()
        plt.show()

    def eda_quant_uni(self, quant_var=None, type = 'hist') -> None:
        """ 
        This function plots the univariate analysis of the quantitative variables

        Args:
            quant_var: list of quantitative variables
            type: type of plot to be used. Options are 'hist', 'box' or 'violin'
            
        """ 
        if quant_var is None:
            quant_var = self.numeric_list
        if len(quant_var)==0:
            return 'No quantitative variables'
        n_graphs = len(quant_var)
        n_row = math.ceil(n_graphs / 3)
        fig, axes = plt.subplots(nrows = n_row, ncols = 3, figsize=(10,n_row*3)) 
        axes=axes.flatten()
        title_text = 'Univariate Analysis of Quantitative Variables'
        if n_graphs > 2:
            fig.suptitle(title_text)
        else:
            fig.suptitle(title_text, x=0.0, ha='left')
        for v, ax in zip(quant_var, axes):
            if type == 'hist':
                sns.histplot(data=self.df, x = v, ax = ax, kde=True)
            elif type == 'box':
                sns.boxplot(data=self.df, y = v, ax = ax)
            elif type == 'violin':
                sns.violinplot(data=self.df, x = v, ax = ax)
            ax.set_title(v)
        for ax in axes[n_graphs:]:
            ax.set_visible(False)
        plt.tight_layout()
        plt.show()

    def eda_cat_uni(self, cat_var=None, drop_hc=True, max_card=20) -> None:
        """ 
        This function plots the univariate analysis of the categorical variables

        Args:
            cat_var: list of categorical variables
            drop_hc: Drop columns with high-cardinality.
            max_card: If drop_hc=True, max_card control the number of categories threshold to be called High Cardinality.
        """ 
        if cat_var is None:
            cat_var = self.categorical_list + self.boolean_list
        if len(cat_var)==0:
            return 'No categorical variables'
        final_list = cat_var.copy()
        if drop_hc:
            for x in cat_var:
                card = self.df[x].nunique()
                if card > max_card:
                    final_list.remove(x)
                    print(f'WARNING: Column {x} removed due to high-cardinality ({card} unique elements)')
        n_graphs = len(final_list)
        n_row = math.ceil(n_graphs / 2)
        fig, axes = plt.subplots(nrows = n_row, ncols = 2, figsize=(12,n_row*5))
        title_text = 'Univariate Analysis of Categorical Variables'
        if n_graphs > 2:
            fig.suptitle(title_text)
        else:
            fig.suptitle(title_text, x=0.0, ha='left')
        if len(final_list)==0:
            print('No graphs generated, please check drop_hc or max_card arguments')
        else:
            axes=axes.flatten()
            for v, ax in zip(final_list, axes):
                sns.countplot(data = self.df, x = v, ax = ax)
            for ax in axes[:n_graphs]:
                ax.tick_params(axis='x', rotation=45)
                ax.set_xticks(ax.get_xticks())
                ax.set_xticklabels(ax.get_xticklabels(), ha='right')
            for ax in axes[n_graphs:]:
                ax.set_visible(False)
            plt.tight_layout()
            plt.show()

    def eda_date_uni(self, date_var=None) -> None:
        """ 
        This function plots the univariate analysis of the datetime variables

        Args:
            date_var: list of categorical variables
        """ 
        if date_var is None:
            date_var = self.datetime_list
        if len(date_var)==0:
            return 'No date variables'
        n_graphs = len(date_var)
        n_row = math.ceil(n_graphs / 2)
        fig, axes = plt.subplots(nrows = n_row, ncols = 2, figsize=(12,n_row*4))
        title_text = 'Univariate Analysis of Datetime Variables'
        if n_graphs > 2:
            fig.suptitle(title_text)
        else:
            fig.suptitle(title_text, x=0.0, ha='left')
        axes=axes.flatten()
        for v, ax in zip(date_var, axes):
            sns.histplot(data=self.df, x = v, ax = ax)
        for ax in axes[:n_graphs]:
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:%M'))
            ax.tick_params(axis='x', rotation=45)
            ax.set_xticks(ax.get_xticks())
            ax.set_xticklabels(ax.get_xticklabels(), ha='right')
        for ax in axes[n_graphs:]:
            ax.set_visible(False)
        plt.tight_layout()
        plt.show()
    
    def eda_cat_vs_quant_bi(self, outcome, x_columns = None, type = 'kde') -> None:
        '''Create multiple plots using a subset of variables specified.
        
        Args:
            outcome: Categorical variable that we will use as hue.
            x_columns: Listing of column-names we wish to plot against outcome.
            type: type of graph (kde, hist or violin)
        '''
        if x_columns is None:
            x_columns = self.numeric_list
        n_graphs = len(x_columns)
        n_row = math.ceil(n_graphs / 2)
        fig, axes = plt.subplots(nrows = n_row, ncols = 2, figsize=(12,n_row*5))
        axes=axes.flatten()
        title_text = 'Bivariate Analysis - Categorical vs Quantitative'
        if n_graphs > 2:
            fig.suptitle(title_text, y=1.01)
        else:
            fig.suptitle(title_text, x=0.0, ha='left', y=1.01)
        for v, ax in zip(x_columns, axes):
            if type == 'hist':
                sns.histplot(data=self.df, x = v, hue = outcome, ax = ax, kde=True, common_norm=False)
            elif type == 'violin':
                sns.violinplot(data=self.df, y = v, hue = outcome, ax = ax)
            elif type == 'kde':
                sns.kdeplot(data=self.df, x = v, hue = outcome, ax = ax, common_norm=False)
            ax.set_title(v)
        for ax in axes[n_graphs:]:
            ax.set_visible(False)
        plt.tight_layout()
        plt.show()
    
    def eda_cat_vs_cat_bi(self, outcome, x_columns = None, drop_hc=True, max_card=20) -> None:
        '''Create multiple plots using a subset of variables specified.
        
        Args:
            outcome: Categorical variable that we will use as hue.
            x_columns: Listing of column-names we wish to plot against outcome.
            drop_hc: Drop columns with high-cardinality.
            max_card: If drop_hc=True, max_card control the number of categories threshold to be called High Cardinality.
        '''
        if x_columns is None:
            x_columns = self.categorical_list + self.boolean_list
        final_list = x_columns.copy()
        if drop_hc:
            for x in x_columns:
                card = self.df[x].nunique()
                if card > max_card:
                    final_list.remove(x)
                    print(f'WARNING: Column {x} removed due to high-cardinality ({card} unique elements)')
        n_graphs = len(final_list)
        n_row = math.ceil(n_graphs / 2)
        fig, axes = plt.subplots(nrows = n_row, ncols = 2, figsize=(12,n_row*5))
        axes=axes.flatten()
        title_text = 'Bivariate Analysis - Categorical vs Categorical'
        if n_graphs > 2:
            fig.suptitle(title_text, y=1.01)
        else:
            fig.suptitle(title_text, x=0.0, ha='left', y=1.01)
        for v, ax in zip(final_list, axes):
            sns.countplot(data = self.df, x = v, hue = outcome, ax = ax)
            ax.set_title(v)
        for ax in axes[n_graphs:]:
            ax.set_visible(False)
        plt.tight_layout()
        plt.show()
        
    def cat_bivariate(self, col1, col2) -> None:
        '''Bivariate Analysis of two list of categorical columns
        
        Args:
            data: Data Frame
            col1: List of input categorical columns
            col2: List of outcome variables, should be low cardinality
        '''
        data = self.df
        for i in col1:
            for j in col2:
                cross_tab = pd.crosstab(data[i], data[j])
                proportions = round((cross_tab[cross_tab.columns[1]]/cross_tab.sum(axis=1))*100,2)
                chi2, p = chi2_contingency(cross_tab)[0:2]
                print(f'{i} vs {j}')
                print(f'Chi-squared: {round(chi2,2)}')
                if p<0.0001:
                    print('p-value: <0.0001')
                else:
                    print(f'p-value: {round(p,4)}')
                fig, axes = plt.subplots(1, 2, figsize=(10, 4))
                cross_tab.plot(kind='bar', stacked=False,width=0.9, ax=axes[0])
                d = proportions.plot(kind = 'bar',ax=axes[1])
                d.bar_label(d.containers[0])
                plt.title(f'Proportion of {j}={cross_tab.columns[1]} vs {i}')
                plt.show()
    def ln_analysis(self, outcome, x_columns = None, bins = 10, rem_ol = False, thres_1 = 0.05, thres_2 = 0.95):
        '''
        This function helps understand if polynomial terms and/or transformations are needed in a logistic regression. It calculates ln(p/(1-p)) of each bin of numerical columns.
        It also plot the ranges used, and a kernel distribution to help decide which transformation or polynomial term would help.
        If the relationship looks like linear, no need of polynomial term.
        Args:
            outcome: Categorical variable that we will use to calculate ln(p/(1-p)).
            x_columns: Listing of column-names we wish to plot against outcome.
            bins: How many bins we will use to cut the numerical x column
            rem_ol: Remove anything lower than thres_1 percentile or higher than thres_2 percentile
            thres_1: Lower Percentile 
            thres_2: Higher Percentile 
        '''
        if x_columns == None:
            x_columns = [x for x in self.numeric_list if x in self.non_missing_list and x != outcome]
        for x in x_columns:
            print('-'*100)
            print(f'{outcome} vs {x} -> rem_ol={rem_ol}')
            print('-'*100)
            data_clean = self.df[[outcome,x]]
            if rem_ol:
                lim_1 = data_clean[x].quantile([thres_1]).iloc[0]
                lim_2 = data_clean[x].quantile([thres_2]).iloc[0]
                df = data_clean[(data_clean[x]>lim_1) & (data_clean[x]<lim_2)]   
            else:
                df = data_clean
            x_cat = pd.cut(df[x],bins=bins,retbins=True)
            p = df.groupby(x_cat[0], observed=False)[outcome].sum()/df.groupby(x_cat[0], observed=False)[outcome].count()
            all_indexes = range(len(p))
            original_indexes = p.index
            p.index = all_indexes
            p = pd.Series(p[(p.values>0) & (p.values<1)], index=p.index) 
            log_odd = np.log(p/(1-p))
            fig, axes = plt.subplots(1, 2, figsize=(10, 4))
            g = log_odd.plot(marker='o', label='Values',ax=axes[0])
            missing_indexes = log_odd.index[log_odd.isna()]
            g.scatter(missing_indexes, log_odd[log_odd.isna()])
            g.set_xticks(all_indexes)
            sns.kdeplot(data=data_clean, x=x, ax=axes[1])
            axes[0].set_title(f'ln(p/(1-p)) of {outcome} vs {bins} {x} ranges')
            axes[1].set_title(f'{x} kernel distribution')
            plt.tight_layout()
            for i, int in enumerate(original_indexes):
                print(f'{i} = {original_indexes[i]}')
            plt.show()
