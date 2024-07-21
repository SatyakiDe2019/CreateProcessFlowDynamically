################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  15-May-2020               ####
#### Modified On: 21-Jul-2024               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the keys for        ####
#### personal UpTrain-based LLM evaluation  ####
#### solution to fetch the KPIs to tune it. ####
####                                        ####
################################################

import os
import platform as pl

class clsConfigClient(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        'ARCH_DIR': Curr_Path + sep + 'arch' + sep,
        'PROFILE_PATH': Curr_Path + sep + 'profile' + sep,
        'LOG_PATH': Curr_Path + sep + 'log' + sep,
        'DATA_PATH': Curr_Path + sep + 'data' + sep,
        'OUTPUT_PATH': Curr_Path + sep + 'output' + sep,
        'TEMP_PATH': Curr_Path + sep + 'temp' + sep,
        'IMAGE_PATH': Curr_Path + sep + 'Image' + sep,
        'SESSION_PATH': Curr_Path + sep + 'my-app' + sep + 'src' + sep + 'session' + sep,
        'OUTPUT_DIR': 'model',
        'APP_DESC_1': 'Dynamically Creating Process Flow Demo!',
        'DEBUG_IND': 'Y',
        'INIT_PATH': Curr_Path,
        'FILE_NAME': 'input.json',
        'MODEL_NAME': "gpt-3.5-turbo",
        'OPEN_AI_KEY': "sk-fz1KHdgdy747fhoT3BLOIUs86743PnN3Y9Pt2OjKuYti",
        'TITLE': "Dynamically Creating Process Flow Demo!",
        'TEMP_VAL': 0.2,
        'PATH' : Curr_Path,
        'MAX_TOKEN' : 512,
        'MAX_CNT' : 5,
        'OUT_DIR': 'data',
        'OUTPUT_DIR': 'output',
        'SUBDIR_OUT': 'output',
        'SESSION_CACHE_FILE': 'sessionCacheCounter.csv',
        'ADMIN_KEY': "Admin@23",
        'SECRET_KEY': "Adsec@23",
        "USER_NM": "Test",
        "USER_PWD": "Test@23",
        "DB_PATH": Curr_Path + sep + 'data' + sep,
        "INPUT_VAL": 1000000000,
        'YEAR_RANGE': 1
    }
