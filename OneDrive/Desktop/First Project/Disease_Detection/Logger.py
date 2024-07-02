import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOGS_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOGS_PATH,exist_ok = True)

Log_file_path = os.path.join(LOGS_PATH,LOG_FILE)

logging.basicConfig(

    filename = Log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO

)