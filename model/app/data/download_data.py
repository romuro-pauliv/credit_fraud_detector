# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/data/download_data.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files import configfiles

from log.genlog import genlog

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
        
        self.zip_name   : str           = configfiles.dot_ini['data']['data:filename']['zip']
        self.csv_name   : str           = configfiles.dot_ini['data']['data:filename']['csv']
        
        self.rsrc_files : list[str]     = []
        
        self._check_resources()
        
    def get(self) -> None:
        """
        Request data to uri
        """
        genlog.report("downloading...", f"{self.rsrc_path}/{self.zip_name}")
        self.r: requests.models.Response = requests.get(self.uri)
        if self.r.status_code == 200:
            genlog.report(True, f"{self.rsrc_path}/{self.zip_name}")
        else:
            genlog.report(False, f"{self.rsrc_path}/{self.zip_name}")
        
    def save_zip(self) -> None:
        """
        Save zip file in the dir
        """
        with open(self.zip_path, "wb") as file:
            file.write(self.r.content)
        genlog.report(True, f"save zip {self.zip_path}")
    
    def unzip(self) -> None:
        """
        Unzip the zip file
        """
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.csv_path)
        genlog.report(True, f"unzip {self.zip_path}")
    
    def _check_resources(self) -> None:
        """
        Check if the resources dir exists. If not, creates one. 
        """
        if self.resources_dir not in os.listdir(self.app_dir):
            os.mkdir(self.rsrc_path)
            genlog.report(True, f"created {self.rsrc_path} dir")
    
    def download(self) -> PosixPath:
        """
        Download and unzip the data
        return:
            PosixPath: The path of the csv file
        """
        rsrc_files: list[str] = os.listdir(self.rsrc_path)
        
        if self.zip_name not in rsrc_files:
            self.get()
            self.save_zip()
            self.unzip()
        else:
            if self.csv_name not in rsrc_files:
                genlog.report(True, f"{self.zip_path} in cache")
                self.unzip()
            else:
                genlog.report(True, "all files in cache")
            
        return Path(self.app_dir, self.resources_dir, self.csv_name)