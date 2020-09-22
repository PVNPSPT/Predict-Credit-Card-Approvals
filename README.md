# Predict-Credit-Card-Approvals

## Introduction
Commercial banks receive a lot of applications for credit cards. Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit report, for example. Manually analyzing these applications is mundane, error-prone, and time-consuming (and time is money!). Luckily, this task can be automated with the power of machine learning and pretty much every commercial bank does so nowadays. This project builds an automatic credit card approval predictor using machine learning techniques.

## Prerequisites
Supervised Learning with scikit-learn
Data Manipulation with pandas

## Dataset
The dataset used in this project is the Credit Card Approval dataset from the UCI Machine Learning Repository. (http://archive.ics.uci.edu/ml/datasets/credit+approval)

## Project Tasks
### 1. Load the applications
    1. The number of applications are **690** and each application has 16 different features. To protect the privacy of the customer, all the features has been anonymized.
### 2. Inspect the applications
    1. Inspect the numerical and categorical features, statistical summary and any missing values in the dataset.
### 3. Handle misssing data
    1. For numeric features mean imputation is used to fill in the missing data and for categorical features the most frequent values are used to fill the missing values.
### 4. Preprocessing the data
    1. Convert the non-numeric data into numeric.
    2. Split the data into train and test sets.
    3. Scale the feature values to a uniform range.



