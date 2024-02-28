# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                            app/data/treatment/time_amount_scale.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import numpy as np
from sklearn.preprocessing import RobustScaler

from config.config_files import configfiles
from log.genlog import genlog

from pandas.core.frame import DataFrame as pdDataframe
# |--------------------------------------------------------------------------------------------------------------------|


class ScaleTimeAndAmount(RobustScaler):
    def __init__(self, dataframe: pdDataframe) -> None:
        """
        Initialize the ScaleTimeAndAmount instance.
        """
        self.rob_scaler: RobustScaler = RobustScaler()
        self.df: pdDataframe = dataframe
        
        self.clmn_time   : str = configfiles.dot_ini['dataframe']['dataframe:columns']['amount']
        self.clmn_amount : str = configfiles.dot_ini['dataframe']['dataframe:columns']['time']
        
    def _fit_transform(self) -> None:
        """
        Fit scale of the Time and Amount column
        """
        self.scaled_time  : np.ndarray  = self.rob_scaler.fit_transform(self.df[self.clmn_time].values.reshape(-1, 1))
        self.scaled_amount: np.ndarray  = self.rob_scaler.fit_transform(self.df[self.clmn_amount].values.reshape(-1, 1))
        genlog.report(True, f"Scaled ({self.clmn_time}, {self.clmn_amount})")
        
    def _drop_old_columns(self) -> None:
        """
        Drop the no-scaled Time and Amount from dataframe
        """
        self.df.drop([self.clmn_amount, self.clmn_time], axis=1, inplace=True)
        genlog.report(True, f"Drop no-scale ({self.clmn_time}, {self.clmn_amount}) from dataframe")
        
    def _insert_scaled_in_df(self) -> None:
        """
        Insert the scaled Time and Amount in the dataframe
        """
        self.df.insert(0, self.clmn_time, self.scaled_time)
        self.df.insert(1, self.clmn_amount, self.scaled_amount)
        genlog.report(True, f"Insert scaled ({self.clmn_time}, {self.clmn_amount}) in the dataframe")
        
    def scale(self) -> pdDataframe:
        """
        Scale and return the Dataframe with columns scaled
        return:
            Dataframe: The dataframe scaled
        """
        self._fit_transform()
        self._drop_old_columns()
        self._insert_scaled_in_df()
        
        print(self.df.head())
        
        return self.df