# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                 app/data/analysis/graph/classifiers_learn_curve.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from log.genlog     import genlog
from theme.romuro   import theme_romuro, ROMURO_BLUE, ROMURO_RED

from sklearn.model_selection import learning_curve, ShuffleSplit

import numpy                as np
import matplotlib.pyplot    as plt

from matplotlib.figure  import Figure
from matplotlib.axes    import Axes

from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|


class LearningCurveGraph(object):
    def __init__(self, X: np.ndarray, Y: np.ndarray) -> None:
        """
        Args:
            X (np.ndarray): X values
            Y (np.ndarray): Y values
        """
        self.X: np.ndarray = X
        self.Y: np.ndarray = Y
        self._parameters()
        
    def _parameters(self) -> None:
        """
        Parameters to learning_curve function
        """
        self.cv: ShuffleSplit = ShuffleSplit(100, test_size=0.2, random_state=42)
        self.n_jobs: int = 4
        self.train_size_param: np.ndarray = np.linspace(0.1, 1, 20)
        
    def post_models(self, models: list[Any]) -> None:
        """
        Define the models list
        Args:
            models (list[Any]): models list
        """
        self.models_list: list[Any] = models
    
    def _define_plot(self) -> tuple[Figure, Axes]:
        """
        Creates a graph
        Returns:
            tuple[Figure, Axes]: The Figure and Axes matplotlib
        """
        graph: tuple[Figure, Axes] = plt.subplots()
        theme_romuro(graph[1], graph[0], "","","")
        return graph
    
    def define_data_plot(self, train_size: np.ndarray, train_score: np.ndarray, test_score: np.ndarray, t: str) -> None:
        """
        Defines the data and input in the graph
        """
        graph: tuple[Figure, Axes] = self._define_plot()
        
        train_score_mean: np.ndarray = np.mean(train_score, axis=1)
        train_score_std : np.ndarray = np.std(train_score, axis=1)
        test_score_mean : np.ndarray = np.mean(test_score, axis=1)
        test_score_std  : np.ndarray = np.std(test_score, axis=1)
        
        graph[1].plot(train_size, train_score_mean, color=ROMURO_RED, label="Training Score")
        graph[1].plot(train_size, test_score_mean, color=ROMURO_BLUE, label="Test Score")
        
        graph[1].fill_between(
            train_size, train_score_mean - train_score_std, train_score_mean + train_score_std, 
            alpha=0.1, color=ROMURO_RED
        )
        graph[1].fill_between(
            train_size, test_score_mean - test_score_std, test_score_mean + test_score_std,
            alpha=0.1, color=ROMURO_BLUE
        )
        graph[1].set_xlabel("Training size (m)")
        graph[1].set_ylabel("Score")
        graph[1].set_title(t)
        
    
    def _estimator_data(self, model: Any) -> None:
        train_size, train_score, test_score = learning_curve(
            model, self.X, self.Y, cv=self.cv, n_jobs=self.n_jobs, train_sizes=self.train_size_param
        )
        self.define_data_plot(train_size, train_score, test_score, model.__class__.__name__)
        
    def show(self) -> None:
        for model in self.models_list:
            self._estimator_data(model)
        plt.show()
        plt.clf()