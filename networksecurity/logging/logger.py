import os 
import sys
import logging
from datetime import datetime

Log_file_format = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = os.path.join(os.getcwd(),"logs",Log_file_format)
os.makedirs(log_dir,exist_ok=True)

log_file_path = os.path.join(log_dir,Log_file_format)

logging.basicConfig(
    filename=log_file_path,
    format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    level=logging.INFO
)