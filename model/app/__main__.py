from pathlib import PosixPath
import warnings
warnings.filterwarnings("ignore")

from data.download_data import DownloadData
download_data: DownloadData = DownloadData()
csv_path: PosixPath = download_data.download()

from data.read_csv import ReadCSV
read_csv: ReadCSV = ReadCSV(csv_path)

from data.analysis.csv_info import CSVInfo
csv_info: CSVInfo = CSVInfo(read_csv.dataframe)
csv_info.head()
csv_info.describe()
csv_info.null_values()
csv_info.columns()
csv_info.frauds_count()

from data.analysis.graph.time_and_amount_dist import TimeAmountDist
time_amount_dist: TimeAmountDist = TimeAmountDist(read_csv.dataframe)
time_amount_dist.show()