"""
Numpy markov chain
With probabilities on words and stuff
"""
import numpy as np
import scipy as sci
import scipy.sparse as sci_sp
import collections

if __name__ == "__main__":
	corpus = []
	with open("corpus.txt", "r") as corpus_file:
		for word in corpus_file.read().split():
			corpus.append(word)
	corpus_cts = collections.Counter(corpus).most_common()
	len_corpus = len(corpus_cts)
	order_1 = sci_sp.dok_matrix((len_corpus, len_corpus), dtype=np.float32)
	print order_1.shape

