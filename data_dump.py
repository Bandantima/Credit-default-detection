import pymongo
import pandas as pd
import json
import os

client = pymongo.MongoClient("mongodb+srv://Bandantima:rakhinesh02@cluster0.v50bhkr.mongodb.net/?retryWrites=true&w=majority")

data_file_path =(r"C:\UCI_Credit_Card.csv")
database_name = "project"
collection_name = "Credit"


database = client[database_name]
collection = database[collection_name]

if __name__ == '__main__':

    ##import dataset to make dataframe
     df = pd.read_csv(data_file_path)
     print(df.shape)

    ##reset index of dataframe to have continuous count
     df.reset_index(drop = True,inplace = True)

    ##convert df to json so that we can dump these records in MongoDB
     json_records = list(json.loads(df.T.to_json()).values())

    ##inset json records into MongoDB
     client[database_name][collection_name].insert_many(json_records)
