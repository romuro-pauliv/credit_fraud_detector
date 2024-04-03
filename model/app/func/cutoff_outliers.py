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

feature_c0: str = configfiles.dot_ini['treatment']['treatment:cutoff_outliers']["class_0"]
feature_c1: str = configfiles.dot_ini['treatment']['treatment:cutoff_outliers']["class_1"]

def _transform(ini_data: str) -> list[str]:
    if ini_data == "None":
        return []
    return ini_data.split(",")

def cutoff_outliers(data: pdDataframe) -> pdDataframe:
    coo: CutOffOutliers = CutOffOutliers(data)
    data: pdDataframe = coo.cutoff(_transform(feature_c0), 0)
    
    coo: CutOffOutliers = CutOffOutliers(data)
    data: pdDataframe = coo.cutoff(_transform(feature_c1), 1)
    
    return data