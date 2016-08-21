# @author:akash

from itertools import count
from Utils import *
from VSP import VectorSpaceModel


class Doc:
	''' class to represenet a document or 
	a query in binary vector form, one instance
	of this class is either a document or a query,
	it takes in the vector space model as an argument,
	as the dictionary in the vector space model will determine
	the binary mapping.'''


	# keep index for docids and count number of docs processed.
	_docnums = count(1)
	def __init__(self, docString):
		self.docString = docString
		self.docNum = self._docnums.next()
		self.wordList = []
		self.docId = None
		self.docCat = None
		self.vector = None
		# self

	'create a doc with the list of all the words in the doc, category-1 for a document, category-2 for a query.'
	def _listify(self, cat=1):
		self.wordList = cleanString(self.docString)
		self.docCat = cat


	# method to vectorise the document to binary vector by invoking vectorize function of word-vector space model.
	def vectorify(self, vsp, ordered=False):
		if not isinstance(vsp, VectorSpaceModel):
			raise Exception('object not vector space')

		self._listify()
		# self.vector = vsp.vectorize(self.wordList, ordered)
		self.vector = vsp.vectorize_efficient(self.wordList, ordered)

# getter functions
	def getVector(self):
		return self.vector

	def getDocNum(self):
		return self.docNum

	def getDocString(self):
		return self.docString

	# fetch docstring from database. 
	def getDocStringById(self, docNum):
		pass