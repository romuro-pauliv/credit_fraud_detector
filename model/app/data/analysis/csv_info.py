# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/data/analysis/csv_info.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from log.genlog import genlog

from pandas.core.frame import DataFrame as pdDataframe
from pandas.core.indexes.base import Index as pdIndex
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
    
    def head(self) -> None:
        """
        Print head of csv values
        """
        print(self.df.head())
        genlog.report("debug", ".head()")
    
    def describe(self) -> None:
        """
        Describe the csv values
        """
        print(self.df.describe())
        genlog.report("debug", ".describe()")
    
    def null_values(self) -> None:
        """
        Report amount of null values in dataframe
        """
        null_values: int = self.df.isnull().sum().max()
        if null_values == 0:
            genlog.report(True, f"{null_values} null values in Dataframe")
        else:
            genlog.report(False, f"{null_values} null values in Dataframe")
    
    def columns(self) -> pdIndex:
        """
        Get the columns names
        """
        print(self.df.columns)
        genlog.report("debug", "csv columns")
        return self.df.columns