#!/usr/bin/python 

""" 
    skeleton code for k-means clustering mini-project

"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than 4 clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

max_stock_option = 0
min_stock_option = 1000000000
max_salary = 0
min_salary = 100000000000
for item in data_dict:
    data =  data_dict.get(item)
    if data["exercised_stock_options"] == "NaN":
        continue
    else:
        if data["exercised_stock_options"] > max_stock_option:
            max_stock_option = data["exercised_stock_options"]
        if data["exercised_stock_options"] < min_stock_option:
            min_stock_option = data["exercised_stock_options"]
    if data["salary"] == "NaN":
        continue
    else:
        if data["salary"] > max_salary:
            max_salary = data["salary"]
        if data["salary"] < min_salary:
            min_salary = data["salary"]

print max_salary, min_salary
print max_stock_option, min_stock_option

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, line below assumes 2 features)
for f1, f2, _ in finance_features:
    plt.scatter( f1, f2 )
plt.show()



from sklearn.cluster import KMeans
features_list = ["poi", feature_1, feature_2, feature_3]
data2 = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data2 )


clf = KMeans(n_clusters=2)
pred = clf.fit_predict( finance_features )
Draw(pred, finance_features, poi, name="clusters_before_scaling.pdf", f1_name=feature_1, f2_name=feature_2)


### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
features_list = ["poi", feature_1, feature_2, feature_3]
data2 = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data2 )

from sklearn import preprocessing
min_max_scaler_1 = preprocessing.MinMaxScaler()
min_max_scaler_2 = preprocessing.MinMaxScaler()

feature_1_values = [ x[0] for x in finance_features]
feature_2_values = [ x[1] for x in finance_features]

min_max_scaler_1.fit(feature_1_values)
min_max_scaler_2.fit(feature_2_values)

for item in finance_features:
    item[0] = min_max_scaler_1.transform([item[0]])
    item[1] = min_max_scaler_2.transform([item[1]])

print min_max_scaler_1.transform([float(200000)])
print min_max_scaler_2.transform([float(1000000)])

clf = KMeans(n_clusters=2)
pred = clf.fit_predict( finance_features )

try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"




