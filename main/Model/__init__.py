#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:53:34 2021
@author: Mounir
"""

import pandas
import matplotlib.pyplot as plt
import numpy
from sklearn.svm._libsvm import predict_proba

dataset = pandas.read_csv('~/.config/spyder-py3/exemplaires.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
#%%

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
#%%

# Feature Scaling improve the model performance for Logistic Regression.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
#%%

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()

target = "speciality"


classifier.fit(X_train, y_train)
#%%
# There are also predict_proba and predict_log_proba methods.

y_predicted = classifier.predict_proba(X_test)
#%%
# numpy.set_printoptions(precision=2)  # Not needed.
# print(numpy.concatenate((y_predicted.reshape(len(y_predicted), 1),
#                          y_test.reshape(len(y_test), 1)), 1))
numpy.set_printoptions(suppress=True)
print(classifier.classes_)
print(y_predicted)
# Predict one.
#print(classifier.predict(scaler.transform([[40, 87000]])))
#%%
# Evaluating the model using Confusion matrix.
from sklearn.metrics import confusion_matrix, accuracy_score
#cm = confusion_matrix(y_test, y_predicted)
#print(cm)
#accuracy = accuracy_score(y_test, y_predicted)

#print(accuracy)