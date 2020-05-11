# Codenames helper
Scripts to help you win the board-game "Codenames"!
<br><br>
**Disclaimer:** This may not be super accurate!

# Requirements
- python3
- nltk with wordnet corpus downloaded

# How-to
## Predicting similarity between available words
- ```python3 guessSimilarity.py <space separated words> <target word>```
- Make sure to quote the ```<space separated words>``` or else they will be considered as separate command line arguments
- Returns top occurrences of words which match the target word semantically

## Getting a common word based on list of words
- ```python3 findCommonWord.py <space separated words>```
- Finds all hypernyms of the list of words provided as cmd-line argument (Quote it!)

<br><br>
*Footnote: Is this cheating? Maybe. Probably.*
