# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/data/analysis/csv_info.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from log.genlog import genlog

from config.config_files import configfiles

from pandas.core.frame import DataFrame as pdDataframe
from pandas.core.indexes.base import Index as pdIndex
from typing import Callable
# |--------------------------------------------------------------------------------------------------------------------|


class CSVInfo(object):
    """
    See infos from CSV data
    """
    def __init__(self, dataframe: pdDataframe) -> None:
        """
        Initialize the CSVInfo instance.

        Args:
            dataframe (pdDataframe): Dataframe to see the infos
        """
        self.df: pdDataframe = dataframe
        
        self.clmn_class: str = configfiles.dot_ini['dataframe']['dataframe:columns']['class']
    
    def head(self) -> None:
        """
        Print head of csv values
        """
        print(self.df.head())
        genlog.report("debug", "info: .head()")
    
    def describe(self) -> None:
        """
        Describe the csv values
        """
        print(self.df.describe())
        genlog.report("debug", "info: .describe()")
    
    def null_values(self) -> None:
        """
        Report amount of null values in dataframe
        """
        null_values: int = self.df.isnull().sum().max()
        if null_values == 0:
            genlog.report(True, f"info: {null_values} null values in Dataframe")
        else:
            genlog.report(False, f"info: {null_values} null values in Dataframe")
    
    def columns(self) -> pdIndex:
        """
        Get the columns names
        """
        print(self.df.columns)
        genlog.report("debug", "info: csv columns")
        return self.df.columns

    def frauds_count(self) -> None:
        """
        Amount of fraud and no fraud in the dataframe
        """
        count_func: Callable[[int], float] = lambda index : round(
            self.df[self.clmn_class].value_counts()[index]/len(self.df) * 100, 2
        )
        
        genlog.report("debug", f"info: No Frauds {count_func(0)}% of the dataset")
        genlog.report("debug", f"info: Frauds {count_func(1)}% of the dataset")