# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                             app/func/dist_graph.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from argparse_list          import args
from pandas.core.frame      import DataFrame as pdDataframe
from graph.all_dist_plots   import AllDistPlots
# |--------------------------------------------------------------------------------------------------------------------|


def dist_graph(data: pdDataframe) -> None:
    if args.distgraph == True or args.graphs == True:
        adp: AllDistPlots = AllDistPlots(data)