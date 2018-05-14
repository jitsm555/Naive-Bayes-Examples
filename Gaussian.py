# see jupyter notebook to know more about Naive Bayes classifier
''''
Formula of naive bayes
P(H|E) = P(E|H) * P(H) / P(E)
given the evidence.

P(H|E) - Posterior probability of 'H' given the evidence.
p(H) - Prior probability.
P(E) - Prior probability that the evidence itself is true.
P(E/H) - Likelihood of the evidence 'E' if the Hypothesis 'H' is true.

Problem : Find out the possibility of whether player play in Rainy condition ?
  P(Yes|Rainy) = P(Rainy|Yes) * P(Yes) / P(Rainy)
  P(Yes) - Find all yes from weather / All the weather records.
  P(Rainy) - All rainy records / All the weather records.
  P(Rainy/Yes) - All yes for rainy / Find all yes from weather
'''

from Classifier import classify_play
from Classifier import create_database
from enums.weather import WeatherCondition
from enums.weather import Play

if __name__ == '__main__':
    create_database()
    print(classify_play(WeatherCondition.sunny.value, Play.yes.value))
