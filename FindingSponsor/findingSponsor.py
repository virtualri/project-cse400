# Finding the sponsor from employee list
#
# CSE 400 - Dissertation: Implementation and Results
# Student    : Rashadul Islam
# Id         : 0301175301
# Department : Department of CSE
# Semester   : Spring 2019
# Written on : Wed Sep 10 10:00:00 BST 2019
#

# Library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Import Dataset as train and test as input
train = pd.read_csv("sales-per-employee.csv")
test = pd.read_csv("employee.csv")

# Preparing Dataset
number = preprocessing.LabelEncoder()

# Based on OEE_score finding the most possible sponsor from the employees
train["OEE_score"] = np.sqrt(train["OEE_score"])
test["OEE_score"] = np.sqrt(test["OEE_score"])

test["Profit"] = 0

combi = train.append(test)

col = ["Room_Status"]
for i in col:
    combi[i] = number.fit_transform(combi[i].astype("str"))
    combi[i] = combi[i].astype("object")

train = combi[: train.shape[0]]
test = combi[train.shape[0] :]
test.drop("Profit", axis=1, inplace=True)

# dataset preparation for tpot
tpot_train = train.drop(["Employee id"], axis=1)
tpot_test = test.drop(["Employee id"], axis=1)
tpot_train = train.drop(["Employee name", "Room_Status"], axis=1)
tpot_test = test.drop(["Employee name", "Room_Status"], axis=1)
target = tpot_train["Profit"]
tpot_train.drop("Profit", axis=1, inplace=True)

# To automate the machine learning
# to optimizes machine learning pipelines using genetic programming
# through optimization

from tpot import TPOTRegressor
from tpot import TPOTClassifier

X_train, X_test, y_train, y_test = train_test_split(
    tpot_train, target, train_size=0.8, test_size=0.2
)

# Genetic Algorithm
# to find the model
# please insert as more generations and population size to get the
# appropriate Cross Validation (C V) Score for model validation

# Pipeline optimizer

# to get the sample estimate model faster
# tpot = TPOTRegressor(generations=10, population_size=100, verbosity=3)

# most suitable optimizer
#tpot = TPOTRegressor(verbosity=3, cv=5)

tpot = TPOTRegressor(verbosity=3, 
 generations=500,
 population_size=100)

# Learning and predicting
tpot.fit(X_train, y_train)

# Estimate error or loss
print("Cross validation score")
print(tpot.score(X_test, y_test))

# Prediction
tpot_pred = tpot.predict(tpot_test)

# Results
final = pd.DataFrame(data=tpot_pred)
final = final.rename(columns={"0": "Profit"})
final["Employee id"] = test["Employee id"]
final["Employee name"] = test["Employee name"]
final["OEE_score"] = test["OEE_score"]
final["Client_Stays"] = test["Client_Stays"]
final["Room_Status"] = test["Room_Status"]
final.columns = [
    "Profit",
    "Employee id",
    "Employee name",
    "OEE_score",
    "Client_Stays",
    "Room_Status",
]
final.sort_values(by=["OEE_score"], ascending=False)

# Sponsor details based on possible sales over the client as profit
final["Sponsor"] = final.loc[final[["Profit", "OEE_score"]].idxmax()[1]]
print (final)

# Sponsor may be
print (final.loc[final[["Profit", "OEE_score"]].idxmax()[1]])
