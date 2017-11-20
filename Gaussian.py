# see jupyter notebook to know more about Naive Bayes classifier
''''
Formula of naive bayes
P(H|E) = P(E|H) * P(H) / P(E)
given the evidence.

P(H|E) - Posterior probability of 'H' given the evidence.
p(H) - Prior probability.
P(E) - Prior probability that the evidence itself is true.
P(E/H) - Likelihood of the evidence 'E' if the Hypothesis 'H' is true.
'''

from Classifier import classify_play
from Classifier import create_database

if __name__ == '__main__':
    create_database()
    print(classify_play())
