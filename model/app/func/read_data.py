# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                              app/func/read_data.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pathlib            import PosixPath
from pandas.core.frame  import DataFrame as pdDataframe
from data.read_csv      import ReadCSV
# |--------------------------------------------------------------------------------------------------------------------|


def read_data(csv_path: PosixPath) -> pdDataframe:
    read_csv: ReadCSV = ReadCSV(csv_path)
    return read_csv.dataframe