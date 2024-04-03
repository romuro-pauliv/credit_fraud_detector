# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                               app/boxplot_graph.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from argparse_list              import args
from pandas.core.frame          import DataFrame as pdDataframe
from graph.corr_pos_neg_boxplot import CorrBoxPlot
# |--------------------------------------------------------------------------------------------------------------------|


def boxplot_graph(data: pdDataframe) -> None:
    if args.boxgraph == True or args.graphs == True:
        cbp: CorrBoxPlot = CorrBoxPlot(data)
        cbp.show()