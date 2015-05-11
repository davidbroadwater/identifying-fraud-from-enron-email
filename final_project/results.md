GaussianNB()
    Accuracy: 0.23070   Precision: 0.17502  Recall: 0.76650 F1: 0.28497 F2: 0.45737
    Total predictions: 10000    True positives: 1533    False positives: 7226   False negatives:  467   True negatives:  774

[Finished in 2.4s]

Features used: ['poi', 'total_payments', 'restricted_stock']
GaussianNB()
    Accuracy: 0.76371   Precision: 0.07752  Recall: 0.06000 F1: 0.06764 F2: 0.06284
    Total predictions: 14000    True positives:  120    False positives: 1428   False negatives: 1880   True negatives: 10572

[Finished in 2.0s]

Features used: ['poi', 'exercised_stock_options', 'long_term_incentive']
GaussianNB()
    Accuracy: 0.21867   Precision: 0.14497  Recall: 0.75300 F1: 0.24314 F2: 0.40951
    Total predictions: 12000    True positives: 1506    False positives: 8882   False negatives:  494   True negatives: 1118

[Finished in 2.6s]

Features used: ['poi', 'exercised_stock_options', 'restricted_stock']
GaussianNB()
    Accuracy: 0.20446   Precision: 0.13082  Recall: 0.73900 F1: 0.22229 F2: 0.38294
    Total predictions: 13000    True positives: 1478    False positives: 9820   False negatives:  522   True negatives: 1180

[Finished in 2.0s]

AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None)
    Accuracy: 0.71390   Precision: 0.17362  Recall: 0.11450 F1: 0.13799 F2: 0.12287
    Total predictions: 10000    True positives:  229    False positives: 1090   False negatives: 1771   True negatives: 6910

[Finished in 41.7s]

Features used: ['poi', 'salary', 'total_stock_value']
AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None)
    Accuracy: 0.78131   Precision: 0.16361  Recall: 0.10250 F1: 0.12604 F2: 0.11077
    Total predictions: 13000    True positives:  205    False positives: 1048   False negatives: 1795   True negatives: 9952

[Finished in 41.4s]

Features used: ['poi', 'salary', 'bonus']
AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None)
    Accuracy: 0.73910   Precision: 0.30740  Recall: 0.24300 F1: 0.27143 F2: 0.25363
    Total predictions: 10000    True positives:  486    False positives: 1095   False negatives: 1514   True negatives: 6905

[Finished in 36.4s]

# Max Values

The max value for total_payments is:            103559793.0
The max value for loan_advances is:             81525000.0
The max value for total_stock_value is:         49110078.0
The max value for exercised_stock_options is:   34348384.0
The max value for restricted_stock is:          14761694.0
The max value for bonus is:                     8000000.0
The max value for long_term_incentive is:       5145434.0
The max value for deferral_payments is:         6426990.0
The max value for salary is:                    1111258.0
The max value for to_messages is:               15149.0
The max value for from_poi_to_this_person is:   528.0
The max value for from_messages is:             14368.0
The max value for from_this_person_to_poi is:   609.0
The max value for shared_receipt_with_poi is:   5521.0
The max value for deferred_income is:           0.0

# Financial Feature Coverage

Coverage for total_payments             [0.86, 0.84, 1.0]*
Coverage for total_stock_value          [0.86, 0.84, 1.0]*
Coverage for restricted_stock           [0.75, 0.73, 0.94]**
Coverage for exercised_stock_options    [0.7, 0.7, 0.67]**
Coverage for salary                     [0.65, 0.61, 0.94]**
Coverage for bonus                      [0.56, 0.52, 0.89]**
Coverage for long_term_incentive        [0.45, 0.42, 0.67]**
Coverage for deferred_income            [0.34, 0.3, 0.61]
Coverage for deferral_payments          [0.27, 0.27, 0.28]*
Coverage for loan_advances              [0.03, 0.02, 0.06]

Too much POI coverage:
Coverage for expenses                   [0.65, 0.6, 1.0]
Coverage for other                      [0.64, 0.59, 1.0]

Insufficient POI Coverage:
Coverage for restricted_stock_deferred  [0.12, 0.14, 0.0]
Coverage for director_fees              [0.12, 0.13, 0.0]



# Email Feature Coverage

Coverage for poi                        [1.0, 1.0, 1.0]**
Coverage for to_messages                [0.59, 0.56, 0.78]**
Coverage for from_poi_to_this_person    [0.59, 0.56, 0.78]**
Coverage for from_messages              [0.59, 0.56, 0.78]**
Coverage for from_this_person_to_poi    [0.59, 0.56, 0.78]**
Coverage for shared_receipt_with_poi    [0.59, 0.56, 0.78]**

Too much POI coverage:
Coverage for email_address              [0.76, 0.73, 1.0]

[Finished in 0.2s]

# Feature SelectKBest f_classif ANOVA scores:

exercised_stock_options             25.3801052998
bonus                               21.327890414
fractional_bonus                    21.2620834165
salary                              18.8617953165
fraction_to_poi                     16.8738702646
fractional_long_term_incentive      14.1772818163
deferred_income                     11.7326980761
long_term_incentive                 10.2229042058
fraction_shared_receipt_with_poi    9.49145795071
loan_advances                       7.30140665154
restricted_stock                    9.48074320348
shared_receipt_with_poi             8.90382155717*
from_poi_to_this_person             5.44668748333
fraction_from_poi                   3.29382863203
fractional_salary                   2.85912570107
from_this_person_to_poi             2.47052122266
to_messages                         1.75169427903
fractional_restricted_stock         1.20846709097
deferral_payments                   0.20970584227
from_messages                       0.158770239213
fractional_exercised_stock_options  0.0157018942358

# DecisionTree Feature Importances

exercised_stock_options             0.200157604413
shared_receipt_with_poi             0.177984330906
fraction_to_poi                     0.13649901634
fractional_bonus                    0.119228517488
fractional_restricted_stock         0.0978094649933
fraction_from_poi                   0.0966545848436
salary                              0.0422863808691
long_term_incentive                 0.0422863808691
from_poi_to_this_person             0.0422863808691
restricted_stock                    0.0281948316394
fractional_salary                   0.01661250677
bonus                               0.0
deferred_income                     0.0
deferral_payments                   0.0
loan_advances                       0.0
fractional_long_term_incentive      0.0
fractional_exercised_stock_options  0.0
to_messages                         0.0
from_messages                       0.0
from_this_person_to_poi             0.0
fraction_shared_receipt_with_poi    0.0

# Pipeline Optimized (f1) Gaussian Naive Bayes with KBest

Pipeline(steps=[('anova', SelectKBest(k=6, score_func=<function f_classif at 0x105d5e8c0>)), ('clf', GaussianNB())])
    Accuracy: 0.84053   Precision: 0.38389  Recall: 0.32400 F1: 0.35141 F2: 0.33443
    Total predictions: 15000    True positives:  648    False positives: 1040   False negatives: 1352   True negatives: 11960

[Finished in 2.1s]

Pipeline(steps=[('anova', SelectKBest(k=12, score_func=<function f_classif at 0x105d609b0>)), ('clf', GaussianNB())])
    Accuracy: 0.85073   Precision: 0.42422  Recall: 0.33450 F1: 0.37406 F2: 0.34927
    Total predictions: 15000    True positives:  669    False positives:  908   False negatives: 1331   True negatives: 12092

[Finished in 2.2s]

Pipeline(steps=[('anova', SelectKBest(k=11, score_func=<function f_classif at 0x105d5e9b0>)), ('clf', GaussianNB())])
    Accuracy: 0.85013   Precision: 0.42269  Recall: 0.33900 F1: 0.37625 F2: 0.35298
    Total predictions: 15000    True positives:  678    False positives:  926   False negatives: 1322   True negatives: 12074

[Finished in 41.5s]

# Pipeline Optimized (f1) Gaussian Naive Bayes with KBest and PCA

Pipeline(steps=[('anova', SelectKBest(k=8, score_func=<function f_classif at 0x105c588c0>)), ('pca', PCA(copy=True, n_components=None, whiten=True)), ('clf', GaussianNB())])
    Accuracy: 0.81753   Precision: 0.30837  Recall: 0.29650 F1: 0.30232 F2: 0.29880
    Total predictions: 15000    True positives:  593    False positives: 1330   False negatives: 1407   True negatives: 11670

[Finished in 2.6s]

Pipeline(steps=[('anova', SelectKBest(k=18, score_func=<function f_classif at 0x105c5e9b0>)), ('pca', PCA(copy=True, n_components=None, whiten=True)), ('clf', GaussianNB())])
    Accuracy: 0.77887   Precision: 0.24702  Recall: 0.32150 F1: 0.27938 F2: 0.30322
    Total predictions: 15000    True positives:  643    False positives: 1960   False negatives: 1357   True negatives: 11040

[Finished in 2.8s]

Pipeline(steps=[('anova', SelectKBest(k=11, score_func=<function f_classif at 0x105c5c9b0>)), ('pca', PCA(copy=True, n_components=None, whiten=True)), ('clf', GaussianNB())])
    Accuracy: 0.81453   Precision: 0.31712  Recall: 0.33900 F1: 0.32769 F2: 0.33439
    Total predictions: 15000    True positives:  678    False positives: 1460   False negatives: 1322   True negatives: 11540

[Finished in 49.7s]

Pipeline(steps=[('anova', SelectKBest(k=11, score_func=<function f_classif at 0x105d609b0>)), ('pca', PCA(copy=True, n_components=8, whiten=True)), ('clf', GaussianNB())])
    Accuracy: 0.83547   Precision: 0.37241  Recall: 0.34150 F1: 0.35629 F2: 0.34726
    Total predictions: 15000    True positives:  683    False positives: 1151   False negatives: 1317   True negatives: 11849

[Finished in 28.4s]

# Pipeline Optimized (f1) Decision Tree with KBest

Pipeline(steps=[('anova', SelectKBest(k=4, score_func=<function f_classif at 0x105d5a8c0>)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='gini',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=2,
            random_state=None, splitter='best'))])
    Accuracy: 0.80467   Precision: 0.27558  Recall: 0.28550 F1: 0.28045 F2: 0.28346
    Total predictions: 15000    True positives:  571    False positives: 1501   False negatives: 1429   True negatives: 11499

[Finished in 2.9s]


Pipeline(steps=[('anova', SelectKBest(k=16, score_func=<function f_classif at 0x105e5f9b0>)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='entropy',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=30,
            random_state=None, splitter='best'))])
    Accuracy: 0.83693   Precision: 0.39461  Recall: 0.41750 F1: 0.40573 F2: 0.41271
    Total predictions: 15000    True positives:  835    False positives: 1281   False negatives: 1165   True negatives: 11719

[Finished in 649.0s]

Pipeline(steps=[('anova', SelectKBest(k=16, score_func=<function f_classif at 0x105d5c9b0>)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='entropy',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=30,
            random_state=None, splitter='best'))])
    Accuracy: 0.83807   Precision: 0.39858  Recall: 0.42150 F1: 0.40972 F2: 0.41671
    Total predictions: 15000    True positives:  843    False positives: 1272   False negatives: 1157   True negatives: 11728

[Finished in 3.5s]

Pipeline(steps=[('anova', SelectKBest(k=16, score_func=<function f_classif at 0x105d5f9b0>)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='entropy',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=30,
            random_state=None, splitter='best'))])
    Accuracy: 0.83687   Precision: 0.39443  Recall: 0.41750 F1: 0.40564 F2: 0.41267
    Total predictions: 15000    True positives:  835    False positives: 1282   False negatives: 1165   True negatives: 11718

[Finished in 3.2s]

Pipeline(steps=[('anova', SelectKBest(k=16, score_func=<function f_classif at 0x105d5f9b0>)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='entropy',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=30,
            random_state=42, splitter='best'))])
    Accuracy: 0.83840   Precision: 0.39972  Recall: 0.42250 F1: 0.41079 F2: 0.41774
    Total predictions: 15000    True positives:  845    False positives: 1269   False negatives: 1155   True negatives: 11731

[Finished in 2.6s]

Pipeline(steps=[('anova', SelectKBest(k=15, score_func=<function f_classif at 0x105d609b0>)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='entropy',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=30,
            random_state=42, splitter='best'))])
    Accuracy: 0.83980   Precision: 0.40446  Recall: 0.42650 F1: 0.41519 F2: 0.42190
    Total predictions: 15000    True positives:  853    False positives: 1256   False negatives: 1147   True negatives: 11744

[Finished in 2.5s]

DecisionTreeClassifier(compute_importances=None, criterion='entropy',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=30,
            random_state=42, splitter='best')
    Accuracy: 0.86073   Precision: 0.48093  Recall: 0.56100 F1: 0.51789 F2: 0.54292
    Total predictions: 15000    True positives: 1122    False positives: 1211   False negatives:  878   True negatives: 11789

[Finished in 1.7s]

# Pipeline Optimized (f1) Decision Tree with KBest and PCA

Pipeline(steps=[('anova', SelectKBest(k=13, score_func=<function f_classif at 0x105d5d8c0>)), ('pca', PCA(copy=True, n_components=None, whiten=False)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='gini',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=2,
            random_state=None, splitter='best'))])
    Accuracy: 0.81413   Precision: 0.30061  Recall: 0.29700 F1: 0.29879 F2: 0.29771
    Total predictions: 15000    True positives:  594    False positives: 1382   False negatives: 1406   True negatives: 11618

[Finished in 4.9s]

Pipeline(steps=[('anova', SelectKBest(k=15, score_func=<function f_classif at 0x105d609b0>)), ('pca', PCA(copy=True, n_components=None, whiten=False)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='gini',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=20,
            random_state=None, splitter='best'))])
    Accuracy: 0.84087   Precision: 0.39546  Recall: 0.36600 F1: 0.38016 F2: 0.37154
    Total predictions: 15000    True positives:  732    False positives: 1119   False negatives: 1268   True negatives: 11881

[Finished in 1702.8s]

Pipeline(steps=[('anova', SelectKBest(k=15, score_func=<function f_classif at 0x105c5e9b0>)), ('pca', PCA(copy=True, n_components=11, whiten=True)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='gini',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=20,
            random_state=42, splitter='best'))])
    Accuracy: 0.84620   Precision: 0.41391  Recall: 0.36900 F1: 0.39017 F2: 0.37718
    Total predictions: 15000    True positives:  738    False positives: 1045   False negatives: 1262   True negatives: 11955

Pipeline(steps=[('anova', SelectKBest(k=15, score_func=<function f_classif at 0x105e989b0>)), ('pca', PCA(copy=True, n_components=12, whiten=True)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='gini',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=20,
            random_state=42, splitter='best'))])
    Accuracy: 0.84380   Precision: 0.40634  Recall: 0.37200 F1: 0.38841 F2: 0.37839
    Total predictions: 15000    True positives:  744    False positives: 1087   False negatives: 1256   True negatives: 11913

[Finished in 269.3s]

# Decision Tree

DecisionTreeClassifier(compute_importances=None, criterion='entropy',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=30,
            random_state=42, splitter='best')
    Accuracy: 0.86073   Precision: 0.48093  Recall: 0.56100 F1: 0.51789 F2: 0.54292
    Total predictions: 15000    True positives: 1122    False positives: 1211   False negatives:  878   True negatives: 11789

[Finished in 1.9s]

# Decision Tree with PCA

Pipeline(steps=[('pca', PCA(copy=True, n_components=6, whiten=False)), ('clf', DecisionTreeClassifier(compute_importances=None, criterion='entropy',
            max_depth=None, max_features=None, max_leaf_nodes=None,
            min_density=None, min_samples_leaf=1, min_samples_split=30,
            random_state=42, splitter='best'))])
    Accuracy: 0.84440   Precision: 0.23742  Recall: 0.07550 F1: 0.11457 F2: 0.08742
    Total predictions: 15000    True positives:  151    False positives:  485   False negatives: 1849   True negatives: 12515

[Finished in 13.5s]

# Pipeline Optimized (f1) Adaboost with KBest

Pipeline(steps=[('anova', SelectKBest(k=9, score_func=<function f_classif at 0x105c5c8c0>)), ('clf', AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=200, random_state=None))])
    Accuracy: 0.83000   Precision: 0.32417  Recall: 0.25350 F1: 0.28451 F2: 0.26506
    Total predictions: 15000    True positives:  507    False positives: 1057   False negatives: 1493   True negatives: 11943

[Finished in 185.7s]

Pipeline(steps=[('anova', SelectKBest(k=10, score_func=<function f_classif at 0x105e65a28>)), ('clf', AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None))])
    Accuracy: 0.84060   Precision: 0.36452  Recall: 0.26300 F1: 0.30555 F2: 0.27851
    Total predictions: 15000    True positives:  526    False positives:  917   False negatives: 1474   True negatives: 12083

# Pipeline Optimized (f1) Adaboost with KBest and PCA

Pipeline(steps=[('anova', SelectKBest(k=11, score_func=<function f_classif at 0x105c5c8c0>)), ('pca', PCA(copy=True, n_components=None, whiten=True)), ('clf', AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=200, random_state=None))])
    Accuracy: 0.84053   Precision: 0.35818  Recall: 0.24750 F1: 0.29273 F2: 0.26380
    Total predictions: 15000    True positives:  495    False positives:  887   False negatives: 1505   True negatives: 12113

[Finished in 214.2s]

Pipeline(steps=[('anova', SelectKBest(k=2, score_func=<function f_classif at 0x105d65a28>)), ('pca', PCA(copy=True, n_components=None, whiten=True)), ('clf', AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None,
          learning_rate=1.0, n_estimators=50, random_state=None))])
    Accuracy: 0.83580   Precision: 0.34997  Recall: 0.27000 F1: 0.30483 F2: 0.28293
    Total predictions: 15000    True positives:  540    False positives: 1003   False negatives: 1460   True negatives: 11997

# Pipeline Optimized (f1) SVM with KBest

Pipeline(steps=[('anova', SelectKBest(k=18, score_func=<function f_classif at 0x105d608c0>)), ('clf', SVC(C=5000.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
  gamma=0.0001, kernel='linear', max_iter=-1, probability=False,
  random_state=None, shrinking=True, tol=0.001, verbose=False))])
    Accuracy: 0.85313   Precision: 0.41406  Recall: 0.24450 F1: 0.30745 F2: 0.26631
    Total predictions: 15000    True positives:  489    False positives:  692   False negatives: 1511   True negatives: 12308

[Finished in 777.0s]

# Pipeline Optimized (f1) SVM with KBest and PCA

Pipeline(steps=[('anova', SelectKBest(k=18, score_func=<function f_classif at 0x105c619b0>)), ('pca', PCA(copy=True, n_components=None, whiten=True)), ('clf', SVC(C=5000, cache_size=200, class_weight=None, coef0=0.0, degree=3,
  gamma=0.0001, kernel='linear', max_iter=-1, probability=False,
  random_state=None, shrinking=True, tol=0.001, verbose=False))])
    Accuracy: 0.82620   Precision: 0.25385  Recall: 0.15650 F1: 0.19363 F2: 0.16950
    Total predictions: 15000    True positives:  313    False positives:  920   False negatives: 1687   True negatives: 12080

[Finished in 7089.6s]

# KBest=9 with Optimized SVM:

Pipeline(steps=[('anova', SelectKBest(k=9, score_func=<function f_classif at 0x105d618c0>)), ('clf', SVC(C=10, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.1,
  kernel='rbf', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False))])
    Accuracy: 0.88053   Precision: 0.92623  Recall: 0.11300 F1: 0.20143 F2: 0.13707
    Total predictions: 15000    True positives:  226    False positives:   18   False negatives: 1774   True negatives: 12982
[Finished in 78.7s]

# KBest=9 with Optimized SVM and PCA:

Pipeline(steps=[('anova', SelectKBest(k=9, score_func=<function f_classif at 0x105d5f8c0>)), ('pca', PCA(copy=True, n_components=None, whiten=True)), ('clf', SVC(C=10, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.01,
  kernel='poly', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False))])
    Accuracy: 0.87973   Precision: 0.87121  Recall: 0.11500 F1: 0.20318 F2: 0.13916
    Total predictions: 15000    True positives:  230    False positives:   34   False negatives: 1770   True negatives: 12966
[Finished in 1950.8s]

# Pipeline Optimized SVM with KBest

Pipeline(steps=[('anova', SelectKBest(k=8, score_func=<function f_classif at 0x105d618c0>)), ('clf', SVC(C=10, cache_size=200, class_weight=None, coef0=0.0, degree=3, gamma=0.1,
  kernel='rbf', max_iter=-1, probability=False, random_state=None,
  shrinking=True, tol=0.001, verbose=False))])
    Accuracy: 0.87780   Precision: 0.91960  Recall: 0.09150 F1: 0.16644 F2: 0.11160
    Total predictions: 15000    True positives:  183    False positives:   16   False negatives: 1817   True negatives: 12984

[Finished in 1004.7s]

# Pipeline Optimized (Recall) SVM with KBest

Pipeline(steps=[('anova', SelectKBest(k=18, score_func=<function f_classif at 0x105d5a8c0>)), ('clf', SVC(C=5000.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
  gamma=0.0001, kernel='linear', max_iter=-1, probability=False,
  random_state=None, shrinking=True, tol=0.001, verbose=False))])
    Accuracy: 0.85313   Precision: 0.41406  Recall: 0.24450 F1: 0.30745 F2: 0.26631
    Total predictions: 15000    True positives:  489    False positives:  692   False negatives: 1511   True negatives: 12308

[Finished in 1191.3s]
