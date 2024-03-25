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
scaled_df: pdDataframe = ScaleTimeAndAmount(df).scale()
# |--------------------------------------------------------------------------------------------------------------------|

# | Split in Training and Test dataframe |-----------------------------------------------------------------------------|
from data.treatment.split_train_test import SplitTrainTest
split_train_test: SplitTrainTest = SplitTrainTest(scaled_df)
split_train_test.split()
# |--------------------------------------------------------------------------------------------------------------------|

# | Random Under Sampling |--------------------------------------------------------------------------------------------|
from data.treatment.random_under_sampling import RandomUnderSampling
random_under_sampling: RandomUnderSampling = RandomUnderSampling(scaled_df)
scaled_and_balanced_df: pdDataframe = random_under_sampling.balanced_df
# |--------------------------------------------------------------------------------------------------------------------|

# | Correlation Graph |------------------------------------------------------------------------------------------------|
from data.analysis.graph.correlation_matrix_dataframe import CorrelationMatrixGraph
correlation_matrix_graph: CorrelationMatrixGraph = CorrelationMatrixGraph(scaled_df, scaled_and_balanced_df)
correlation_matrix_graph.show()
# |--------------------------------------------------------------------------------------------------------------------|

# | Boxplot Graph |----------------------------------------------------------------------------------------------------|
from data.analysis.graph.corr_pos_neg_boxplot import CorrBoxPlot
CorrBoxPlot(scaled_and_balanced_df).show()
# |--------------------------------------------------------------------------------------------------------------------|

# | Cutoff Ouliers |---------------------------------------------------------------------------------------------------|
from data.treatment.cutoff_outliers import CutOffOutliers
cutoff_outliers: CutOffOutliers = CutOffOutliers(scaled_and_balanced_df)
scaled_and_balaced_df_without_outliers: pdDataframe = cutoff_outliers.cutoff(["V10", "V14", "V12"], 1)
# |--------------------------------------------------------------------------------------------------------------------|

# | Distribution Graph |-----------------------------------------------------------------------------------------------|
from data.analysis.graph.all_dist_plots import AllDistPlots
all_dist_plots: AllDistPlots = AllDistPlots(scaled_and_balaced_df_without_outliers)
# |--------------------------------------------------------------------------------------------------------------------|

# | Dimensionality Reduction |-----------------------------------------------------------------------------------------|
from data.analysis.dimensionality_reduction_and_clustering import Algo
DR_algo: Algo = Algo(scaled_and_balaced_df_without_outliers)
DR_algo.run()
DR_algo.plot()
# |--------------------------------------------------------------------------------------------------------------------|