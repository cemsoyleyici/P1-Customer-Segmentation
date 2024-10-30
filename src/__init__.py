"""
This script contains the logger configuration for the project.

"""

import os
import sys
import logging

logging_str = "[%(asctime)s] [%(levelname)s] [%(module)s:%(funcName)s:%(lineno)d] [%(threadName)s] - %(message)s" # logging format
log_dir = "logs" # directory to save the logs
log_filepath = os.path.join(log_dir, "running_logs.log") # file to save the logs
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath), # save the log
        logging.StreamHandler(sys.stdout) # print the log to the console
        ]
)

logger = logging.getLogger("CustomerSegmentationLogger")
