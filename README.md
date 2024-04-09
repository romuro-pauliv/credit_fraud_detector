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

Before running the code, it is necessary to [download the Kaggle data](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data). Afterward, move the zip file to the `/model/app/resources/` folder of the project and rename the file to `data.zip`.

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
