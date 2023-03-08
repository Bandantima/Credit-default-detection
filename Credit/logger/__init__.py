import logging
import os
from datetime import datetime

LOG_DIR="Credit_log"

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}"

#log_file_name 
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

#create folder if not available
os.makedirs(LOG_DIR,exist_ok=True)

#log file path
LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename = LOG_FILE_PATH,
    filemode="w",
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.debug)
