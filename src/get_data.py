import yaml
import pandas as pd
import argparse
from logger import App_Logger

file_object=open("Training_Logs/Loggings.txt", 'a+')
logger_object=App_Logger()

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config
    
def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["source"]

    try:
       df=pd.read_csv(data_path)
       logger_object.log(file_object, 'Data was read successfully')

    except Exception as e:
       logger_object.log(file_object,'Exception occurred in get_data. Exception message: '+str(e))
       logger_object.log(file_object,'get_data unsuccessful')
       raise Exception()

if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data=get_data(config_path=parsed_args.config)