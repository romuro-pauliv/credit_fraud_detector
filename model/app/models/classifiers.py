# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/models/classifiers.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files import configfiles

import numpy as np

from sklearn.model_selection import train_test_split

from pandas.core.frame  import DataFrame as pdDataframe
from pandas.core.series import Series as pdSeries
# |--------------------------------------------------------------------------------------------------------------------|


class ClassifierModels(object):
    def __init__(self, data: pdDataframe) -> None:
        """
        Initialize the ClassfierModels instance.
        Args:
            data (pdDataframe): The dataframe in pandas Dataframe
        """
        self.class_clmn: str = configfiles.dot_ini["dataframe"]["dataframe:columns"]["class"]
        
        self.X: pdDataframe = data.drop(self.class_clmn, axis=1)
        self.Y: pdSeries    = data[self.class_clmn]
        
        self.test_size      : float = float(configfiles.dot_ini['classifiers']['database']["train_test_split"])
        self.random_state   : int = int(configfiles.dot_ini['classifiers']['database']['random_state'])

        self._split_train_test()
        
    def _split_train_test(self) -> None:
        """
        Split the X and Y in train a and test.
        """
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.X, self.Y, test_size=0.2, random_state=self.random_state)
        self._convert_train_test2array()
        
    def _convert_train_test2array(self) -> None:
        """
        Convert train and test dataframes to np.ndarray
        """
        self.X_train: np.ndarray = self.X_train.values
        self.X_test : np.ndarray = self.X_test.values
        self.Y_train: np.ndarray = self.Y_train.values
        self.Y_test : np.ndarray = self.Y_test.values
    
    