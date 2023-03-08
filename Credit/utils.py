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