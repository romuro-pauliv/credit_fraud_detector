# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/func/classifiers_model.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from argparse_list      import args
from pandas.core.frame  import DataFrame as pdDataframe
from models.classifiers import ClassifierModels
# |--------------------------------------------------------------------------------------------------------------------|


def classifiers_model(data: pdDataframe) -> None:
    cm: ClassifierModels = ClassifierModels(data)
    if args.learningcurvegraph == True or args.graphs == True:
        cm.run_brute(True)
        cm.run_optimized(True)
        return None
    cm.run_brute(False)
    cm.run_optimized(False)