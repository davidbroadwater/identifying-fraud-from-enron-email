#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.tree import DecisionTreeClassifier
### create classifier
clf = DecisionTreeClassifier(min_samples_split=40)

### fit the classifier on the training features and labels
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

### use the trained classifier to predict labels for the test features
t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"


### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print accuracy

### Determine the number of features
print "number of features:", len(features_train[0])


#########################################################

''' 
Output using default values:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 118.075 s
predicting time: 0.076 s
0.992036405006
[Finished in 124.8s]

Output using min_samples_split=40:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 121.442 s
predicting time: 0.08 s
0.9795221843
[Finished in 126.8s]
'''


