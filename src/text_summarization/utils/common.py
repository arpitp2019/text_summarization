import os
import yaml
from src.text_summarization.logging import logging
from src.text_summarization.exception import CustomException
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

from pathlib import Path

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get file size in KB
    """
    size_in_kb = round(os.path.getsize(path))
    return f"{size_in_kb} KB"
    
    

def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """
    read YAML file 
    """
    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(path_to_yaml)
            logging.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys) from e 
            
    

def create_directories(path_to_directories : list, verbose = True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directories at : {path}")
    
    

