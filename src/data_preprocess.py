import pandas as pd
from re import split
import argparse
import yaml
from sklearn.preprocessing import LabelEncoder
from logger import App_Logger

file_object=open("Training_Logs/Loggings.txt", 'a+')
logger_object=App_Logger()

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def encoding(config_path):
    config = read_params(config_path)
    train_data_path=config["encoder"]["train_path"]
    test_data_path=config["encoder"]["test_path"]
    source_train_data_path=config["split_data"]["train_path"]
    source_test_data_path=config["split_data"]["test_path"]
    
    train=pd.read_csv(source_train_data_path)
    test=pd.read_csv(source_test_data_path)

    try:
        encoder=LabelEncoder()
        for column in range(len(train.columns)):
          train[train.columns[column]]= encoder.fit_transform(train[train.columns[column]])
          train.to_csv(train_data_path,index=False)
        logger_object.log(file_object,'Label encoding was successful for train data')

        encoder=LabelEncoder()
        for column in range(len(test.columns)):
          test[test.columns[column]]= encoder.fit_transform(test[test.columns[column]])
          test.to_csv(test_data_path,index=False)
        logger_object.log(file_object,'Label encoding was successful for test data')

    except Exception as e:
        logger_object.log(file_object,'Exception occurred in encoding. Exception message: '+str(e))
        logger_object.log(file_object,'Label encoding was unsuccessful')
        raise Exception()

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data=encoding(config_path=parsed_args.config)