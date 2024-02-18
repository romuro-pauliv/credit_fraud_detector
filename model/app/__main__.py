from pathlib import PosixPath

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