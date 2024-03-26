# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                            app/data/analysis/DR.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Import |-----------------------------------------------------------------------------------------------------------|
from theme.romuro import theme_romuro, ROMURO_RED, ROMURO_BLUE

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from pandas.core.series import Series as pdSeries

from matplotlib.figure import Figure
from matplotlib.axes import Axes
# |--------------------------------------------------------------------------------------------------------------------|


class DR_graph(object):
    def __init__(self, y: pdSeries) -> None:
        """
        Initialize the DR_graph instance.
        Args:
            y (pdSeries): The Class series (fraud or no-fraud)
        """
        self.y: pdSeries = y
        self._create_fig()
        
    def _create_fig(self) -> None:
        """
        Creates a figure with 1 row and 3 columns
        """
        self.plot: tuple[Figure, tuple[Axes]] = plt.subplots(1, 3)
        for ax in self.plot[1]:
            theme_romuro(ax, self.plot[0], "", "", "")
    
    def _fraud_split(self, data: np.ndarray) -> tuple[list[np.float64]]:
        """
        Generates two list with fraud and no-fraud data.
        Args:
            data (np.ndarray): Dimensionality Reduction Data

        Returns:
            tuple[list[np.ndarray]]: (Fraud, No-Fraud) data. Each with (X, Y)
        """
        fraud   : list[list[np.float64]] = [[], []]
        n_fraud : list[list[np.float64]] = [[], []]
        for n, i in enumerate(self.y):
            if i == 1:
                fraud[0].append(data[n, 0])
                fraud[1].append(data[n, 1])
            if i == 0:
                n_fraud[0].append(data[n, 0])
                n_fraud[1].append(data[n, 1])
        
        return fraud, n_fraud
        
    def graph(self, data: np.ndarray, column: int, title: str) -> None:
        fraud, n_fraud = self._fraud_split(data)
        self.plot[1][column].scatter(n_fraud[0], n_fraud[1], c=ROMURO_BLUE, label="No Fraud", s=0.5)
        self.plot[1][column].scatter(fraud[0], fraud[1], c=ROMURO_RED, label="Fraud", s=0.5)
        self.plot[1][column].set_title(title)
        
    
    def show(self) -> None:
        plt.show()
        plt.clf()


class DR3D_graph(object):
    def __init__(self, y: pdSeries) -> None:
        """
        Initialize the DR3D graph intance.
        Args:
            y (pdSeries): The Class series (fraud or no-fraud)
        """
        self.y: pdSeries = y
        self._create_fig()
    
    def _create_fig(self) -> None:
        self.fig: Figure = plt.figure()
        self.ax: Axes = self.fig.add_subplot(projection="3d")
        theme_romuro(self.ax, self.fig, "", "", "")
    
    def _fraud_split(self, data: np.ndarray) -> tuple[list[np.float64]]:
        """
        Generates two list with fraud and no-fraud data.
        Args:
            data (np.ndarray): Dimensionality Reduction Data

        Returns:
            tuple[list[np.ndarray]]: (Fraud, No-Fraud) data. Each with (X, Y, Z)
        """
        fraud   : list[list[np.float64]] = [[], [], []]
        n_fraud : list[list[np.float64]] = [[], [], []]
        
        for n, i in enumerate(self.y):
            if i == 1:
                fraud[0].append(data[n, 0])
                fraud[1].append(data[n, 1])
                fraud[2].append(data[n, 2])
            if i == 0:
                n_fraud[0].append(data[n, 0])
                n_fraud[1].append(data[n, 1])
                n_fraud[2].append(data[n, 2])
        
        return fraud, n_fraud

    def graph(self, data: np.ndarray, title: str) -> None:
        fraud, n_fraud = self._fraud_split(data)
        self.ax.scatter(fraud[0], fraud[1], fraud[2], c=ROMURO_RED, s=0.5)
        self.ax.scatter(n_fraud[0], n_fraud[1], n_fraud[2], c=ROMURO_BLUE, s=0.5)
        
        self.ax.xaxis.set_pane_color((0.15, 0.15, 0.15, 1))
        self.ax.yaxis.set_pane_color((0.15, 0.15, 0.15, 1))
        self.ax.zaxis.set_pane_color((0.15, 0.15, 0.15, 1))

        self.ax.grid(False)
        self.ax.tick_params("both", color="#404040")
        self.ax.xaxis.pane.set_edgecolor('#404040')
        self.ax.yaxis.pane.set_edgecolor('#404040')
        self.ax.zaxis.pane.set_edgecolor('#404040')
        
        self.ax.set_title(title)
    
    def show(self) -> None:
        plt.show()
        plt.clf()