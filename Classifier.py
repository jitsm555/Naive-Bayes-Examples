from database.table import get_all_records_count
from database.table import get_all_yes_records_count
from database.table import get_all_rainy_records
from database.table import get_all_yes_for_rainy_count

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
    print('get_all_yes_records_count().fetchone()[0]' + str(get_all_yes_records_count().fetchone()[0]))
    print('get_all_records_count().fetchone()[0]' + str(get_all_records_count().fetchone()[0]))
    print('get_all_rainy_records() ' + str(get_all_rainy_records().fetchone()[0]))
    print('get_all_yes_for_rainy_count()' + str(get_all_yes_for_rainy_count().fetchone()[0]))

    yes = get_all_yes_records_count().fetchone()[0] / get_all_records_count().fetchone()[0]
    rainy = get_all_rainy_records().fetchone()[0] / get_all_records_count().fetchone()[0]
    ry = get_all_yes_for_rainy_count().fetchone()[0] / get_all_yes_records_count().fetchone()[0]
    print('yes' + str(yes))
    print('rainy' + str(rainy))
    print('yes/rainy' + str(ry))
    return (ry * yes) / rainy
