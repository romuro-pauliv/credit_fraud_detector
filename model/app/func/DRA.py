# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app/func/DRA.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from argparse_list                                          import args
from pandas.core.frame                                      import DataFrame as pdDataframe
from data.analysis.dimensionality_reduction_and_clustering  import Algo
# |--------------------------------------------------------------------------------------------------------------------|


def dimensionality_reduction(data: pdDataframe) -> None:
    if args.DRA == True or args.graphs == True:
        dr: Algo = Algo(data)
        dr.run()
        dr.plot()