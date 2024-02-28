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

# # | CSV infos |--------------------------------------------------------------------------------------------------------|
# from data.analysis.csv_info import CSVInfo
# csv_info: CSVInfo = CSVInfo(df)
# csv_info.head()
# csv_info.describe()
# csv_info.null_values()
# csv_info.columns()
# csv_info.frauds_count()
# # |--------------------------------------------------------------------------------------------------------------------|

# # | Distribution graphs |----------------------------------------------------------------------------------------------|
# from data.analysis.graph.time_and_amount_dist import TimeAmountDist
# time_amount_dist: TimeAmountDist = TimeAmountDist(df)
# time_amount_dist.show()
# # |--------------------------------------------------------------------------------------------------------------------|

# # | Scale data |-------------------------------------------------------------------------------------------------------|
# from data.treatment.time_amount_scale import ScaleTimeAndAmount
# df: pdDataframe = ScaleTimeAndAmount(df).scale()
# # |--------------------------------------------------------------------------------------------------------------------|

# # | Split in Training and Test dataframe |-----------------------------------------------------------------------------|
# from data.treatment.split_train_test import SplitTrainTest
# split_train_test: SplitTrainTest = SplitTrainTest(df)
# split_train_test.split()
# # |--------------------------------------------------------------------------------------------------------------------|

# | Random Under Sampling |--------------------------------------------------------------------------------------------|
from data.treatment.random_under_sampling import RandomUnderSampling
random_under_sampling: RandomUnderSampling = RandomUnderSampling(df)
# |--------------------------------------------------------------------------------------------------------------------|

# # | Correlation Graph |------------------------------------------------------------------------------------------------|
# from data.analysis.graph.correlation_matrix_dataframe import CorrelationMatrixGraph
# correlation_matrix_graph: CorrelationMatrixGraph = CorrelationMatrixGraph(df, random_under_sampling.balanced_df)
# correlation_matrix_graph.show()
# # |--------------------------------------------------------------------------------------------------------------------|

# | Boxplot Graph |----------------------------------------------------------------------------------------------------|
from data.analysis.graph.corr_pos_neg_boxplot import CorrBoxPlot
CorrBoxPlot(random_under_sampling.balanced_df).show()
# |--------------------------------------------------------------------------------------------------------------------|

# # | Distribution Graph |-----------------------------------------------------------------------------------------------|
# from data.analysis.graph.all_dist_plots import AllDistPlots
# all_dist_plots: AllDistPlots = AllDistPlots(random_under_sampling.balanced_df)
# all_dist_plots.gen_graph_by_column(
#     ["V2", "V3", "V4", "V6", "V7", "V9", "V10", "V11", "V12", "V14", "V16", "V17", "V18", "V27", "V28"]
# )
# all_dist_plots.gen_graph_by_column(
#     ["Time", "V1", "V5", "V8", "V13", "V15", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26"]
# )
# # |--------------------------------------------------------------------------------------------------------------------|