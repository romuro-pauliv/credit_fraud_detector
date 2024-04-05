# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                          app/models/classifiers.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from graph.classifiers_learn_curve  import LearningCurveGraph
from config.config_files            import configfiles
from log.genlog                     import genlog

import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, learning_curve, ShuffleSplit

from sklearn.linear_model   import LogisticRegression
from sklearn.svm            import SVC
from sklearn.neighbors      import KNeighborsClassifier
from sklearn.tree           import DecisionTreeClassifier

from pandas.core.frame  import DataFrame    as pdDataframe
from pandas.core.series import Series       as pdSeries

from typing import Any
# |--------------------------------------------------------------------------------------------------------------------|


class ClassifierModels(object):
    def __init__(self, data: pdDataframe) -> None:
        """
        Initialize the ClassfierModels instance.
        Args:
            data (pdDataframe): The dataframe in pandas Dataframe
        """
        self.class_clmn: str = configfiles.dot_ini["dataframe"]["dataframe:columns"]["class"]
        
        self.X: pdDataframe = data.drop(self.class_clmn, axis=1)
        self.Y: pdSeries    = data[self.class_clmn]
        
        self.test_size      : float = float(configfiles.dot_ini['classifiers']['database']["train_test_split"])
        self.random_state   : int = int(configfiles.dot_ini['classifiers']['database']['random_state'])

        self._split_train_test()
        self._define_classifiers()
        
        self.learning_curve_graph: LearningCurveGraph = LearningCurveGraph()
        
    def _split_train_test(self) -> None:
        """
        Split the X and Y in train a and test.
        """
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.X, self.Y, test_size=0.2, random_state=self.random_state)
        self._convert_train_test2array()
        
    def _convert_train_test2array(self) -> None:
        """
        Convert train and test dataframes to np.ndarray
        """
        self.X_train: np.ndarray = self.X_train.values
        self.X_test : np.ndarray = self.X_test.values
        self.Y_train: np.ndarray = self.Y_train.values
        self.Y_test : np.ndarray = self.Y_test.values
    
    def _define_classifiers(self) -> None:
        """
        Defines the Machine Learning Algorithms
        """
        self.classifiers: list[LogisticRegression, KNeighborsClassifier, SVC, DecisionTreeClassifier] = [
            LogisticRegression(),
            KNeighborsClassifier(),
            SVC(),
            DecisionTreeClassifier()
        ]

    def _grid_search_optimizer(self) -> None:
        """
        Options to run the GridSearch Optimizer
        """
        self.optimizer: list[dict[str, Any]] = [
            {
                "penalty": ["l1", "l2"],
                "C": [0.001, 0.01, 0.1, 1, 10, 100, 1000]
            },
            {
                "n_neighbors": list(range(2, 5, 1)),
                "algorithm": ["auto", "ball_tree", "kd_tree", "brute"]
            },
            {
                "C": [0.5, 0.7, 0.9, 1],
                "kernel": ["rbf", "poly", "sigmoid", "linear"]
            },
            {
                "criterion": ["gini", "entropy"],
                "max_depth": list(range(2, 4, 1)),
                "min_samples_leaf": list(range(5,7,1))
            }
        ]
    
    def _apply_optimizer(self) -> None:
        """
        Apply the GridSearchCV
        """
        self._grid_search_optimizer()
        
        self.classifiers_optimized_object: list[Any] = []
        self.classifiers_optimized: list[Any] = []
        
        for algorithm, params in zip(self.classifiers, self.optimizer):
            self.classifiers_optimized_object.append(GridSearchCV(algorithm, params))
        
        for algorithm_opt in self.classifiers_optimized_object:
            algorithm_opt.fit(self.X_train, self.Y_train)
            self.classifiers_optimized.append(algorithm_opt.best_estimator_)
            
    def train(self, classifiers: list, fit: bool, type_: str) -> None:
        """
        Train and get the algoritms results
        Args:
            classifiers (list): A list of classifiers object from sklearn
        """
        self.models: list[Any] = []
        for n, algorithm in enumerate(classifiers):
            algorithm.fit(self.X_train, self.Y_train) if fit is True else None
            training_score: np.ndarray = cross_val_score(algorithm, self.X_test, self.Y_test, cv=10)
            self.models.append(algorithm)
            
            log: str = f"{self.classifiers[n].__class__.__name__} | {round(training_score.mean(), 4) * 100}%"
            genlog.report(
                True,
                f"classifier model: [{type_}] {log}"
            )
    
    def _learing_curve(self, model: Any) -> list[np.ndarray, str]:
        """
        Determines cross-validated training and test scores for different training set sizes.

        A cross-validation generator splits the whole dataset k times in training and test data. Subsets of the training
        set with varying sizes will be used to train the estimator and a score for each training subset size and the 
        test set will be computed. Afterwards, the scores will be averaged over all k runs for each training subset size.
        """
        cv              : ShuffleSplit = ShuffleSplit(100, test_size=0.2, random_state=42)
        n_jobs          : int = -1
        train_size_param: np.ndarray = np.linspace(0.1, 1, 20)
        
        train_size, train_score, test_score = learning_curve(
            model, self.X_train, self.Y_train, cv=cv, n_jobs=n_jobs, train_sizes=train_size_param 
        )
        
        genlog.report("debug", f"classifier model: Learning Curve -> {model.__class__.__name__}")
        return train_size, train_score, test_score, model.__class__.__name__
        
    def run_learning_curve(self) -> None:
        model_data_list: list[list[np.ndarray, str]] = []
        for model in self.models:
            model_data_list.append(self._learing_curve(model))

        self.learning_curve_graph.post_models(model_data_list)
        self.learning_curve_graph.show()
        
    def run_brute(self, learing_curve: bool) -> None:
        self._define_classifiers()
        self.train(self.classifiers, True, "brute")
        self.run_learning_curve() if learing_curve == True else None
    
    def run_optimized(self, learning_curve: bool) -> None:
        self._define_classifiers()
        self._apply_optimizer()
        self.train(self.classifiers_optimized, False, "optimized")
        self.run_learning_curve() if learning_curve == True else None