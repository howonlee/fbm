import numpy as np
import numpy.linalg as np_lin
import numpy.random as np_rand
import matplotlib.pyplot as plt
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
		for word in list(corpus_file.read()):
			corpus.append(word)
	return corpus


#use cumsum and turn into markov chain eventually
if __name__ == "__main__":
	assert len(sys.argv) == 2
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
	if sys.argv[1] == "plot":
		plt.plot(range(dim_len), u, 'b-')
		plt.show()
	else:
		corpus = get_corpus("corpus.txt")
		len_corpus = len(corpus)
		u = np.ceil(u * len_corpus).astype(int).tolist()
		text = ""
		for i in u:
			text = text + corpus[i- 1]
		print text
