import enum

'''
Enum for getting weather condtion
'''


class WeatherCondition(enum.Enum):
    sunny = 0
    overcast = 1
    rainy = 2


'''
Check whether play happend or not
'''


class Play(enum.Enum):
    yes = 1
    no = 0


def get_weather_condition_string(enum):
    if enum == 0:
        return 'Sunny'
    elif enum == 1:
        return 'Overcast'
    else:
        return 'Rainy'


def get_play_condition_string(enum):
    if enum == 0:
        return 'Yes'
    else:
        return 'No'
