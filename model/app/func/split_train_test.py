# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                       app/func/split_train_test.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pandas.core.frame                  import DataFrame as pdDataframe
from data.treatment.split_train_test    import SplitTrainTest
# |--------------------------------------------------------------------------------------------------------------------|


def split_train_test(data: pdDataframe) -> SplitTrainTest:
    split_traintest: SplitTrainTest = SplitTrainTest(data)
    split_traintest.split()
    return split_traintest