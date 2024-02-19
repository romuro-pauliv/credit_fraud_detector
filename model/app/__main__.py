from pandas.core.frame import DataFrame as pdDataframe
from pathlib import PosixPath

import warnings
warnings.filterwarnings("ignore")

# | Download the data |------------------------------------------------------------------------------------------------|
from data.download_data import DownloadData
download_data: DownloadData = DownloadData()
csv_path: PosixPath = download_data.download()
# |--------------------------------------------------------------------------------------------------------------------|

# | Read the csv with pandas |-----------------------------------------------------------------------------------------|
from data.read_csv import ReadCSV
read_csv: ReadCSV = ReadCSV(csv_path)
df: pdDataframe = read_csv.dataframe
# |--------------------------------------------------------------------------------------------------------------------|

# | CSV infos |--------------------------------------------------------------------------------------------------------|
from data.analysis.csv_info import CSVInfo
csv_info: CSVInfo = CSVInfo(df)
csv_info.head()
csv_info.describe()
csv_info.null_values()
csv_info.columns()
csv_info.frauds_count()
# |--------------------------------------------------------------------------------------------------------------------|

# | Distribution graphs |----------------------------------------------------------------------------------------------|
from data.analysis.graph.time_and_amount_dist import TimeAmountDist
time_amount_dist: TimeAmountDist = TimeAmountDist(df)
time_amount_dist.show()
# |--------------------------------------------------------------------------------------------------------------------|

# | Scale data |-------------------------------------------------------------------------------------------------------|
from data.treatment.time_amount_scale import ScaleTimeAndAmount
df: pdDataframe = ScaleTimeAndAmount(df).scale()
# |--------------------------------------------------------------------------------------------------------------------|