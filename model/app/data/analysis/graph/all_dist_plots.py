# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                          app/data/analysis/graph/all_dist_plots.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files import configfiles
from log.genlog import genlog

import seaborn as sns
import matplotlib.pyplot as plt

from pandas.core.frame import DataFrame as pdDataframe
from pandas.core.series import Series as pdSeries
from pandas.core.indexes.base import Index as pdIndex
from matplotlib.axes import _axes
# |--------------------------------------------------------------------------------------------------------------------|


class AllDistPlots(object):
    def __init__(self, dataframe: pdDataframe) -> None:
        """
        Initialize the AllDistPlots
        Args:
            dataframe (pdDataframe): The data in dataframe type
        """
        self.clmn_class: str = configfiles.dot_ini['dataframe']['dataframe:columns']['class']
        
        self.df: pdDataframe = dataframe
        self.columns: pdIndex = self.df.columns
        self.columns: pdIndex = self.columns.drop(self.clmn_class)
        
        self._gen_graph()
    
    @staticmethod
    def _get_lines_columns(qnt: int) -> tuple[int, int]:
        if qnt >= 4:
            alpha   : float = qnt**(1/2)
            column  : int = int(alpha)
            lines   : int = column+1 if alpha % column > 0 else column
            return lines, column
        return 1, qnt

    @staticmethod
    def _generate_coor_js(lines: int, columns: int) -> list[tuple[int]]:
        coor: list[tuple[int]] = []
        for i in range(lines):
            for j in range(columns):
                coor.append((i, j))
        return coor
    
    def _create_histplot(self, column: str, ax: _axes.Axes) -> None:
        data: pdSeries = self.df[column]
        fraud: pdSeries = data[self.df[self.clmn_class] == 1]
        n_fraud: pdSeries = data[self.df[self.clmn_class] == 0]
        
        sns.histplot(x=fraud, color="red", label=column, kde=True, ax=ax)
        sns.histplot(x=n_fraud, color="skyblue", label=column, kde=True, ax=ax)
        
        genlog.report(True, f"Generate {column} histplot")
    
    def _gen_graph(self) -> None:
        lines, columns = self._get_lines_columns(len(self.columns))
        coor: list[tuple[int]] = self._generate_coor_js(lines, columns)
        fig, axes = plt.subplots(lines, columns, figsize=(20, 20))
        
        for column, coor in zip(self.columns, coor):
            self._create_histplot(column, axes[coor[0]][coor[1]])
        
        plt.show()
        plt.clf()