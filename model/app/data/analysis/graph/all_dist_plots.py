# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                          app/data/analysis/graph/all_dist_plots.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files    import configfiles
from log.genlog             import genlog
from theme.romuro           import theme_romuro, ROMURO_BLUE, ROMURO_RED

import seaborn              as sns
import matplotlib.pyplot    as plt

from pandas.core.frame          import DataFrame as pdDataframe
from pandas.core.series         import Series as pdSeries
from pandas.core.indexes.base   import Index as pdIndex
from matplotlib.axes            import _axes
from matplotlib.figure          import Figure
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
    
    def _create_histplot(self, column: str, ax: _axes.Axes, fig: Figure) -> None:
        """
        Creates a histplot graph
        Args:
            column (str): Column name
            ax (_axes.Axes): axes from matplotlib
            fig (Figure): figure from matplotlib
        """
        data: pdSeries = self.df[column]
        fraud: pdSeries = data[self.df[self.clmn_class] == 1]
        n_fraud: pdSeries = data[self.df[self.clmn_class] == 0]
        
        sns.histplot(x=fraud, color=ROMURO_RED, label=column, kde=True, ax=ax)
        sns.histplot(x=n_fraud, color=ROMURO_BLUE, label=column, kde=True, ax=ax)
               
        theme_romuro(ax, fig, column, f"Density [{column}]", None)
        
        genlog.report(True, f"Generate {column} histplot")
    
    def _gen_graph(self) -> None:
        """
        Generates all histplots
        """
        lines, columns = self._get_lines_columns(len(self.columns))
        coor: list[tuple[int]] = self._generate_coor_js(lines, columns)
        fig, axes = plt.subplots(lines, columns, figsize=(20, 20))
        
        for column, coor in zip(self.columns, coor):
            self._create_histplot(column, axes[coor[0]][coor[1]], fig)
        
        plt.show()
        plt.clf()
    
    def gen_graph_by_column(self, columns_names: list[str]) -> None:
        """
        Generates the graphs based on columns names
        Args:
            columns_names (list[str]): Columns names to generate the graphs
        """
        lines, columns = self._get_lines_columns(len(columns_names))
        coor: list[tuple[int]] = self._generate_coor_js(lines, columns)
        fig, axes = plt.subplots(lines, columns, figsize=(20, 20))
        
        for column, coor in zip(columns_names, coor):
            self._create_histplot(column, axes[coor[0]][coor[1]], fig)
        
        plt.show()
        plt.clf()
        