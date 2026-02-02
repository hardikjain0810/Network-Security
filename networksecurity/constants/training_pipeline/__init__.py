import os
import sys
import numpy as np
import pandas as pd

'''
Defining common constant variable for training pipeline
'''
TARGET_COLUMN = "Result"
PIPELINE_NAME:str = 'NetworkSecurity'
ARTIFACT_DIR:str = 'artifacts'
FILE_NAME:str = 'phishingData.csv'
TRAIN_FILE_NAME:str = 'train.csv'
TEST_FILE_NAME:str = 'test.csv'

'''
Data ingestion related constant start with DATA_INGESTION var name 
'''
DATA_INGESTION_COLLECTION_NAME:str = "NetworkData"
DATA_INGESTION_DATABASE_NAME:str = "HARDIK"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
# raw data csv
DATA_INGESTION_FEATURE_STORE_DIR:str = 'feature_store'
# train.csv and test.csv
DATA_INGESTION_INGESTED_DIR:str = "ingested"
# train test split ratio
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2