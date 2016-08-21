This file will contain instructions to run the miniproject of ranked scoring of documents based on bag of word feature as asked in the chalenge.

Main File: testVSP.py

To run:

for unordered scoring:
python testVSP.py

for ordered scoring:
python testVSP.py --order 1

In ordered scoring, the sequence of words in the query string matters, and thus "milk hot" will be different from "hot milk". In ordered sequnce, if there is a match for the first word, we proceed to the second word in the remaining dictionary and so on. As the dictionary of words we use in VSP class has an inherent sequence because of list properties in python.


VSP : Vector Word Space Model class, creates an object with the specified dictionary of all possible food words in english. A new instantiation of this class can be a different language dictionary of words. contains our algorithm of calculating cosine score to calculate similarities between two vectors, also contains function to generate vectors out of raw document strings.

Doc:Class for storing documents, all docs and strings are stored as a Doc object, each instance gets a new id:docNum 

Utils: Helper functions



Proposal for Optimisation

Computing dot product of matrices is highly optimised in numpy, so the bottlneck is the creation of vectors.
The complexity of the current algorithm is O(n) where n is the min(words in dictionary, words in document). If
the data is of much bigger scale like 1 million rows, then we should ideally use a database layer, one million
large dataset might not come into memory at once, although keeping data in memory is faster than looking up in database.
The data vectors we will get will be quite sparse, so we can use some standard matrix compression techniques to reduce
the rank of the document vectors.  
