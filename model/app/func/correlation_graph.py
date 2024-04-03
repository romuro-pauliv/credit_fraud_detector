# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/func/correlation_graph.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from argparse_list                      import args
from pandas.core.frame                  import DataFrame as pdDataframe
from graph.correlation_matrix_dataframe import CorrelationMatrixGraph
# |--------------------------------------------------------------------------------------------------------------------|


def correlation_matrix_graph(unbalanced_data: pdDataframe, balanced_data: pdDataframe) -> None:
    if args.corrgraph == True or args.graphs == True:
        cmg: CorrelationMatrixGraph = CorrelationMatrixGraph(unbalanced_data, balanced_data)
        cmg.show()
