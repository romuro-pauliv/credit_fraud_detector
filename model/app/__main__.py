# from data.download_data import DownloadData

# DownloadData().get()

from config.config_files import ConfigFiles

config_files: ConfigFiles = ConfigFiles()

print(config_files.dot_ini['data']['data:uri']['uri'])