import pandas as pd 
from sklearn.linear_model import LogisticRegression
import joblib
import mlflow
import mlflow.sklearn
import shutil


def load_and_process_data(data_path = "https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv")

    df = pd.read_csv(data_path)

    X = df.drop(['label'], axis=1)
    y = df['label']

    model = LogisticRegression(penalty='l1')

    model.fit(X, y)

    # joblib.dump(model, 'test_model.sav')
    mlflow.sklearn.save_model(model, 'test_model')