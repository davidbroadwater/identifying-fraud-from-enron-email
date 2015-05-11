#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
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

#########################################################
from sklearn.svm import SVC
clf = SVC(C=10000.0, kernel="rbf")

### Make training set smaller to improve performance
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

### fit the classifier on the training features and labels
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

### use the trained classifier to predict labels for the test features
t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print "Accuracy:", acc
#print "10th Prediction Element:", pred[10]
#print "26th Prediction Element:", pred[26]
#print "50th Prediction Element:", pred[50]

import numpy
print "Number of Emails by Chris:", numpy.size(pred[numpy.where( pred == 1.0 )])

'''
Initial Output:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 192.438 s
predicting time: 20.44 s
0.984072810011
[Finished in 218.2s]

Output for smaller training set:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 0.107 s
predicting time: 1.252 s
0.884527872582
[Finished in 6.4s]

Output for smaller training set with rbf kernel:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 0.14 s
predicting time: 1.374 s
0.616040955631
[Finished in 6.0s]

Output for smaller training set with rbf kernel and C=10:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 0.132 s
predicting time: 1.42 s
0.616040955631
[Finished in 6.6s]

Output for smaller training set with rbf kernel and C=100.0:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 0.131 s
predicting time: 1.328 s
0.616040955631
[Finished in 6.2s]

Output for smaller training set with rbf kernel and C=1000.0:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 0.127 s
predicting time: 1.325 s
0.821387940842
[Finished in 6.1s]

Output for smaller training set with rbf kernel and C=10000.0:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 0.118 s
predicting time: 1.03 s
0.892491467577
[Finished in 5.4s]

Output for full training set with rbf kernel and C=10000.0:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 127.568 s
predicting time: 12.381 s
0.990898748578
[Finished in 144.5s]

Output for smaller training set with rbf kernel and C=10000.0 for specific elements:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 0.126 s
predicting time: 1.142 s
Accuracy: 0.892491467577
10th Prediction Element: 1
26th Prediction Element: 0
50th Prediction Element: 1
[Finished in 6.5s]

Output for full training set with rbf kernel and C=10000.0 for emails classified as Chris:
no. of Chris training emails: 7936
no. of Sara training emails: 7884
training time: 130.481 s
predicting time: 12.178 s
Accuracy: 0.990898748578
Number of Emails by Chris: 877
[Finished in 147.2s]'''

