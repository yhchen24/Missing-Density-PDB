from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
import pandas as pd
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
