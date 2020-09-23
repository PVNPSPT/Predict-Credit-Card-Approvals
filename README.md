# Predicting credit card approvals

## Project description
Commercial banks receive a lot of applications for credit cards. Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit report, for example. Manually analyzing these applications is mundane, error-prone, and time-consuming (and time is money!). Luckily, this task can be automated with the power of machine learning and pretty much every commercial bank does so nowadays. This project builds an automatic credit card approval predictor using machine learning techniques.

## Technologies used
1. Python
2. Data manipulation
3. Machine Learning


## Dataset
The dataset used in this project is the Credit Card Approval dataset from the UCI Machine Learning Repository. (http://archive.ics.uci.edu/ml/datasets/credit+approval)

## Project Tasks
### 1. Load the applications
   The number of applications are **690** and each application has **16** different features. To protect the privacy of the customer, all the features has been anonymized.
### 2. Inspect the applications
   Inspect the numerical and categorical features, statistical summary and any missing values in the dataset.
### 3. Handle misssing data
   For numeric features **mean imputation** is used to fill in the missing data and for categorical features the most frequent values are used to fill the missing values.
### 4. Preprocessing the data
   1. Convert the non-numeric data into numeric using **Label Encoding**
### 5. Split the dataset into train and test sets
   1. Perform **feature selection** to use the best features.
   2. Split the data into train and test sets
### 6. Scale the data
   1. Scale the data to avoid the significant effect of large values on the predictive model.
### 7. Fit the model
   1. Fit the **Logistic Regression** model to the training set
### 8. Make predictions and evaluate the performance
   1. The classifier predicted whether an application get approved or not with an accuracy of **84%** given some information of the person.
### 9. The best performing model
   1. In order to make the model better perform, **GridSearchCV** is used with 5-fold **cross-validation**.
   2. Improved the accuracy of the model to around **86%**

