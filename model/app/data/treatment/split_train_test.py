# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                             app/data/treatment/split_train_test.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold

from config.config_files import configfiles
from log.genlog import genlog

import pandas as pd

from pandas.core.frame import DataFrame as pdDataframe
from pandas.core.series import Series as pdSeries
# |--------------------------------------------------------------------------------------------------------------------|


class SplitTrainTest(object):
    def __init__(self, dataframe: pdDataframe) -> None:
        """
        Initialize the SplitTrainTest instance.
        Args:
            dataframe (pdDataframe): The data type pandas dataframe
        """
        self.df: pdDataframe = dataframe
        
        self.clmn_class: str = configfiles.dot_ini['dataframe']['dataframe:columns']['class']
        
        self.n_splits: int = int(configfiles.dot_ini['treatment']['treatment:stratified_k_fold']['n_splits'])
    
    def _get_x_y(self) -> None:
        """
        Get the X and Y dataframe
        """
        self.X: pdDataframe = self.df.drop(self.clmn_class, axis=1)
        self.Y: pdSeries = self.df[self.clmn_class]
        genlog.report(True, "split TT: get X and Y")
        
    def _stratified_k_fold(self) -> None:
        """
        Provides train/test indices to split data in train/test sets.
        """
        self.sss: StratifiedKFold = StratifiedKFold(n_splits=self.n_splits, random_state=None, shuffle=False)
    
    def _split(self) -> None:
        """
        Creates a train/test dataframe
        """
        for train_index, test_index in self.sss.split(self.X, self.Y):
            self.original_X_train, self.original_X_test = self.X.iloc[train_index], self.X.iloc[test_index]
            self.original_Y_train, self.original_Y_test = self.Y.iloc[train_index], self.Y.iloc[test_index]
            """
            A doubt that be occur: Only the last iteration will be used. The function StratifiedKFold generates
            in each iteration a split train/test indexes in 80%/20%. 
            """
        genlog.report(True, "split TT: Split train/test")
        
    def _ratio_info(self) -> None:
        """
        Print ratio of dataframe to comparing with the original dataframe.
        """
        _, train_count_values = np.unique(self.original_Y_train, return_counts=True)
        _, test_count_values = np.unique(self.original_Y_test, return_counts=True)
        
        genlog.report(True, f"split TT: train ratio: {train_count_values/len(self.original_Y_train)}")
        genlog.report(True, f"split TT: test ratio: {test_count_values/len(self.original_Y_test)}")
    
    def split(self) -> None:
        """
        Split in train/test dataframe
        """
        self._get_x_y()
        self._stratified_k_fold()
        self._split()
        self._ratio_info()
    
    def train(self) -> tuple[pdDataframe, pdSeries, pdDataframe]:
        """
        Return the train dataset.
        Returns:
            tuple[pdDataframe, pdSeries, pdDataframe]: X, Y, full dataframe
        """
        total: pdDataframe = self.original_X_train.copy(True)
        total.insert(0, self.clmn_class, self.original_Y_train)
        return self.original_X_train, self.original_Y_train, total
    
    def test(self) -> tuple[pdDataframe, pdSeries, pdDataframe]:
        """
        Return the test dataset.
        Returns:
            tuple[pdDataframe, pdSeries, pdDataframe]: X, Y, full dataframe
        """
        total: pdDataframe = self.original_X_test.copy(True)
        total.insert(0, self.clmn_class, self.original_Y_test)
        return self.original_X_test, self.original_Y_test, total