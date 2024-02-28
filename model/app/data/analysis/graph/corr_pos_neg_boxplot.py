# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                    app/data/analysis/graph/corr_pos_neg_boxplot.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files    import configfiles
from log.genlog             import genlog
from theme.romuro           import theme_romuro, ROMURO_BLUE, ROMURO_RED, MEDIUM_WHITE

import matplotlib.pyplot    as plt
import seaborn              as sns

from pandas.core.series         import Series       as pdSeries
from pandas.core.frame          import DataFrame    as pdDataframe
from pandas.core.indexes.base   import Index        as pdIndex
from matplotlib.axes            import _axes
from matplotlib.figure          import Figure
# |--------------------------------------------------------------------------------------------------------------------|


class CorrBoxPlot(object):
    """
    Analysis the variables that contain correlation with Class variable
    """
    def __init__(self, balanced_df: pdDataframe) -> None:
        """
        Initialize the CorrBoxPlot instance.
        Args:
            balanced_df (pdDataframe): The balanced data in Dataframe type
        """
        self.df: pdDataframe = balanced_df
        
        self.clmn_class: str = configfiles.dot_ini['dataframe']['dataframe:columns']['class']
        
        self.neg_param_corr: float = float(configfiles.dot_ini['analysis']['correlation:negative']['threshold'])
        self.pos_param_corr: float = float(configfiles.dot_ini['analysis']['correlation:positive']['threshold'])

        self._get_class_corr()
        self._get_columns_corr()
        
    def _get_class_corr(self) -> None:
        """
        Get the Correlation Class column from .corr() function
        """
        self.class_corr: pdSeries = self.df.corr()[self.clmn_class]
        self.class_corr: pdSeries = self.class_corr.drop(self.clmn_class)
    
    def _get_columns_corr(self) -> None:
        """
        Get the correlation based on correlation threshold.
        """
        self.clmns_neg_corr: pdIndex = self.class_corr[self.class_corr < -self.neg_param_corr].index
        self.clmns_pos_corr: pdIndex = self.class_corr[self.class_corr > self.pos_param_corr].index
    
    @staticmethod
    def _get_lines_columns(qnt: int) -> tuple[int, int]:
        if qnt >= 4:
            alpha   : float = qnt**(1/2)
            column  : int = int(alpha)
            lines   : int = column+2 if alpha % column > 0 else column
            return lines, column
        return 1, qnt
    
    @staticmethod
    def _generate_coor_ij(lines: int, columns: int) -> list[list[int]]:
        coor: list[list[int]] = []
        for i in range(lines):
            for j in range(columns):
                coor.append([i, j])
        return coor
        
    @staticmethod
    def _create_boxplot(x: str, y: str, data: pdDataframe, ax: _axes.Axes, fig: Figure) -> None:
        """
        Create boxplot
        """
        sns.boxplot(x=x, y=y, data=data, ax=ax, palette=[ROMURO_BLUE, ROMURO_RED],
                    fill=True, fliersize=0.7, linewidth=0.7, saturation=1)
        ax.set_xlabel("Class", fontsize=6)
        theme_romuro(ax, fig, "Class", y, None)
        genlog.report(True, f"Created ({y}) Boxplot")
    
    def boxplot_graph(self, var_index: pdIndex, corr_type: str) -> None:
        """
        Generate Negative Correlation Boxplot
        """
        if len(var_index) != 0:
            lines, columns = self._get_lines_columns(len(var_index))
            matrix_graph_coor: list[list[int]] = self._generate_coor_ij(lines, columns)
            
            fig, axes = plt.subplots(lines, columns, figsize=(5, 20))
            
            for name, coor in zip(var_index, matrix_graph_coor):
                if len(var_index) >= 4:
                    self._create_boxplot(self.clmn_class, name, self.df, axes[coor[0]][coor[1]], fig)
                else:
                    self._create_boxplot(self.clmn_class, name, self.df, axes[coor[1]], fig)
                
            fig.subplots_adjust(hspace=0.8, wspace=0.5)
            fig.suptitle(f'Var vs Class {corr_type} Correlation', fontsize=12, color=MEDIUM_WHITE)
        else:
            genlog.report(False, f"No {corr_type} correlation that satisfies ({self.neg_param_corr})")
        
        plt.show()
        plt.clf()
    
    def show(self) -> None:
        self.boxplot_graph(self.clmns_neg_corr, "Negative")
        self.boxplot_graph(self.clmns_pos_corr, "Positive")
        