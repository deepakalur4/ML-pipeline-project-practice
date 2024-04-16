import logging
from datetime import datetime
import os
from src.exception import CustomException
import sys

log_path=f"{datetime.now().strftime("%m_%d_%y_%H_%M_%S")}.log"
log_file_dir_path=os.path.join(os.getcwd(),"logs",log_path)
os.makedirs(log_file_dir_path,exist_ok=True)
log_file_path=os.path.join(log_file_dir_path,log_path)


logging.basicConfig(filename=log_file_path,level=logging.INFO)

