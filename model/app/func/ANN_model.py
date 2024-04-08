# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                              app/func/ANN_model.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pandas.core.frame  import DataFrame as pdDataframe
from pandas.core.series import Series as pdSeries
from models.ANN         import ANNModel
# |--------------------------------------------------------------------------------------------------------------------|


def ANN_model(data: pdDataframe, X_test: pdDataframe, Y_test: pdSeries) -> None:
    ANNModel(data).real_test(X_test, Y_test)