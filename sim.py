import numpy as np
import numpy.linalg as np_lin

def is_pos_def(x):
	return np.all(np.linalg.eigvals(x) > 0)

def is_sym(x):
	return (x.transpose(1, 0) == x).all()

if __name__ == "__main__":
	times = range(1, 101)
	gamma = np.zeros((100, 100))
	h = 0.75
	double_h = h * 2
	for i in times:
		for j in times:
			gamma[i-1, j-1] = (i ** (double_h) + j ** (double_h) - (abs(j - i) ** double_h)) / 2
	#print is_pos_def(gamma)
	#print is_sym(gamma)
	sigma = np_lin.cholesky(gamma)
	vec = gaussian distribution
	u = sigma times vec
	print u #graph u also
