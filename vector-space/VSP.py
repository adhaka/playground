# @_author:akash

# script to store words int he word vector space.


import numpy as np 
import matplotlib.pyplot as plt
import math

from Utils import *

# takes the list of all words as an input.
class VectorSpaceModel():
	'''
	class for the word-vector space model, an object
	of this class will represent the word space, it takes
	a dictionary which is a list of words, as an argument
	and uses it to make vector representations for all the 
	documents and queries. The dictionary is a Python list 
	and thus it can preserve the inherent sequence of words.
	'''

	def __init__(self):
		'lazy loading ftw '
		self.dictionary = None
		self.dictionary_sorted = None
		self.space_size = None

	def loadDict(self, dictionary):
		'load the dictionary'
		if not self.dictionary:
			dictionary = map(lambda x: cleanWords(x), dictionary)		
			self.dictionary = dictionary
			self.space_size = len(self.dictionary)
		
		dictionary_sorted = sorted(dictionary)
		self.dictionary_sorted = dictionary_sorted



	def vectorize(self, document, ordered=False):
		'if ordered is true, we care about the sequence of words in the dictionary otherwise not. \
		the logic is, if no order is to be maintained, just look if each individual word in the \
		dictionary is present in the document or not.'
		
		if not isinstance(document, (list, tuple)):
			document = cleanString(document)

		binary_vector = np.zeros((len(self.dictionary),1))

		i = 0
		j = 0
		k = 0
		if ordered:
			for i, word_doc in enumerate(document):
				for j, word_query in enumerate(self.dictionary[k:]):
					if word_doc == word_query:
						ind = self.dictionary.index(word_doc)
						k = j
						binary_vector[ind] = 1
						i += 1
						j += 1
		else:

			for word in self.dictionary:
				if word in document:
					binary_vector[i] = 1
				i += 1

		return binary_vector



	def vectorize_efficient(self, document, ordered=False):
		' max complexity:O(n) where n is the number of words in the document; should be less than number of words in dictionary in general'

		# sanity check to ensure document is a list of words and not a string.
		if not isinstance(document, (list, tuple)):
			document = cleanString(document)

		binary_vector = np.zeros((len(self.dictionary),1))

		i = 0
		j = 0
		k = 0

		if ordered:
			for i, word_doc in enumerate(document):
				for j, word_query in enumerate(self.dictionary[k:]):
					if word_doc == word_query:
						ind = self.dictionary.index(word_doc)
						k = j
						binary_vector[ind] = 1
						i += 1
						j += 1
		else:
			for word in document:
				if word in self.dictionary:
					ind = self.dictionary.index(word)
					binary_vector[ind] = 1
				i += 1

		return binary_vector
		

	def dotProduct(self, doc_vec, query_vec, normalise=True):
		'this function computes the cosine score between a document and a query vector. \
		the score should be normalise by dividing the score by the length of both the vectors.'

		doc_size = doc_vec.shape[0]
		query_size = query_vec.shape[0]

		ones = np.ones((self.space_size,1))
		if (doc_size != query_size or self.space_size != doc_size) :
			raise Exception("query and doc should have same size.")

		# a.b
		scalar_score = np.dot(doc_vec.T, query_vec)

		# calculate the number of ones in document- will give the length of vector.
		doc_ones = np.dot(ones.T, doc_vec)
		# calculate the number of ones in query.
		query_ones = np.dot(ones.T, query_vec)

		# cosine_score = a.b / (|a||b|)
		# |a| = number of ones in vector a.
		if normalise == True:
			scalar_score = scalar_score / math.sqrt(doc_ones*query_ones)

		return scalar_score[0,0]


