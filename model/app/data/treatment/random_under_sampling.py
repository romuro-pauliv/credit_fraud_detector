# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                        app/data/treatment/random_under_sampling.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files import configfiles
from log.genlog import genlog

import pandas as pd

from pandas.core.frame import DataFrame as pdDataframe
# |--------------------------------------------------------------------------------------------------------------------|


class RandomUnderSampling(object):
    def __init__(self, dataframe: pdDataframe) -> None:
        """
        Initialize the RandomUnderSampling instance.
        Args:
            dataframe (pdDataframe): The data in dataframe type
        """
        self.df: pdDataframe = dataframe

        self.clmn_class: str = configfiles.dot_ini['dataframe']['dataframe:columns']['class']
        
        self._shuffle()
        self._split_balanced_fraud()
        self._concat()
        
    def _shuffle(self) -> None:
        """
        Shuffle the data
        """
        self.df: pdDataframe = self.df.sample(frac=1)
        genlog.report(True, "Random Sample [frac=1]")
    
    def _split_balanced_fraud(self) -> None:
        """
        Split the dataframe in fraud/no-fraud balanced
        """
        self.fraud_df   : pdDataframe = self.df.loc[self.df[self.clmn_class] == 1]
        self.no_fraud_df: pdDataframe = self.df.loc[self.df[self.clmn_class] == 0][:len(self.fraud_df)]
        genlog.report(True, f"Split in [fraud: {len(self.fraud_df)}] [no-fraud: {len(self.no_fraud_df)}]")
        
    def _concat(self) -> None:
        """
        Concat and Re-shuffle the new dataframe
        """
        df_concat: pdDataframe = pd.concat([self.fraud_df, self.no_fraud_df])
        self.new_df: pdDataframe = df_concat.sample(frac=1)
        genlog.report(True, "Concat fraud and no-fraud")
        genlog.report(True, "Random Sample [frac=1]")
        
    @property
    def balanced_df(self) -> pdDataframe:
        return self.new_df