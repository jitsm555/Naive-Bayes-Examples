'''
This class will take care of all Database related queries which used to classify naive bayes
algorithm.


'''

import sqlite3
from sqlite3 import Error
import pandas as pd
import os
from database.utils import get_database_file_path
df = pd.read_csv('weather.csv')

""" 
create a database connection to a SQLite database 
"""


def get_connection():
    return sqlite3.connect(get_database_file_path())


def create_database_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("CREATE TABLE if not exists Data (Column1 TEXT, Column2 TEXT)")
        df.to_sql("weather", conn, if_exists='append', index=False)
        return conn

    except Error as e:
        print(e)


''''
Check whether given databas exist or not.

'''


def is_file_exists(file_name):
    if os.path.isfile(file_name):
        return True
    else:
        return False


''''
Get the count of all records.

'''


def get_all_records_count():
    return get_connection().execute("SELECT COUNT(*) FROM weather").fetchone()[0]


''''
Get the count of all match count eg : yes/no.
'''


def get_all_match_records_count(play):
    return get_connection().execute("SELECT COUNT(*) from weather WHERE PLAY = " + str(play)).fetchone()[0]


''''
Get all the given weather records.
'''


def get_all_weather_records(weather):
    return get_connection().execute("SELECT COUNT(*) from weather WHERE Weather = " + str(weather)).fetchone()[0]


''''
Get all match records count count, based on the play happed or not and weather condition 
'''


def get_all_match_for_weather_count(play, weather):
    return get_connection().execute(
        "SELECT COUNT(*) from weather WHERE Weather = " + str(weather) + " AND Play = " + str(play)).fetchone()[0]
