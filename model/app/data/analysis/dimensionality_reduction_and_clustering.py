# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                         app/data/analysis/t_sne.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from config.config_files import configfiles
from log.genlog import genlog

from graph.DR import DR_graph, DR3D_graph

import numpy as np
from time import time

from sklearn.manifold import TSNE
from sklearn.decomposition import PCA, TruncatedSVD

from pandas.core.frame import DataFrame as pdDataframe
from pandas.core.series import Series as pdSeries
# |--------------------------------------------------------------------------------------------------------------------|


class Algo(object):
    def __init__(self, data: pdDataframe) -> None:
        """
        Initialize the T_SNE instance.
        """
        self.df: pdDataframe = data
        
        self.class_clmn: str = configfiles.dot_ini['dataframe']['dataframe:columns']['class']
    
        self._get_XY()
        
        self.graph  : DR_graph = DR_graph(self.Y)
        self.graph3d: DR3D_graph = DR3D_graph(self.Y)
    
    def _get_XY(self) -> None:
        """
        Get X and Y
        """
        self.X: pdDataframe  = self.df.drop(self.class_clmn, axis=1)
        self.Y: pdSeries     = self.df[self.class_clmn]
    
    def TSNE(self) -> np.ndarray:
        """
        Get T Distributed Stochastic Neighbor Embeding
        """
        a: float = time()
        self.X_TSNE: np.ndarray = TSNE(n_components=2, random_state=42).fit_transform(self.X.values)
        genlog.report("DEBUG", f"TSNE Algorithm: {round(time()-a, 4)}s")
        self.graph.graph(self.X_TSNE, 0, "t-SNE")
        
    def PCA(self) -> np.ndarray:
        """
        Get Principal Compoment Analsysis
        """
        a: float = time()
        self.X_PCA: np.ndarray = PCA(n_components=2, random_state=42).fit_transform(self.X.values)
        genlog.report("DEBUG", f"PCA Algorithm: {round(time()-a, 4)}s")
        self.graph.graph(self.X_PCA, 1, "PCA")
        
    def SVD(self) -> np.ndarray:
        """
        Get Truncated Singular Value Decomposition 
        """
        a: float = time()
        self.X_SVD: np.ndarray = TruncatedSVD(
            n_components=2, algorithm="randomized", random_state=42).fit_transform(self.X.values)
        genlog.report("DEBUG", f"SVD Algorithm: {round(time()-a, 4)}s")
        self.graph.graph(self.X_SVD, 2, "Truncated SVD")
    
    def TSNE_3D(self) -> np.ndarray:
        """
        Get T Distributed Stochastic Neighbor Embbeding in 3 components
        """
        a: float = time()
        self.X_TSNE3D: np.ndarray = TSNE(n_components=3, random_state=42).fit_transform(self.X.values)
        genlog.report("DEBUG", f"TSNE 3D Algorithm:{round(time()-a, 4)}s")
        self.graph3d.graph(self.X_TSNE3D, "t-SNE 3D")
    
    def run(self) -> None:
        self.TSNE()
        self.PCA()
        self.SVD()
        self.TSNE_3D()
         
    def plot(self) -> None:
        self.graph.show()
        self.graph3d.show()