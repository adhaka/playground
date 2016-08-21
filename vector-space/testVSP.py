# @author:akash

# test script to test word vector space model.

import argparse
import VSP 
from Doc import Doc
from Utils import *


def main():

	parser = argparse.ArgumentParser()

	parser.add_argument('--order', type=int)
	args = parser.parse_args()
	foodList1 = ['hot', 'chocolate', 'milk', 'taco', 'sandwich', 'sushi', 'schnitzel', 'naan', 'croissant', 'bulle']
	vsp = VSP.VectorSpaceModel()
	vsp.loadDict(foodList1)

	ordered = False
	if args.order == 1:
		ordered=True

	doc1str = ' hot chocolate milk sandwich'
	doc1 = Doc(doc1str)
	doc1.vectorify(vsp)
	doc1Vec = doc1.getVector()
	doc2str = 'hot milk sandwich sushi naan'
	doc2 = Doc(doc2str)
	doc2.vectorify(vsp)
	doc2Vec = doc2.getVector()
	query1str = 'milk hot sushi'
	query1 = Doc(query1str)
	query1.vectorify(vsp, ordered=ordered)
	query1Vec = query1.getVector()
	score1 = vsp.dotProduct(query1Vec, doc1Vec)
	score2 = vsp.dotProduct(query1Vec, doc2Vec)
	# score3 = vsp.dotProduct(query1Vec, doc3Vec)
	query2str = 'hot milk sushi'
	query2 = Doc(query2str)
	query2.vectorify(vsp, ordered=ordered)
	query2Vec = query2.getVector()
	score21 = vsp.dotProduct(query2Vec, doc1Vec)
	score22 = vsp.dotProduct(query2Vec, doc2Vec)

	# print doc1Vec, doc2Vec
	# print query1Vec, query2Vec
	print "Dictionary:", foodList1
	print "Document 1:", doc1str
	print "Document 2:", doc2str
	print "Query:", query1str
	print "Score for doc1:", score1
	print "Score for doc2:", score2

	print "Query 2:", query2str
	print "Score for doc1:", score21
	print "Score for doc2:", score22

	scoreMap_Q1 = {}
	scoreMap_Q2 = {}

	# the key-map pair below can be stored in a persistance layer for a fast lookup ... 
	scoreMap_Q1[doc1.getDocNum()] = score1
	scoreMap_Q1[doc2.getDocNum()] = score2

	scoreMap_Q1_sorted = sortScoresWithOrder(scoreMap_Q1, desc=True)
	scoreMap_Q2_sorted = sortScoresWithOrder(scoreMap_Q2)

	# print scoreMap_Q1_sorted
	print "For query1- score sheet:"
	for k,v in scoreMap_Q1_sorted:
		print('DocNumber: %i, score:%5.4f' %(k,v))



if __name__ == '__main__':
	main()


