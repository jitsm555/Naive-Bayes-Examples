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
    yes = 0
    no = 1
