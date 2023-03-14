from Credit.config import mongo_client
from Credit.logger import logging
from Credit.exception import CreditException
import pandas as pd
import os,sys
import numpy as np
import dill
import yaml


##This function coonvert database collection into dataframe.
def get_collection_as_dataframe(database_name:str,collection_name:str)-> pd.DataFrame:
    try:
        logging.info(f"fetching data from database: {database_name} and collection: {collection_name}")
        #fetch the records from mongodb collection 
        mongo_record = list(mongo_client[database_name][collection_name].find())

        logging.info(f"creating dataframe")
        #create dataframe
        df = pd.DataFrame(mongo_record)

        logging.info(f"found columns: {df.columns}")
        #drop _id column that is provided by mongodb by default
        if "_id" in df:
            logging.info(f"dropping column: _id")
            df.drop(columns = ['_id'],inplace = True)

        return df
    
    except Exception as e:
        raise CreditException(e,sys)
    


def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise CreditException(e, sys)
    


def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        for column in df.columns:
            if column not in exclude_columns:
                if df[column].dtypes != 'O':
                    df[column]=df[column].astype('float')
        return df
    except Exception as e:
        raise CreditException(e, sys)
    



def save_object(file_path: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CreditException(e, sys) from e


    
def load_object(file_path: str, ) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CreditException(e, sys) from e




def save_numpy_array_data(file_path: str, array: np.array):

    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise CreditException(e, sys) from e
