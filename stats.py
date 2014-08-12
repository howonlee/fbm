import matplotlib.pyplot as plt

def get_corpus(filename):
	corpus = []
	with open(filename, "r") as corpus_file:
		for word in list(corpus_file.read().split()):
			corpus.append(word)
	return corpus

if __name__ == "__main__":
	corpus = get_corpus("corpus.txt")
	idx_arr = []
	idx_dict = {}
	for i, word in enumerate(corpus):
		if word not in idx_dict:
			idx_dict[word] = i
		idx_arr.append(idx_dict[word])
	plt.plot(range(len(idx_arr)), idx_arr, 'b-')
	plt.show()

