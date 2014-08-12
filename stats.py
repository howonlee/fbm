import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

def get_corpus(filename):
	corpus = []
	with open(filename, "r") as corpus_file:
		for word in list(corpus_file.read().split()):
			corpus.append(word)
	return corpus

if __name__ == "__main__":
	mp.rcParams['axes.linewidth'] = .01
	mp.rcParams['lines.linewidth'] = .01
	mp.rcParams['patch.linewidth'] = .01
	corpus = get_corpus("corpus.txt")
	idx_arr = []
	idx_dict = {}
	for i, word in enumerate(corpus):
		if word not in idx_dict:
			idx_dict[word] = i
		idx_arr.append(idx_dict[word])
	#print idx_arr[0:1000]
	plt.plot(idx_arr)
	plt.show()

