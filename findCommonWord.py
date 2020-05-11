#!/usr/bin/env python3

"""
Find all synsets for all words
Find all hypernyms for those synsets
"""

from nltk.corpus import wordnet
import sys

input = sys.argv[1].split()
allSyns = set(ss for word in input for ss in wordnet.synsets(word))

allGenericWords = set()

for syn in allSyns:
	commons = [e for e in syn.hypernyms()]
	for word in commons:
		w = word.name()
		if "_" not in w: # filtering one-word words
			allGenericWords.add(w[:w.find(".")])

for word in allGenericWords:
	print(word)	



