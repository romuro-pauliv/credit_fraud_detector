import warnings
warnings.filterwarnings("ignore")

# | Imports |----------------------------------------------------------------------------------------------------------|
from pandas.core.frame          import DataFrame as pdDataframe
from pathlib                    import PosixPath

from func.download_data         import download_data
from func.read_data             import read_data
from func.data_info             import data_info
from func.time_amount_graph     import time_amount_graph
from func.scale_time_amount     import scale_time_amount_features
from func.split_train_test      import split_train_test
from func.random_undersampling  import random_undersampling
# |--------------------------------------------------------------------------------------------------------------------|

csv_path            : PosixPath     = download_data()
df                  : pdDataframe   = read_data(csv_path)

data_info(df)
time_amount_graph(df)

df_scaled           : pdDataframe   = scale_time_amount_features(df)
df_scaled_balanced  : pdDataframe   = random_undersampling(df_scaled)

# split_train_test(df_scaled)

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