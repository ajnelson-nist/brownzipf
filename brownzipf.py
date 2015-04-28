from __future__ import division
import sys
from itertools import *
from pylab import *
from nltk.corpus import brown
from collections import Counter

# Pick a lowercasing function according to Python version
if sys.version_info.major < 3:
    from string import lower
else:
    lower = str.lower

# The data: token counts from the Brown corpus
tokens_with_count = Counter(map(lower, brown.words()))
#Dictionary keys in Python 3 aren't indexable, so store the tokens as a list.
#The list is sorted to prevent changes in display text on repeated runs.
tokens = sorted([k for k in tokens_with_count.keys()])
counts = array([tokens_with_count[k] for k in tokens])

# A Zipf plot
ranks = arange(1, len(counts)+1)
indices = argsort(-counts)
frequencies = counts[indices]
loglog(ranks, frequencies, marker=".")
title("Zipf plot for Brown corpus tokens")
xlabel("Frequency rank of token")
ylabel("Absolute frequency of token")
grid(True)
for n in list(logspace(-0.5, log10(len(counts)), 20).astype(int)):
    dummy = text(ranks[n], frequencies[n], " " + tokens[indices[n]], 
                 verticalalignment="bottom",
                 horizontalalignment="left")

show()
