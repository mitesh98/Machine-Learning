# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:14:59 2018

@author: MITESH KUMAR
"""

import numpy as np
import matplotlib.pyplot
import pandas as pd

dataset=pd.read_csv("Data.csv")
#all rows and all column except last
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:,-1:].values

#Missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

#Encode text categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])

#converting into only 0 and 1
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()

# yes/no into 0 and 1
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)

#Splitting the dataset into Training set and Test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

#we use the scaling paramaters learned on the train data










