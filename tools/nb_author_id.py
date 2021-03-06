#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from class_vis import prettyPicture, output_image
from time import time
sys.path.append("/")
from email_preprocess import preprocess
# from class_vis import prettyPicture, output_image

# ## features_train and features_test are the features for the training
# ## and testing datasets, respectively
# ## labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.naive_bayes import GaussianNB


clf = GaussianNB()

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score


print pred


accuracy = accuracy_score(labels_test, pred)

print accuracy



# prettyPicture(clf, features_test, labels_test)
# output_image("test.png", "png", open("test.png", "rb").read())
#########################################################

