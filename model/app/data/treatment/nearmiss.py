# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                     app/data/treatment/nearmiss.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from log.genlog import genlog

from data.treatment.split_train_test import SplitTrainTest
from imblearn.under_sampling import NearMiss

import numpy as np

from pandas.core.frame import DataFrame as pdDataframe
from pandas.core.series import Series as pdSeries
# |--------------------------------------------------------------------------------------------------------------------|


class NearMissAlgorithm(SplitTrainTest):
    def __init__(self, data: pdDataframe) -> None:
        """
        Initialize the NearMiss Algorithm
        """
        super().__init__(data), self.split()
        self.train_data: tuple[pdDataframe, pdSeries] = self.train

        self._near_miss_xy()
        
    def _near_miss_xy(self) -> None:
        """
        Apply the NearMiss instance.
        """
        self.nearmiss_x, self.nearmiss_y = NearMiss().fit_resample(
            X=self.train_data[0].values,
            y=self.train_data[1].values
        )
        genlog.report(True, f"NM | Real data length: {self.train_data[1].shape[0]}L")
        genlog.report(True, f"NM | NearMiss Algorithm: {self.nearmiss_x.shape[0]}L")
        
    