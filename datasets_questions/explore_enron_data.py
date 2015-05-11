#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print len(enron_data)

# print len(enron_data["SKILLING JEFFREY K"])

# poi_count = 0
# for person in enron_data:
# 	if enron_data[person]["poi"] == True:
# 		poi_count += 1
# 	else:
# 		continue

# print poi_count

# print enron_data["PRENTICE JAMES"]["total_stock_value"]

# print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# print enron_data["SKILLING JEFFREY K"]["total_payments"]

# print enron_data["LAY KENNETH L"]["total_payments"]

# print enron_data["FASTOW ANDREW S"]["total_payments"]

# print enron_data["FASTOW ANDREW S"]

salary_count = 0
for person in enron_data:
	if enron_data[person]["salary"] == "NaN":
		continue
	else:
		salary_count += 1
print salary_count

email_count = 0
for person in enron_data:
	if enron_data[person]["email_address"] == "NaN":
		continue
	else:
		email_count += 1
print email_count

total_payments_exist_count = 0
for person in enron_data:
	if enron_data[person]["total_payments"] == "NaN":
		continue

print total_payments_exist_count

# total_payments_exist_poi_count = 0
# for person in enron_data:
# 	if enron_data[person]["total_payments"] != "NaN" and enron_data[person]["poi"] == True:
# 		total_payments_exist_poi_count += 1
# 	else if enron_data[person]["total_payments"] == "NaN":
# 		continue
# 	else:
# 		total_payments_exist_count += 1
# print total_payments_exist_poi_count


def data_coverage_checker(feature_name, input_data):

	counter = 0
	poi_counter = 0
	data_coverage = []
	feature_exist_poi = 0
	feature_exist_non_poi = 0
	for person in input_data:
		counter += 1
		if input_data[person]["poi"] == True:
			poi_counter += 1 
			if input_data[person][feature_name] != "NaN":
				feature_exist_poi += 1
			else:
				continue
		
		elif input_data[person][feature_name] == "NaN":
			continue
		else:
			feature_exist_non_poi += 1

	data_coverage.append(round(float(feature_exist_poi+feature_exist_non_poi)/float(counter),2))
	data_coverage.append(round(float(feature_exist_non_poi)/float(counter - poi_counter),2))
	data_coverage.append(round(float(feature_exist_poi)/float(poi_counter),2))


	return data_coverage


financial_features = ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 
	'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 
	'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 
	'director_fees']

email_features = ['to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages', 
	'from_this_person_to_poi', 'poi', 'shared_receipt_with_poi']

for feature in financial_features:
	print "Coverage for", feature, "\t", data_coverage_checker(feature, enron_data)

for feature in email_features:
	print "Coverage for", feature, data_coverage_checker(feature, enron_data)
