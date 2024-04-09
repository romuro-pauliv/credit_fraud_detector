# |--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                  app/models/ANN.py |
# |                                                                                                    encoding: UTF-8 |
# |                                                                                                     Python v: 3.10 |
# |--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from log.genlog             import genlog
from config.config_files    import configfiles

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

from keras.models       import Sequential
from keras.layers       import Dense
from keras.optimizers   import Adam

from pandas.core.frame  import DataFrame    as pdDataframe
from pandas.core.series import Series       as pdSeries

from keras.src.models.sequential import Sequential as kSequential
# |--------------------------------------------------------------------------------------------------------------------|


class ANNModel(object):
    def __init__(self, data: pdDataframe) -> None:
        """
        Initialize the ANNmodel instance.
        Args:
            data (pdDataframe): The dataframe in pandas dataframe
        """
        self.class_clmn: str = configfiles.dot_ini['dataframe']['dataframe:columns']['class']
        
        self.X: pdDataframe = data.drop(self.class_clmn, axis=1)
        self.Y: pdSeries    = data[self.class_clmn]
        
        self.test_size      : float = float(configfiles.dot_ini['ANN']['database']['train_test_split'])
        self.random_state   : int   = int(configfiles.dot_ini['ANN']['database']['random_state'])
        
        self._split_train_test()
        self._ANN_model()
        self._ANN_compile()
        self._ANN_fit()
        
    def _split_train_test(self) -> None:
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.X, self.Y, test_size=self.test_size, random_state=self.random_state
        )
        self._convert_train_test2array()

    def _convert_train_test2array(self) -> None:
        """
        Convert train and test dataframes to np.ndarray
        """
        self.X_train: np.ndarray = self.X_train.values
        self.X_test : np.ndarray = self.X_test.values
        self.Y_train: np.ndarray = self.Y_train.values
        self.Y_test : np.ndarray = self.Y_test.values
    
    def _ANN_model(self) -> None:
        """
        Create a ANN model
        """
        act_l1: str = configfiles.dot_ini["ANN"]["model:activation"]["layer1"]
        act_l2: str = configfiles.dot_ini["ANN"]["model:activation"]["layer2"]
        act_l3: str = configfiles.dot_ini["ANN"]["model:activation"]["layer3"]
        act_l4: str = configfiles.dot_ini["ANN"]["model:activation"]["layer4"]
        
        uni_l2: int = int(configfiles.dot_ini["ANN"]["model:units"]["layer2"])
        uni_l3: int = int(configfiles.dot_ini["ANN"]["model:units"]["layer3"])
        uni_l4: int = int(configfiles.dot_ini["ANN"]["model:units"]["layer4"])
        
        self.keras_model: kSequential = Sequential([
            Dense(self.X_train.shape[1], input_shape=(self.X_train.shape[1], ), activation=act_l1),
            Dense(uni_l2, activation=act_l2),
            Dense(uni_l3, activation=act_l3),
            Dense(uni_l4, activation=act_l4)
        ])
        self.keras_model.summary()
    
    def _ANN_compile(self) -> None:
        p_loss      : str = configfiles.dot_ini["ANN"]["model:compile"]["loss"]
        p_metrics   : str = configfiles.dot_ini["ANN"]["model:compile"]["metrics"]
        
        self.keras_model.compile(Adam(), loss=p_loss, metrics=[p_metrics])
    
    def _ANN_fit(self) -> None:
        p_validation_split  : float = float(configfiles.dot_ini["ANN"]["model:fit"]["validation_split"])
        p_batch_size        : int   = int(configfiles.dot_ini["ANN"]["model:fit"]["batch_size"])
        p_epochs            : int   = int(configfiles.dot_ini["ANN"]["model:fit"]["epochs"])
        p_shuffle           : bool  = bool(configfiles.dot_ini["ANN"]["model:fit"]["shuffle"])
        p_verbose           : int   = int(configfiles.dot_ini["ANN"]["model:fit"]["verbose"])
        
        self.keras_model.fit(
            self.X_train, self.Y_train,
            validation_split=p_validation_split,
            batch_size=p_batch_size,
            epochs=p_epochs,
            shuffle=p_shuffle,
            verbose=p_verbose
        )

    def real_test(self, X: pdDataframe, Y: pdSeries) -> None:
        X: np.ndarray = X.values
        Y: np.ndarray = Y.values
        
        predict: np.ndarray = np.argmax(self.keras_model.predict(X),axis=1)
        
        cm: np.ndarray = confusion_matrix(Y, predict)
        fraud_precision     : float = round((cm[1][1]/(cm[1][1] + cm[0][1]))*100, 4)
        n_fraud_precision   : float = round((cm[0][0]/(cm[0][0] + cm[1][0]))*100, 4)

        log_prefix: str = f"classifier model: ANN | precision"
        genlog.report("debug", f"{log_prefix} [n-fraud: {n_fraud_precision}%] [fraud: {fraud_precision}%]")
        print(classification_report(Y, predict))