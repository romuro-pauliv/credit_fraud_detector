# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                      app/func/time_amount_graph.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from graph.time_and_amount_dist import TimeAmountDist
from pandas.core.frame          import DataFrame as pdDataframe
from argparse_list              import args
# |--------------------------------------------------------------------------------------------------------------------|


def time_amount_graph(data: pdDataframe) -> None:
    if args.time_amount_graph == True or args.graphs == True:
        time_amount_graph: TimeAmountDist = TimeAmountDist(data)
        time_amount_graph.show()