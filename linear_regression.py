# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:04:32 2018

@author: MITESH KUMAR
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#dataset
dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1:].values

#split train and test data
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


#Fitting into LinearRegression
from sklearn.linear_model import LinearRegression
clf=LinearRegression()
clf.fit(X_train,y_train)

#Visualising train Data
plt.scatter(X_train,y_train,color="red")
plt.plot(X_train,clf.predict(X_train),color='blue')
plt.title("Experience vs salary")
plt.xlabel('Experience')
plt.ylabel('Salary')

#Visualising test Data
plt.scatter(X_test,y_test,color="green")
plt.plot(X_test,clf.predict(X_test),color='blue')
plt.title("Experience vs salary")
plt.xlabel('Experience')
plt.ylabel('Salary')














