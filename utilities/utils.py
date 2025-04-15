import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def load_data(path):
    return pd.read_csv(path)

def preprocess(df):
    # example: remove NaNs, convert columns, etc.
    return df.dropna()

def train_model(X_train, y_train):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    return model.score(X_test, y_test)
