# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/func/classifiers_model.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from argparse_list      import args
from pandas.core.frame  import DataFrame as pdDataframe
from pandas.core.series import Series    as pdSeries
from models.classifiers import ClassifierModels
# |--------------------------------------------------------------------------------------------------------------------|


def classifiers_model(data: pdDataframe, X_test: pdDataframe, Y_test: pdSeries) -> None:
    cm: ClassifierModels = ClassifierModels(data)
    if args.learningcurvegraph == True or args.graphs == True:
        cm.run_brute(True)
        cm.real_test(X_test, Y_test)
        cm.run_optimized(True)
        cm.real_test(X_test, Y_test)
        return None
    cm.run_brute(False)
    cm.real_test(X_test, Y_test)
    cm.run_optimized(False)
    cm.real_test(X_test, Y_test)