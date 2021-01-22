#!/usr/bin/env python
import sys

# import stop words
from sklearn.feature_extraction import stop_words
# define stops as set of stop words
stops = set(stop_words.ENGLISH_STOP_WORDS)

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # lowercase text
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stops:
        	print '%s\t%s' % (word, "1")
