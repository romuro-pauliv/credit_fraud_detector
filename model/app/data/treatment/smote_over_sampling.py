# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                        app/data/treatment/random_under_sampling.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from imblearn.over_sampling import SMOTE

from config.config_files    import configfiles
from log.genlog             import genlog

import pandas as pd

from pandas.core.frame  import DataFrame as pdDataframe
from pandas.core.series import Series as pdSeries

from typing import Callable
# |--------------------------------------------------------------------------------------------------------------------|


class OverSamplingSMOTE(object):
    def __init__(self, data: pdDataframe) -> None:
        """
        Initialize the OverSamplingSMOTE instance.

        Args:
            data (pdDataframe): The unbalaced data
        """
        self.data       : pdDataframe   = data
        self.clmn_class : str           = configfiles.dot_ini['dataframe']['dataframe:columns']['class']

        self._get_x_y()
        
        self._get_x_y()
        self._define_SMOTE_algorithm()
        self._log()
        
    def _get_x_y(self) -> None:
        """
        Get X and Y dataset
        """
        self.X: pdDataframe = self.data.drop(self.clmn_class, axis=1)
        self.Y: pdSeries    = self.data[self.clmn_class]
    
    def _log(self) -> None:
        a: Callable[[pdSeries, int], int] = lambda y, c: y[y==c].shape[0]
        
        genlog.report("debug", f"oversampling: SMOTE Before [0: {a(self.Y, 0)}] [1: {a(self.Y, 1)}]")
        genlog.report("debug", f"oversampling: SMOTE After  [0: {a(self.Y_sm, 0)}] [1: {a(self.Y_sm, 1)}]")
    
    def _define_SMOTE_algorithm(self) -> None:
        """
        Execute the oversampling SMOTE algorithm
        """
        random_state    : int = int(configfiles.dot_ini['treatment']['treatment:oversampling_SMOTE']['random_state'])
        k_neighbors     : int = int(configfiles.dot_ini['treatment']['treatment:oversampling_SMOTE']['k_neighbors'])
        n_jobs          : int = int(configfiles.dot_ini['treatment']['treatment:oversampling_SMOTE']['n_jobs'])
        
        self.sm: SMOTE = SMOTE(random_state=random_state, k_neighbors=k_neighbors, n_jobs=n_jobs)
        self.X_sm, self.Y_sm = self.sm.fit_resample(self.X, self.Y)
    
    def get_resample(self) -> pdDataframe:
        """
        Get the new oversample data
        Returns:
            pdDataframe: The oversample dataframe
        """
        self.X_sm.insert(0, self.clmn_class, self.Y_sm)
        return self.X_sm