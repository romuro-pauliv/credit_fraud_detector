# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                               app/argparse_list.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import argparse
# |--------------------------------------------------------------------------------------------------------------------|

parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description="Credit Card Fraud Detection Models"
)

parser.add_argument("--graphs", action="store_true", help="Plot all graphs")
parser.add_argument("--info", action="store_true", help="Dataset informations")

parser.add_argument("--time_amount_graph", action="store_true", help="Time and Amount Distribution Graphs")
parser.add_argument("--corrgraph", action="store_true", help="Features Correlation Graph")
parser.add_argument("--boxgraph", action="store_true", help="Feature Boxplot Graphs")
parser.add_argument("--distgraph", action="store_true", help="Feature Distribution Graph")
parser.add_argument("--learningcurvegraph", action="store_true", help="Learning Curve of classification models")
parser.add_argument("--DRA", action="store_true", help="Dimensionality Reduction Analysis")


args = parser.parse_args()