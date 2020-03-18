from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
# from mpl_toolkits import mplot3d
from sklearn.model_selection import train_test_split

seed = 23
size = 0.2


def medium_model():
    model = Sequential()
    model.add(Dense(96, input_dim=7, kernel_initializer='normal',
                    activation='relu'))
    model.add(Dense(48, kernel_initializer='normal', activation='relu'))
    model.add(Dense(24, kernel_initializer='normal', activation='relu'))
    model.add(Dense(12, kernel_initializer='normal', activation='relu'))
    model.add(Dense(6, kernel_initializer='normal', activation='relu'))
    model.add(Dense(3, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


def load_csv(filename):
    data = pd.read_csv('models/' + filename + '.csv')
    df1 = pd.DataFrame.dropna(data)
    X = df1[['b values', 'X pre', 'Y pre', 'Z pre', 'X post', 'Y post',
             'Z post']].values
    Y = df1[['X', 'Y', 'Z']].values
    return [X, Y]


def validation_split(filename, custom_size, custom_seed):
    global seed
    global size
    seed = custom_seed
    size = custom_size
    [X, Y] = load_csv(filename)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=size,
                                                        random_state=seed)
    return [X_train, X_test, y_train, y_test]


def run_model(filename):
    [X_train, X_test, y_train, y_test] = validation_split(filename, size,
                                                          seed)
    estimator = KerasRegressor(build_fn=medium_model, epochs=150,
                               batch_size=25000, verbose=0)
    history = estimator.fit(X_train, y_train, validation_split=0.20,
                            epochs=150, batch_size=10000, verbose=0)
    prediction = estimator.model.predict(X_test)
    return [history, prediction]


def validation_coord(filename):
    [X_train, X_test, y_train, y_test] = validation_split(filename, size,
                                                          seed)
    prediction = run_model(filename)[1]
    X_pred = []
    Y_pred = []
    Z_pred = []
    X_real = []
    Y_real = []
    Z_real = []
    for i in range(len(y_test)):
        X_pred.append(prediction[i][0])
        Y_pred.append(prediction[i][1])
        Z_pred.append(prediction[i][2])
        X_real.append(y_test[i][0])
        Y_real.append(y_test[i][1])
        Z_real.append(y_test[i][2])
    df2 = pd.DataFrame({'X pred': X_pred, 'Y pred': Y_pred, 'Z pred': Z_pred,
                        'X test': X_real, 'Y test': Y_real, 'Z test': Z_real})
    return df2


def get_mse(filename):
    history = run_model(filename)[0]
    print("final MSE for train is %.2f and for validation is %.2f" %
          (history.history['loss'][-1], history.history['val_loss'][-1]))


def plot_validation(filename):
    df2 = validation_coord(filename)
    [X_pred, Y_pred, Z_pred, X_real, Y_real, Z_real] = [df2['X pred'],
                                                        df2['Y pred'],
                                                        df2['Z pred'],
                                                        df2['X test'],
                                                        df2['Y test'],
                                                        df2['Z test']]
    min_val = min(min(X_pred), min(Y_pred), min(Z_pred), min(X_real),
                  min(Y_real), min(Z_real))
    max_val = max(max(X_pred), max(Y_pred), max(Z_pred), max(X_real),
                  max(Y_real), max(Z_real))
    plt.figure(figsize=(6, 6))
    plt.subplot()
    plt.plot(np.linspace(math.floor(min_val) - 5,
                         math.ceil(max_val) + 5,
                         1001),
             np.linspace(math.floor(min_val) - 5,
                         math.ceil(max_val) + 5,
                         1001),
             color='black', label='X = Y')
    plt.scatter(X_pred, X_real, label='X coordinate')
    plt.scatter(Y_pred, Y_real, label='Y coordinate')
    plt.scatter(Z_pred, Z_real, label='Z coordinate')
    plt.xlabel('$Predicted$ $Coordinate$', fontsize='16')
    plt.ylabel('$Real$ $Coordinate$', fontsize='16')
    plt.xlim([math.floor(min_val) - 5, math.ceil(max_val) + 5])
    plt.ylim([math.floor(min_val) - 5, math.ceil(max_val) + 5])
    plt.legend()
    plt.grid()


def plot_validation_atoms(filename):
    df2 = validation_coord(filename)
    [X_pred, Y_pred, Z_pred, X_real, Y_real, Z_real] = [df2['X pred'],
                                                        df2['Y pred'],
                                                        df2['Z pred'],
                                                        df2['X test'],
                                                        df2['Y test'],
                                                        df2['Z test']]
    plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    ax.scatter3D(X_pred, Y_pred, Z_pred, label='predicted atoms')
    ax.scatter3D(X_real, Y_real, Z_real, label='real atoms')
    ax.set_title('Atomes of Protein', fontsize='20')
    ax.set_xlabel('$X$', fontsize='14')
    ax.set_ylabel('$Y$', fontsize='14')
    ax.set_zlabel('$Z$', fontsize='14')
    ax.legend(fontsize='12')
    ax.view_init(elev=45, azim=60)
