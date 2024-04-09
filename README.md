# Credit Card Fraud Detector

In this repository, we shall employ diverse predictive models to assess their efficacy in discerning whether a transaction qualifies as a routine payment or is indicative of fraudulent activity.

---

| Dataset name | about | link |
|-|-|-|
| __Credit Card Fraud__ | Anonymized credit card transactions labeled as fraudulent or genuine. The dataset contains transactions made by credit cards in September 2013 by European cardholders | [Dataset link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data) |

---

## Results

The project employed various classification algorithms, including logistic regression, support vector machines, and k-nearest neighbors. All of them exhibited an accuracy ranging from 92% to 94%. However, when analyzing the accuracy of the models in predicting fraudulent samples, the accuracy ranged from 1% to 9%.

Given these results, a deep learning model was implemented, which achieved an overall accuracy of 99.97%, with a precision of predicting fraudulent samples at 84.67%.

| Model | Balancing Method | Mode | Precision | Fraud Precision |
|-------|------------------|------|-----------|-----------------|
| __Logistic Regression__       | random under-sampling | [brute, cross-validation] | 92.25% | 4.45% |
| __K-Nearest Neighbors__       | random under-sampling | [brute, cross-validation] | 94.25% | 4.73% |
| __Support Vector Machine__    | random under-sampling | [brute, cross-validation] | 93.58% | 9.05% |
| __Decision Tree__             | random under-sampling | [brute, cross-validation] | 89.62% | 1.31% |
| __Logistic Regression__       | random under-sampling | [optimized, cross-validation] | 92.25% | 4.45% |
| __K-Nearest Neighbors__       | random under-sampling | [optimized, cross-validation] | 94.25% | 4.40% |
| __Support Vector Machine__    | random under-sampling | [optimized, cross-validation] | 92.29% | 6.05% |
| __Decision Tree__             | random under-sampling | [optimized, cross-validation] | 89.58% | 6.34% |
| __ANN__                       | random under-sampling | [cross-validation] | 97.83% | 5.45% |
| __ANN__                       | SMOTE over-sampling   | [cross-validation] | 99.97% | 84.67% |

--- 

## Installation

First, we must establish a virtual development environment and install the dependencies:

```bash
cd model && python3 -m venv venv && source venv/bin/activate
```

To install the dependencies:

```bash
pip install --no-cache -r requirements.txt
```

---

### Run

Before running the code, it is necessary to [download the Kaggle data](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data). Afterward, move the zip file to the `/model/app/resources/` folder of the project and rename the file to `data.zip`. If a folder named `resources` does not exist, please create one.

To execute and obtain the results of the models, it is necessary to run the command:

```bash
python app
```

You can utilize the command `python app --help` to explore additional functionalities and supplementary analyses.

```bash
python app --help
usage: app [-h] [--graphs] [--info] [--time_amount_graph] [--corrgraph] [--boxgraph] [--distgraph] [--learningcurvegraph] [--DRA]

Credit Card Fraud Detection Models

options:
  -h, --help            show this help message and exit
  --graphs              Plot all graphs
  --info                Dataset informations
  --time_amount_graph   Time and Amount Distribution Graphs
  --corrgraph           Features Correlation Graph
  --boxgraph            Feature Boxplot Graphs
  --distgraph           Feature Distribution Graph
  --learningcurvegraph  Learning Curve of classification models
  --DRA                 Dimensionality Reduction Analysis
```

---

### Code Structure

The entire code is organized into directories based on their functionalities. Each data preprocessing, graphing, or modeling task is developed as an object to facilitate code modification or restructuring.

```
app
├── config
├── data
│   ├── analysis
│   ├── info
│   └── treatment
├── func
├── graph
├── log
├── models
├── resources
└── theme
```

The code is thoroughly documented. Should you wish to modify any parameters of the analyses or models, you can find them in [model/app/config/](/model/app/config/). Within this directory, you will encounter several `.ini` files containing their respective parameters.

For data information, analyses, or preprocessing, refer to [/app/data/](/model/app/data/). Graphs related to the preprocessing and analysis can be found in [/app/graphs/](/model/app/graph/). The [/app/theme/](/model/app/theme/) directory pertains to the stylization of the graphs utilized to generate a development model report.

The models utilized are located in the directory [/app/models/](/model/app/models/). It is worth noting that their parameters are listed in the `.ini` files within the config directory.

The [/app/resources](/model/app/resources/) directory, as mentioned earlier, contains the databases that will be utilized. Here, you will find the zip file sourced from Kaggle and the uncompressed .csv file.

The [/app/func/](/model/app/func/) directory entails an adaptation of the code to enhance the ease of use and fluidity of analyses and models. Within this directory, there is a translation of the objects created for functional programming.

```python
# To undersample the data
df_undersampling: pdDataframe = random_undersampling(df)

# To apply the ANN model in the data
ANN_model(df_undersampling, df_x, df_y)
```

As depicted above, this approach enhances readability, making it clearer to discern the operations executed in the `__main__.py` file due to the functional methodology.