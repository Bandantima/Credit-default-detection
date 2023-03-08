from Credit.logger import logging
from Credit.exception import CreditException
import os
import sys
from Credit.utils import get_collection_as_dataframe
from Credit.entity.config_entity import DataIngestionConfig
from Credit.entity import config_entity


'''
def test_logger_and_expection():
    try:
       logging.info("Starting the test_logger_and_exception")
       result = 3/0
       print(result)
       logging.info("Stoping the test_logger_and_exception")
    except Exception as e:
       logging.debug(str(e))
       raise InsuranceException(e, sys)
'''

'''
if __name__=="__main__":
    try:
         get_collection_as_dataframe(database_name='project',collection_name='Credit')
    except Exception as e:
         print(e)
'''

if __name__=="__main__":
    try:
      training_pipeline_config = config_entity.TrainingPipelineConfig()
       #data ingestion
      data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
      print(data_ingestion_config.to_dict())
    except Exception as e:
       print(e)
    