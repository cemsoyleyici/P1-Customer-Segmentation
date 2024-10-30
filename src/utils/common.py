

import os
import yaml
import json
from src import logger
from pathlib import Path
from typing import Dict, Any
from box import ConfigBox
from box.exceptions import BoxValueError
from datetime import datetime

def read_yaml(file_path: Path) -> Dict[str, Any]:
    """
    Reads a YAML file and returns its content as a dictionary.
    Args:
        file_path (str): The path to the YAML file.
    Returns:
        Dict[str, Any]: The content of the YAML file as a dictionary.
    Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If the YAML file is empty.
        Exception: If there is an error reading the YAML file.
    """
    
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f"YAML file: {file_path} loaded successfully")
            if data is None:
                raise ValueError("YAML file is empty")
            else:
                return ConfigBox(data)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise

def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

def read_file(path: str, file_type = "csv"):
    """read files from a directory

    Args:
        path (str): _description_
        file_type (str, optional): _description_. Defaults to "csv".
    """
    # Get list of files in the directory
    files = os.listdir(path)
    try:
        # Filter out files that match the pattern "*.csv"
        files = [f for f in files if f.endswith("." + file_type)]

        # Sort files by date in descending order
        files.sort(key=lambda x: datetime.strptime(x.split("_")[-1].split(".")[0], "%Y-%m-%d"), reverse=True)
        
        return files[0]
    
    except Exception as e:
        logger.error(f"Error reading files: {e}")
        raise