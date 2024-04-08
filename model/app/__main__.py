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
from func.correlation_graph     import correlation_matrix_graph
from func.boxplot_graph         import boxplot_graph
from func.cutoff_outliers       import cutoff_outliers
from func.dist_graph            import dist_graph
from func.DRA                   import dimensionality_reduction
from func.classifiers_model     import classifiers_model
from func.SMOTE_oversampling    import oversampling
from func.ANN_model             import ANN_model
# |--------------------------------------------------------------------------------------------------------------------|

csv_path            : PosixPath     = download_data()
df                  : pdDataframe   = read_data(csv_path)
df_s                : pdDataframe   = scale_time_amount_features(df)

data_info(df), time_amount_graph(df)

# | Train Test Split |----------------------|
tt = split_train_test(df_s)
Xt, Yt, train_df_s = tt.train()
Xr, Yr, test_df_s  = tt.test()
# |-----------------------------------------|

# | Undersampling branch |------------------------------------------------------| 
train_df_s_b : pdDataframe   = random_undersampling(train_df_s)
correlation_matrix_graph(train_df_s, train_df_s_b)
boxplot_graph(train_df_s_b)
train_df_s_b_wo : pdDataframe   = cutoff_outliers(train_df_s_b, mode=1)
dist_graph(train_df_s_b_wo)
dimensionality_reduction(train_df_s_b_wo)
classifiers_model(train_df_s_b_wo, Xr, Yr)
ANN_model(train_df_s_b_wo, Xr, Yr)
# |----------------------------------------------------------------------------|

# | Oversampling Branch |------------------------------------------------------|
train_ndf_s_b            : pdDataframe   = oversampling(train_df_s)
correlation_matrix_graph(train_df_s, train_ndf_s_b)
boxplot_graph(train_ndf_s_b)
dist_graph(train_ndf_s_b)
ANN_model(train_ndf_s_b, Xr, Yr)
# |----------------------------------------------------------------------------|