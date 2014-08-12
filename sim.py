import numpy as np
import numpy.linalg as np_lin
import numpy.random as np_rand
import matplotlib.pyplot as plt
from random import choice
import cPickle, sys

def is_pos_def(x):
	return np.all(np.linalg.eigvals(x) > 0)

def is_sym(x):
	return (x.transpose(1, 0) == x).all()

def normalize(arr):
	arr_min = np.min(arr)
	arr_max = np.max(arr)
	rng = arr_max - arr_min
	return 1 - ((arr_max - arr) / rng)

def get_corpus(filename):
	corpus = []
	with open(filename, "r") as corpus_file:
		for word in list(corpus_file.read().split()):
			corpus.append(word)
	return corpus

def get_bigrams(ls):
	return zip(ls, ls[1:])

def generate_sentence(init, ls, corpus, max_itr):
	words = ""
	curr_idx = init
	curr_itr = 0
	while True:
		curr_itr += 1
		next_idx = choice(ls.get(curr_idx, [-1]))
		words = words + " " + corpus[curr_idx-1]
		if next_idx == -1:
			break
		elif curr_itr >= max_itr:
			break
		else:
			curr_idx = next_idx
	return words

if __name__ == "__main__":
	dim_len = 2000
	times = range(1, dim_len + 1)
	gamma = np.zeros((dim_len, dim_len))
	h = 0.5
	double_h = h * 2
	for i in times:
		for j in times:
			gamma[i-1, j-1] = (i ** (double_h) + j ** (double_h) - (abs(j - i) ** double_h)) / 2
	#print is_pos_def(gamma)
	#print is_sym(gamma)
	sigma = np_lin.cholesky(gamma)
	vec = np_rand.normal(size=(dim_len,))
	u = np.dot(sigma, vec)
	u = normalize(u)
	if len(sys.argv) == 2 and sys.argv[1] == "plot":
		plt.plot(range(dim_len), u, 'b-')
		plt.show()
	else:
		"""
		This sort of requires arithmetic coding
		Which requires in and of itself a lot of bit-fuckery
		"""
		corpus = get_corpus("corpus.txt")
		len_corpus = len(corpus)
		u = np.ceil(u * len_corpus).astype(int).tolist()
		tups = {}
		for i in get_bigrams(u):
			if not tups.get(i[0], None):
				tups[i[0]] = []
			tups[i[0]].append(i[1])
		print generate_sentence(0, tups, corpus, 5000)
