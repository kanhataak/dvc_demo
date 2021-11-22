# load the train and test
# train algorithm
# save the matrixes, params

import os, sys, warnings, json, joblib
import argparse
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
from urllib.parse import urlparse 


def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]['test_path']
    train_data_path = config["split_data"]['train_path']
    random_state = config["base"]['random_state']

    model_dir =config["model_dir"]
    alpha = config["estimators"]['ElasticNet']["params"]["alpha"]
    l1_ratio = config["estimators"]['ElasticNet']["params"]["l1_ratio"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path,sep=",")

    train_y = train[target]
    test_y = test[target]
    train_x = train.drop(target, axis =1)
    test_x = test.drop(target, axis =1)

    lr = ElasticNet(
        alpha=alpha,
        l1_ratio=l1_ratio,
        random_state=random_state)

    lr.fit(train_x, train_y) 
    predicted_qualities = lr.predict(test_x)
    mae = mean_absolute_error(test_y, predicted_qualities)
    mse = mean_squared_error(test_y, predicted_qualities)
    print("MAE: {}".format(mae))
    print("MSE: {}".format(mse))
    score_file = config['reports']["scores"]
    params_file = config['reports']['params']

    with open(score_file,"w") as f:
        score = {
            "mae": mae,
            "mse": mse
        }
        json.dump(score,f,indent=4)

    with open(params_file,"w") as f:
        params = {
            "alpha":alpha,
            "l1_ration":l1_ratio
        }
        json.dump(params,f,indent=4)

    os.makedirs(model_dir,exist_ok=True)
    model_path = os.path.join(model_dir,"model.joblib")

    joblib.dump(lr,model_path)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)
