import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def bmi_prediction(age):
    dataset = pd.read_csv('/Users/medalist/opt/anaconda3/envs/mlproject/insurance.csv')
    dataset.head()

    X = dataset.iloc[: , 0].values.reshape(-1, 1)
    Y = dataset.iloc[:, 2].values.reshape(-1, 1)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=0)

    model = LinearRegression()
    model.fit(X_train, Y_train)
    X_test = np.array(age)
    X_test = X_test.reshape((1,-1))

    return model.predict(X_test)[0]









