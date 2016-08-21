# @author:akash

# script contaning helper functions and all useful utilities


def cleanWords(word):
	word = word.strip()
	word = word.replace(' ', '').lower()
	return word


def cleanString(sentence):
	sentence = sentence.strip()
	listVec = sentence.split(' ')
	return listVec


def sortScoresWithOrder(scoreMap, desc=False):
	scoreMap_sorted = sorted(scoreMap.items(), key=lambda x:x[1], reverse=desc)
	return scoreMap_sorted