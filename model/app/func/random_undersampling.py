# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                   app/func/random_undersampling.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pandas.core.frame                      import DataFrame as pdDataframe
from data.treatment.random_under_sampling   import RandomUnderSampling
# |--------------------------------------------------------------------------------------------------------------------|


def random_undersampling(data: pdDataframe) -> pdDataframe:
    rus: RandomUnderSampling = RandomUnderSampling(data)
    return rus.balanced_df()