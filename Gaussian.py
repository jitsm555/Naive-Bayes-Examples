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

import pandas as pd
from Classifier import classify_play

if __name__ == '__main__':
    print(classify_play())
