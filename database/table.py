import sqlite3
from sqlite3 import Error
import pandas as pd
import os
from database.constant import db_name
from database.utils import delete_database

df = pd.read_csv('/Users/jiteshmohite/projects/2017-2018/AI/algo/Naive-Bayes-Examples/database/weather.csv')

""" 
create a database connection to a SQLite database 
"""


def get_connection():
    return sqlite3.connect("/Users/jiteshmohite/projects/2017-2018/AI/algo/Naive-Bayes-Examples/database/weather_report.db")


def create_database_connection(db_file):
    try:
        print(sqlite3.version)
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
    return get_connection().execute("SELECT COUNT(*) FROM weather")


''''
Get the count of all yes records.
'''


def get_all_yes_records_count():
    return get_connection().execute("SELECT COUNT(*) from weather WHERE PLAY = 0")


''''
Get all the rainy records.
'''


def get_all_rainy_records():
    return get_connection().execute("SELECT COUNT(*) from weather WHERE Weather = 2")


''''
Get all yes records for rainy
'''


def get_all_yes_for_rainy_count():
    return get_connection().execute("SELECT COUNT(*) from weather WHERE Weather = 2 AND Play = 0")


if __name__ == '__main__':
    create_database_connection(db_name + '.db')
    # delete_database()
