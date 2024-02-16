# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/data/download_data.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import requests
# |--------------------------------------------------------------------------------------------------------------------|


class DownloadData(object):
    """
    Download data to training the model
    """
    def __init__(self) -> None:
        """
        Initialize the DownloadData instance.
        """
        self.uri: str = "https://github.com/AakashKumarNain/CaptchaCracker/raw/master/captcha_images_v2.zip"
    
    def get(self) -> None:
        """
        Request data to uri
        """
        self.r: requests.models.Response = requests.get(self.uri)
        
        