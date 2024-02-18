# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                               app/data/read_csv.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from log.genlog import genlog

from pathlib import PosixPath
import pandas as pd

from pandas.core.frame import DataFrame as pdDataframe
# |--------------------------------------------------------------------------------------------------------------------|


class ReadCSV(object):
    """
    Read CSV and print the infos
    """
    def __init__(self, path_: PosixPath) -> None:
        """
        Initialize the ReadCSV instance.
        """
        self.path_: PosixPath = path_
        self._read()
        
    def _read(self) -> None:
        """
        Read CSV with pandas
        """
        genlog.report("reading...", f"read {self.path_}")
        self.df: pdDataframe = pd.read_csv(self.path_)
        genlog.report(True, f"read {self.path_}")
    
    @property
    def dataframe(self) -> pdDataframe:
        return self.df 
    

