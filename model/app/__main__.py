from pandas.core.frame import DataFrame as pdDataframe
from pathlib import PosixPath

from argparse_list import args

import warnings
warnings.filterwarnings("ignore")

from func.download_data import download_data
from func.read_data     import read_data

csv_path: PosixPath     = download_data()
df      : pdDataframe   = read_data(csv_path)


# | CSV infos |--------------------------------------------------------------------------------------------------------|
if args.info == True or args.graphs == True:
    from data.info.csv_info import CSVInfo
    csv_info: CSVInfo = CSVInfo(df)
    csv_info.head()
    csv_info.describe()
    csv_info.null_values()
    csv_info.columns()
    csv_info.frauds_count()
# |--------------------------------------------------------------------------------------------------------------------|

# | Distribution graphs |----------------------------------------------------------------------------------------------|
if args.time_amount_graph == True or args.graphs == True:
    from graph.time_and_amount_dist import TimeAmountDist
    time_amount_dist: TimeAmountDist = TimeAmountDist(df)
    time_amount_dist.show()
# |--------------------------------------------------------------------------------------------------------------------|

# | Scale data |-------------------------------------------------------------------------------------------------------|
# from data.treatment.time_amount_scale import ScaleTimeAndAmount
# scaled_df: pdDataframe = ScaleTimeAndAmount(df).scale()
# |--------------------------------------------------------------------------------------------------------------------|

# | Split in Training and Test dataframe |-----------------------------------------------------------------------------|
# from data.treatment.split_train_test import SplitTrainTest
# split_train_test: SplitTrainTest = SplitTrainTest(scaled_df)
# split_train_test.split()
# |--------------------------------------------------------------------------------------------------------------------|

# | Random Under Sampling |--------------------------------------------------------------------------------------------|
# from data.treatment.random_under_sampling import RandomUnderSampling
# random_under_sampling: RandomUnderSampling = RandomUnderSampling(scaled_df)
# scaled_and_balanced_df: pdDataframe = random_under_sampling.balanced_df
# |--------------------------------------------------------------------------------------------------------------------|

# | Correlation Graph |------------------------------------------------------------------------------------------------|
# from graph.correlation_matrix_dataframe import CorrelationMatrixGraph
# correlation_matrix_graph: CorrelationMatrixGraph = CorrelationMatrixGraph(scaled_df, scaled_and_balanced_df)
# correlation_matrix_graph.show()
# |--------------------------------------------------------------------------------------------------------------------|

# | Boxplot Graph |----------------------------------------------------------------------------------------------------|
# from graph.corr_pos_neg_boxplot import CorrBoxPlot
# CorrBoxPlot(scaled_and_balanced_df).show()
# |--------------------------------------------------------------------------------------------------------------------|

# | Cutoff Ouliers |---------------------------------------------------------------------------------------------------|
# from data.treatment.cutoff_outliers import CutOffOutliers
# cutoff_outliers: CutOffOutliers = CutOffOutliers(scaled_and_balanced_df)
# scaled_and_balaced_df_without_outliers: pdDataframe = cutoff_outliers.cutoff(["V10", "V14", "V12"], 1)
# |--------------------------------------------------------------------------------------------------------------------|

# | Distribution Graph |-----------------------------------------------------------------------------------------------|
# from graph.all_dist_plots import AllDistPlots
# all_dist_plots: AllDistPlots = AllDistPlots(scaled_and_balaced_df_without_outliers)
# |--------------------------------------------------------------------------------------------------------------------|

# | Dimensionality Reduction Analysis |--------------------------------------------------------------------------------|
# from data.analysis.dimensionality_reduction_and_clustering import Algo
# DR_algo: Algo = Algo(scaled_and_balaced_df_without_outliers)
# DR_algo.run()
# DR_algo.plot()
# |--------------------------------------------------------------------------------------------------------------------|

# | MODELS |-----------------------------------------------------------------------------------------------------------|
# from models.classifiers import ClassifierModels
# classifier_models: ClassifierModels = ClassifierModels(scaled_and_balaced_df_without_outliers)
# classifier_models.run_brute()
# classifier_models.run_optimized()
# |--------------------------------------------------------------------------------------------------------------------|