# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                              app/data/treatment/cutoff_outliers.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy    as np

from config.config_files    import configfiles
from log.genlog             import genlog

from pandas.core.frame  import DataFrame    as pdDataframe
from pandas.core.series import Series       as pdSeries
# |--------------------------------------------------------------------------------------------------------------------|


class CutOffOutliers(object):
    def __init__(self, data: pdDataframe) -> None:
        """
        Initialize the CutOffOutliers
        Args:
            data (pdDataframe): The data in pandas dataframe type
        """
        self.df         : pdDataframe = data
        self.clmn_class : str = configfiles.dot_ini['dataframe']['dataframe:columns']['class']

        self.per25          : int   = 25
        self.per75          : int   = 75
        self.IQR_multiplier : float = 1.5
        
        self.count_df: int = len(self.df)
            
    def _get_series(self, column: str, class_state: int) -> pdSeries:
        """
        Get pandas series based on column name and class state [0, 1]
        """
        return self.df[column].loc[self.df[self.clmn_class] == class_state].values

    def _per25_75(self, pd_series: pdSeries) -> tuple[np.float64]:
        """
        Get quartile 25% and 75%
        """
        return np.percentile(pd_series, self.per25), np.percentile(pd_series, self.per75)
    
    def _IQR(self, per25_75: tuple[np.float64]) -> np.float64:
        """
        Calculates the IQR (InterQuartile Range)
        """
        return per25_75[1] - per25_75[0]

    def _cutoff_threshold_values(self, per25_75: tuple[np.float64], IQR: np.float64) -> tuple[np.float64]:
        """
        Get lower and higher thresholds [lower, higher]
        """
        cutoff: np.float64 = IQR * self.IQR_multiplier
        return per25_75[0] - cutoff, per25_75[1] + cutoff
    
    def thresholds(self, column: str, class_state: int) -> tuple[np.float64]:
        """
        Get the outliers thresholds
        Args:
            column (str): Column from pandas Dataframe to get outliers thresholds
            class_state (int): Class state (0, 1) [no-fraud, fraud]

        Returns:
            tuple[np.float64]: Outliers thresholds [lower, higher]
        """
        series  : pdSeries          = self._get_series(column, class_state)
        per25_75: tuple[np.float64] = self._per25_75(series)
        iqr     : np.float64        = self._IQR(per25_75)
        
        return self._cutoff_threshold_values(per25_75, iqr)

    def df_without_outliers(self, lower: np.float64, higher: np.float64, column: str, class_state: int) -> None:
        """
        Update the self.df with the data without outliers
        Args:
            lower (np.float64): Lower threshold
            higher (np.float64): High threshold
            column (str): Column name to exclude outliers
        """
        self.df: pdDataframe = self.df.drop(
            self.df[(self.df[column] > higher) | (self.df[column] < lower)].index
        )
        genlog.report("debug", f"Cutoff Outliers: [{column} S:{class_state}]")
    
    def cutoff(self, columns: list[str], class_state: int) -> pdDataframe:
        """
        Cutoff the outliers based on:
        data > Q3 + IQR * IQR_multiplier
        data < Q1 - IQR * IQR_multiplier
        Args:
            columns (list[str]): Columns to cutoff outliers
            class_state (int): Class state (0, 1) (no-fraud, fraud)

        Returns:
            pdDataframe: The pandas Dataframe without outliers
        """
        
        for column in columns:
            lower, higher = self.thresholds(column, class_state)
            self.df_without_outliers(lower, higher, column, class_state)
        
        genlog.report(True,
            f"Cutoff Outliers [B: {self.count_df}, A: {len(self.df)}] [Remove: {self.count_df - len(self.df)}]"
        )
        
        return self.df
    