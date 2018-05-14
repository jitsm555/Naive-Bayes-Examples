from database.table import get_all_records_count
from database.table import get_all_match_records_count
from database.table import get_all_weather_records
from database.table import get_all_match_for_weather_count
from database.table import create_database_connection
from database.utils import delete_database
from database.utils import is_file_exists
from database.utils import get_database_file_path
from enums.weather import get_play_condition_string
from enums.weather import get_weather_condition_string

''''
Formula of naive bayes
P(H|E) = P(E|H) * P(H) / P(E)
given the evidence.

P(H|E) - Posterior probability of 'H' given the evidence.
p(H) - Prior probability.
P(E) - Prior probability that the evidence itself is true.
P(E/H) - Likelihood of the evidence 'E' if the Hypothesis 'H' is true.
'''


def classify_play(weather_condition, play):
    yes = get_all_match_records_count(play) / get_all_records_count()
    rainy = get_all_weather_records(weather_condition) / get_all_records_count()
    ry = get_all_match_for_weather_count(play, weather_condition) / \
         get_all_match_records_count(play)
    print('yes: ' + str(yes))
    print(str(get_weather_condition_string(weather_condition)) + ': ' + str(rainy))
    print('yes/' + str(get_play_condition_string(play)) + ': ' + str(ry))
    return (ry * yes) / rainy


# Creating database file name weather_report.db
def create_database():
    try:
        file_name = get_database_file_path()
        # Check whether existing db file is available or not, if availbale deleted the old one.
        if is_file_exists(file_name):
            print("Deleted the existing db file")
            delete_database()
        create_database_connection(file_name)
    except:
        print("Exception while creating a database")
