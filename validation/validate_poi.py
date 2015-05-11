#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### it's all yours from here forward!  

from sklearn.cross_validation import train_test_split

### test_size is the percentage of events assigned to the test set (remainder go into training)
features_train, features_test, labels_train, labels_test = train_test_split(
	features, labels, test_size=0.3, random_state=42)



from time import time
from sklearn.tree import DecisionTreeClassifier
### create classifier
clf = DecisionTreeClassifier()

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
import numpy as np
# accuracy = accuracy_score(np.zeros(len(pred)), labels_test)
accuracy = accuracy_score(pred, labels_test)
print "accuracy:",accuracy

poi_count = 0
for item in pred:
	if item == 1:
		poi_count += 1
print "number of poi's predicted:", poi_count

print "number of people:", len(pred)

poi_count_test = 0
for item in labels_test:
	if item == 1:
		poi_count_test += 1
print "number of actual poi's:", poi_count_test

true_positives = 0
for i in range(len(pred)):
	if pred[i] == 1 and pred[i] == labels_test[i]:
		true_positives += 1
print "true positives:", true_positives

from sklearn.metrics import precision_score
precision = precision_score(pred, labels_test)
print "precision score:", precision

from sklearn.metrics import recall_score
recall = recall_score(pred, labels_test)
print "recall score:", recall