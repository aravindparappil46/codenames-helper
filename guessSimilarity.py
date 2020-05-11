#!/usr/bin/env python3

from nltk.corpus import wordnet
import heapq
import sys

possibles = sys.argv[1].split()
guessWord = sys.argv[2]
k = 0

target = wordnet.synsets(guessWord) # Target word will have many synsets
allSimilarities = []

"""
Iterate over each possible  word, find list of synsets for that word
Iterate over each synset of target, iterate over each synset of curr word
Find similarity score, push to heap
"""

allSyns = set((ss,word) for word in possibles for ss in wordnet.synsets(word))

for syn, word in allSyns:
	for ts in target:
		score = ts.wup_similarity(syn)
		if score and (-score, word, syn) not in allSimilarities:
			heapq.heappush(allSimilarities, (-score, word, syn))

# Printing only top 12 guesses
while k < 13:
	score, word, syn = heapq.heappop(allSimilarities)
	print(word+":", str(round(-score*100))+"%", "->", syn.lemma_names())
	k += 1

