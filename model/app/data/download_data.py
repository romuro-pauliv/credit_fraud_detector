# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/data/download_data.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files import configfiles

from pathlib import PosixPath, Path

import zipfile
import requests
import os
# |--------------------------------------------------------------------------------------------------------------------|


class DownloadData(object):
    """
    Download data to training the model
    """
    def __init__(self) -> None:
        """
        Initialize the DownloadData instance.
        """
        self.uri: str                   = configfiles.dot_ini['data']['data:uri']['uri']
        
        self.app_dir        : str       = configfiles.dot_ini['data']['data:dir']['app']
        self.resources_dir  : str       = configfiles.dot_ini['data']['data:dir']['resources']
        
        self.zip_path   : PosixPath     = Path(configfiles.dot_ini['data']['data:path']['zip_path'])
        self.csv_path   : PosixPath     = Path(configfiles.dot_ini['data']['data:path']['csv_path'])
        self.rsrc_path  : PosixPath     = Path(self.app_dir, self.resources_dir)
        
        self.rsrc_files : list[str]     = []
        
        self._check_resources()
        self._get_resources_files()
        
    def get(self) -> None:
        """
        Request data to uri
        """
        self.r: requests.models.Response = requests.get(self.uri)
        
    def save_zip(self) -> None:
        """
        Save zip file in the dir
        """
        with open(self.zip_path, "wb") as file:
            file.write(self.r.content)
    
    def unzip(self) -> None:
        """
        Unzip the zip file
        """
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.csv_path)
    
    def _check_resources(self) -> None:
        """
        Check if the resources dir exists. If not, creates one. 
        """
        if self.resources_dir not in os.listdir(self.app_dir):
            os.mkdir(self.rsrc_path)
    
    def _get_resources_files(self) -> None:
        """
        Get the resources filenames.
        """
        self.rsrc_files: list[str] = os.listdir(self.rsrc_path)
    
    