import os
import sys

BASE_DIR = '../'    # project root
DATA_DIR = os.path.join(BASE_DIR, 'Data')

sys.path.append(BASE_DIR)

def fetch_datasets():

    # if directory for data doesn't exist, make one
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    
