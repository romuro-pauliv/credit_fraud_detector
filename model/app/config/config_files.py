# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/config/config_files.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pathlib import Path, PosixPath
import configparser

import os
# |--------------------------------------------------------------------------------------------------------------------|


class ConfigFiles(object):
    """
    Read and distribute the .ini files in py instance.
    """
    def __init__(self) -> None:
        """
        Initialize the ConfigFiles instance.
        """
        self.config_path    : PosixPath = Path("app/config")
        self.ini_ext        : str       = "ini"
    
    def _get_ini_files_path(self) -> None:
        os.listdir()