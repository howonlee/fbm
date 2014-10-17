import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np
from random import shuffle

def get_corpus(filename):
	corpus = []
	with open(filename, "r") as corpus_file:
		for word in list(corpus_file.read().split()):
			corpus.append(word)
	return corpus

if __name__ == "__main__":
	mp.rcParams['axes.linewidth'] = 1
	mp.rcParams['lines.linewidth'] = 1
	mp.rcParams['patch.linewidth'] = 1
	corpus = get_corpus("corpus.txt")
	idx_arr = []
	idx_dict = {}
	for i, word in enumerate(corpus):
		if word not in idx_dict:
			idx_dict[word] = i
		idx_arr.append(idx_dict[word])
	idx_arr = idx_arr[10000:10100]
	#shuffle(idx_arr)
	plt.plot(idx_arr, "ro")
	plt.show()

