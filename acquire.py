import pandas as pd
import os.path
import io

def acquire_data():
    '''
    Checks if csv exists; if yes, reads csv. If no, reads url
    into dataframe and writes to csv. Returns dataframe.
    '''
    if os.path.isfile('tmdb_test.csv'):
        tmdb_test = pd.read_csv('tmdb_test.csv')
        tmdb_train = pd.read_csv('tmdb_train.csv')
    return tmdb_train, tmdb_test