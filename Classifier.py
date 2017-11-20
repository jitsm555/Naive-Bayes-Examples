from database.table import get_all_records_count
from database.table import get_all_match_records_count
from database.table import get_all_weather_records
from database.table import get_all_match_for_weather_count
from enums.weather import WeatherCondition
from enums.weather import Play
from database.table import is_file_exists
from database.table import create_database_connection
from database.utils import delete_database
from database.constant import db_name

''''
Formula of naive bayes
P(H|E) = P(E|H) * P(H) / P(E)
given the evidence.

P(H|E) - Posterior probability of 'H' given the evidence.
p(H) - Prior probability.
P(E) - Prior probability that the evidence itself is true.
P(E/H) - Likelihood of the evidence 'E' if the Hypothesis 'H' is true.
'''


# Problem : Find out the possibility of whether player play in Rainy condition ?
# P(Yes|Rainy) = P(Rainy|Yes) * P(Yes) / P(Rainy)
# P(Yes) - Find all yes from weather / All the weather records.
# P(Rainy) - All rainy records / All the weather records.
# P(Rainy/Yes) - All yes for rainy / Find all yes from weather


def classify_play():
    yes = get_all_match_records_count(Play.yes.value) / get_all_records_count()
    rainy = get_all_weather_records(WeatherCondition.rainy.value) / get_all_records_count()
    ry = get_all_match_for_weather_count(Play.yes.value, WeatherCondition.rainy.value) / \
         get_all_match_records_count(Play.yes.value)
    print('yes' + str(yes))
    print('rainy' + str(rainy))
    print('yes/rainy' + str(ry))
    return (ry * yes) / rainy


'''
Create database connection before modeling
'''


def create_database():
    try:
        delete_database()
        create_database_connection(db_name)
    except:
        create_database_connection(db_name)
