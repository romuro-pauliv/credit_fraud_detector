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
from theme.romuro import theme_romuro, ROMURO_BLUE

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
    
    def _get_data(self) -> None:
        """
        Get the amount and time values from dataset
        """
        genlog.report("debug", "Convert [Amount, Time] to ndarray")
        self.amount_val : np.ndarray    = self.df[self.clmn_amount].values
        self.time_val   : np.ndarray    = self.df[self.clmn_time].values
        
    def graph_transaction_amount(self) -> None:
        """
        Creates the Transaction Amount graph
        """
        fig, ax = plt.subplots(1, 1)
        
        sns.histplot(x=self.amount_val, kde=True, ax=ax, color=ROMURO_BLUE)
        ax.set_xlim([min(self.amount_val), max(self.amount_val)/200])
        theme_romuro(ax, fig, "amount", "count", "Distribution of Transaction Amount")
        genlog.report(True, "Created TimeAmountDist Transaction Amount Graph")
        
    def graph_transaction_time(self) -> None:
        """
        Creates the Transaction Time graph
        """
        fig, ax = plt.subplots(1, 1)
        
        sns.histplot(self.time_val, ax=ax, kde=True, color=ROMURO_BLUE)
        ax.set_xlim([min(self.time_val), max(self.time_val)])
        theme_romuro(ax, fig, "time", "count", "Distribution of Transaction Time")
        genlog.report(True, "Created TimeAmountDist Transaction Time Graph")
    
    def graph_corr_time_amount(self) -> None:
        """
        Creates the Scatter plot with x: time, y: Amount
        """
        fig, ax = plt.subplots(1, 1)
        sns.jointplot(x=self.time_val, y=self.amount_val,
                      xlim=(min(self.time_val), max(self.time_val)),
                      ylim=(min(self.amount_val), max(self.amount_val)/10),
                      color="b", height=7, ax=ax, s=1)
        genlog.report(True, "Created TimeAmountDist Correlation Time x Amount")
                
    def show(self) -> None:
        """
        Show the Analysis
        """
        self._get_data()
        
        self.graph_transaction_amount()
        self.graph_transaction_time()
        self.graph_corr_time_amount()
        
        plt.show()
        plt.clf()
        genlog.report(True, "quit TimeAmountDist Plot")