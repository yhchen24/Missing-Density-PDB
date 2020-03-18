import pandas as pd
import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from collections import Counter


def build_own_model(csvfile):
    """
    This function is for building up own random forest model
    :param: csvfile, name of protein must be first column, and
    predict goal must be the second column
    :return: Output RF_model.pkl, list importance of each feature in the model
    """
    # dataset
    data = pd.read_csv(csvfile, index_col='Protein')
    df1 = pd.DataFrame.dropna(data)

    # x = features, y = predict goal(has_missing_residues)
    x, y = df1.iloc[:, 1:].values, df1.iloc[:, 0]
    # Random Forest Model, set 500 decision trees
    RF_model = RandomForestClassifier(n_estimators=500)
    # fitting your training data
    RF_model.fit(x, y)
    # output model
    joblib.dump(RF_model, 'RF_model.pkl')

    # List importance of each feature in the model
    # name of features
    feature_name = df1.columns[1:]
    # get importances
    importances = RF_model.feature_importances_
    # index of sort of importance
    indices = np.argsort(importances)[::-1]
    for i in range(x.shape[1]):
        print("%2d) %-*s %f" % (i + 1, 30, feature_name[indices[i]],
                                importances[indices[i]]))

    # 5-fold cross-validation
    from sklearn.model_selection import cross_val_score
    scores = cross_val_score(RF_model, x, y, cv=5)
    print('Accuracy of the prediction in 5-fold cross-validation = {:.2%}'.
          format(scores.mean()))


def get_reason_prediction(input_data):
    """
    Getting prediction that if you will get missing residues under this
    experiment conditions, and most used features of nodes that input
    data went through
    :return:
    """
    # load model
    RF_model = joblib.load('RandomForest_model.pkl')

    # prediction
    # get prediction of test data
    y_predict = RF_model.predict(input_data)
    print('Does this circumstance tend to have missing residues?', y_predict)

    # The path of single input data goes through the random forest model
    feature_count_accum = []
    for j, tree in enumerate(RF_model.estimators_):
        # matrix of nodes that input data go through(boolean)
        dense_matrix = tree.decision_path(input_data.reshape(1, -1)).todense()
        # transform to array
        dense_sample = np.array(dense_matrix)[0]
        # extract number of nodes that input data goes through
        node_position = np.where(dense_sample == 1)[0]
        feature_count = []

        for i in range(len(node_position)):
            number = node_position[i]
            # feature name of specific node got from node_position
            feature_count.append(feature_name[tree.tree_.feature[number]])
        feature_count_accum.extend(feature_count)
    # list
    feature_order = Counter(feature_count_accum).most_common(8)
    print('Most used features of nodes that input data went through',
          feature_order)
