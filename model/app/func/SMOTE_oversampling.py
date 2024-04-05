# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                     app/func/SMOTE_oversampling.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pandas.core.frame                  import DataFrame as pdDataframe
from data.treatment.smote_over_sampling import OverSamplingSMOTE
# |--------------------------------------------------------------------------------------------------------------------|


def oversampling(data: pdDataframe) -> pdDataframe:
    return OverSamplingSMOTE(data).get_resample()