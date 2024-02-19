# |--------------------------------------------------------------------------------------------------------------------|
# |                                                            app/data/analysis/graph/correlation_matrix_dataframe.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pandas.core.frame import DataFrame as pdDataframe

import seaborn as sns
import matplotlib.pyplot as plt
# |--------------------------------------------------------------------------------------------------------------------|


class CorrelationMatrixGraph(object):
    """
    Generates a correlation graph to analyze the dataframe
    """
    def __init__(self, unbalanced_dataframe: pdDataframe, balanced_dataframe: pdDataframe) -> None:
        """
        Initialize the CorrelationMatrixGraph
        Args:
            dataframe (pdDataframe): The data in dataframe type
        """
        self.df     : pdDataframe = unbalanced_dataframe
        self.new_df : pdDataframe = balanced_dataframe
    
    def _df_corr(self) -> None:
        fig, ax = plt.subplots(1, 1)
        sns.heatmap(self.df.corr(), cmap="inferno", annot_kws={"size": 10}, ax=ax)
        ax.set_title("Unbalanced Correlation Matrix", fontsize=14)
    
    def _new_df_corr(self) -> None:
        fig, ax = plt.subplots(1, 1)
        sns.heatmap(self.new_df.corr(), cmap="inferno", annot_kws={"size": 10}, ax=ax)
        ax.set_title("Balanced Correlation Matrix", fontsize=14)
    
    def show(self) -> None:
        self._df_corr()
        self._new_df_corr()
        plt.show()
        plt.clf()