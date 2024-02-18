# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                    app/data/analysis/graph/time_and_amount_dist.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from log.genlog import genlog
from config.config_files import configfiles

from pandas.core.frame import DataFrame as pdDataframe
# |--------------------------------------------------------------------------------------------------------------------|


class TimeAmountDist(object):
    def __init__(self, dataframe: pdDataframe) -> None:
        """
        Initialize the TimeAmountDist instance.
        Args:
            dataframe (pdDataframe): The csv data in Dataframe type.
        """
        self.df: pdDataframe = dataframe
        
        self.clmn_amount   : str = configfiles.dot_ini['dataframe']['dataframe:columns']['amount']
        self.clmn_time     : str = configfiles.dot_ini['dataframe']['dataframe:columns']['time']
    
    def _create_fig(self) -> None:
        """
        Creates a fig with matplotlib
        """
        self.fig, self.ax = plt.subplots(1, 2, figsize=(18, 4))
        genlog.report(True, "Created TimeAmountDist plt fig")
        
    def _get_data(self) -> None:
        """
        Get the amount and time values from dataset
        """
        self.amount_val : np.ndarray    = self.df[self.clmn_amount].values
        self.time_val   : np.ndarray    = self.df[self.clmn_time].values
    
    def graph_transaction_amount(self) -> None:
        """
        Creates the Transaction Amount graph
        """
        sns.distplot(self.amount_val, ax=self.ax[0], color="r")
        self.ax[0].set_title('Distribution of Transaction Amount', fontsize=14)
        self.ax[0].set_xlim([min(self.amount_val), max(self.amount_val)])
        genlog.report(True, "Created TimeAmountDist Transaction Amount Graph")
        
    def graph_transaction_time(self) -> None:
        """
        Creates the Transaction Time graph
        """
        sns.distplot(self.time_val, ax=self.ax[1], color='b')
        self.ax[1].set_title("Distribution of Transaction Time", fontsize=14)
        self.ax[1].set_xlim([min(self.time_val), max(self.time_val)])
        genlog.report(True, "Created TimeAmountDist Transaction Time Graph")
    
    def show(self) -> None:
        """
        Show the Analysis
        """
        self._create_fig()
        self._get_data()
        
        self.graph_transaction_amount()
        self.graph_transaction_time()
        
        plt.show()
        plt.clf()
        genlog.report(True, "quit TimeAmountDist Plot")