# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                              app/func/data_info.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from argparse_list      import args
from data.info.csv_info import CSVInfo
from pandas.core.frame  import DataFrame as pdDataframe
# |--------------------------------------------------------------------------------------------------------------------|

def _exec(data: pdDataframe) -> None:
    data_info: CSVInfo = CSVInfo(data)
    data_info.head()
    data_info.describe()
    data_info.null_values()
    data_info.columns()
    data_info.frauds_count()

def data_info(data: pdDataframe) -> None:
    _exec(data) if args.info == True or args.graphs == True else None