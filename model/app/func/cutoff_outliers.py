# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                        app/func/cutoff_outliers.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from pandas.core.frame              import DataFrame as pdDataframe
from data.treatment.cutoff_outliers import CutOffOutliers
from config.config_files            import configfiles
# |--------------------------------------------------------------------------------------------------------------------|

M1_feature_c0: str = configfiles.dot_ini['treatment']['treatment:cutoff_outliers']["M1_class_0"]
M1_feature_c1: str = configfiles.dot_ini['treatment']['treatment:cutoff_outliers']["M1_class_1"]

M2_feature_c0: str = configfiles.dot_ini['treatment']['treatment:cutoff_outliers']["M2_class_0"]
M2_feature_c1: str = configfiles.dot_ini['treatment']['treatment:cutoff_outliers']["M2_class_1"]


def _transform(ini_data: str) -> list[str]:
    if ini_data == "None":
        return []
    return ini_data.split(",")

def cutoff_outliers(data: pdDataframe, mode: int) -> pdDataframe:
    if mode == 1:
        coo: CutOffOutliers = CutOffOutliers(data)
        data: pdDataframe = coo.cutoff(_transform(M1_feature_c0), 0)
    
        coo: CutOffOutliers = CutOffOutliers(data)
        data: pdDataframe = coo.cutoff(_transform(M1_feature_c1), 1)
    
    if mode == 2:
        coo: CutOffOutliers = CutOffOutliers(data)
        data: pdDataframe = coo.cutoff(_transform(M2_feature_c0), 0)
    
        coo: CutOffOutliers = CutOffOutliers(data)
        data: pdDataframe = coo.cutoff(_transform(M2_feature_c1), 1)
    
    return data