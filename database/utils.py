import os

''''

Delete the weather report
'''


def delete_database():
    os.remove('weather_report.db')
