#!/usr/bin/env python

# For changes made after April 1, 2016:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

from __future__ import division

import collections

from pylab import *

def zipf_plot(counter_dict, outfilename):
    #Typecheck
    assert isinstance(counter_dict, collections.Counter)

    #Dictionary keys in Python 3 aren't indexable, so store the tokens as a list.
    #The list is sorted to prevent changes in display text on repeated runs.
    tokens = sorted([k for k in counter_dict.keys()])
    counts = array([counter_dict[k] for k in tokens])

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

    savefig(outfilename, type="png")

def main():
    outfilename = args.out_png

    # Pick a lowercasing function according to Python version
    import sys
    if sys.version_info.major < 3:
        from string import lower
    else:
        lower = str.lower

    # The data: token counts from the Brown corpus
    from nltk.corpus import brown
    tokens_with_count = collections.Counter(map(lower, brown.words()))

    zipf_plot(tokens_with_count, outfilename)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("out_png")
    args = parser.parse_args()

    main()
