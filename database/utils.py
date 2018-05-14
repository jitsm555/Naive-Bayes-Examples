import os
from database.constant import db_name

''''

Delete the weather report
'''


def delete_database():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path) + '/'
    os.remove(dir_path + 'weather_report.db')


def get_database_file_path():
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path) + '/'
    return dir_path + db_name


''''
Check whether given databas exist or not.

'''


def is_file_exists(file_name):
    if os.path.isfile(file_name):
        return True
    else:
        return False
