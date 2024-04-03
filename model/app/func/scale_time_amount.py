# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/func/scale_time_amount.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pandas.core.frame                  import DataFrame as pdDataframe
from data.treatment.time_amount_scale   import ScaleTimeAndAmount
# |--------------------------------------------------------------------------------------------------------------------|


def scale_time_amount_features(data: pdDataframe) -> pdDataframe:
    return ScaleTimeAndAmount(data).scale()