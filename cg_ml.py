# -*- coding: utf-8 -*-
"""cg_ml.ipynb

Automatically generated by Colaboratory.

"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix#for visualizing tree

"""Read the data"""

data = pd.read_csv("deletion.tsv.gz", delimiter='\t')

data

"""drop unwanted colums"""

data = data.drop(['chr_start_end', 'id'], axis=1)

"""split data to labeled, unlabeled"""

unmarked_data = data[np.isnan(data["status"])]
marked_data = data[data['status'].notnull()]
unmarked_data = unmarked_data.drop(['status'], axis=1)
target = marked_data['status']
marked_data = marked_data.drop(['status'], axis=1)

"""split data to train and test"""

X_train, X_test, y_train, y_test = train_test_split(marked_data, target, stratify = target, random_state=420)

"""Naive Bayes model and accuracy

"""

from sklearn.metrics import accuracy_score
nb = GaussianNB()
nb.fit(X_train, y_train)
target_pred_nb = nb.predict(X_test)

print("Classification report - \n", classification_report(y_test,target_pred_nb))
print('accuracy score ', accuracy_score(y_test, target_pred_nb, normalize = True))

"""Decission tree model"""

dtree=DecisionTreeClassifier(criterion='entropy',max_depth=6,min_samples_split=3,)
dtree.fit(X_train,y_train)

target_pred_dtree = dtree.predict(X_test)
print("Classification report - \n", classification_report(y_test,target_pred_dtree))
print('accuracy score ', accuracy_score(y_test, target_pred_dtree, normalize = True))

"""Tree Visualization"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
# %matplotlib inline
plt.figure(figsize=(70,40))
plot_tree(dtree, filled=True, fontsize=14)

"""Random Forest model"""

from sklearn.ensemble import RandomForestClassifier

# Create the model with 100 trees
RFmodel = RandomForestClassifier(n_estimators=100, 
                               bootstrap = True,
                               max_features = 'sqrt')
# Fit on training data
RFmodel.fit(X_train, y_train)

target_pred_RFmodel = RFmodel.predict(X_test)

print("Classification report - \n", classification_report(y_test,target_pred_RFmodel))
print('accuracy score ', accuracy_score(y_test, target_pred_RFmodel, normalize = True))



