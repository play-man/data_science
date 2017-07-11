import numpy as np

class K_means:

	def __init__(self, N, X, k):
		self.about = "K-means clustering by youngster31"
		self.C = []	# clusters centroids
		self.clusters = {}
		self.N = N
		self.X = X	# points
		self.k = k


	def init_X(self, low = -1.0, high = 1.0):
		self.X = np.random.uniform(low, high, [self.N, 2])


	def init_random_centroids(self, low = -1.0, high = 1.0):
		self.C = np.random.uniform(low, high, [self.k, 2])


	def err(self):
		return np.sum(list(np.sum(list(np.linalg.norm(self.C[i] - self.clusters[i][j]) for j in range (len(self.clusters[i])))) for i in range(self.k)))


	def recalculate_centroids(self):
		for i in range (self.k):
			if len(self.clusters[i]) == 0:
				continue
			else:
				self.C[i] = np.mean(self.clusters[i], axis=0)


	def clustering(self):
		N = self.X.shape[0]
		self.clusters = {}
		for i in range (N):
			index = np.argmin(list(np.linalg.norm(self.X[i] - self.C[j]) for j in range(self.k)))
			try:
				self.clusters[index].append(self.X[i])
			except KeyError:
				self.clusters[index] = [self.X[i]]
		for index in range(self.k):
			try:
				a = len(self.clusters[index])  # try to access cluster with index if non-empty
			except KeyError:
				self.clusters[index] = []


	def terminate_count(self, count, count_max):
		return count > count_max


	def terminate_error(self, err, err_new, eps):
		return (err - err_new < eps) or (err_new > err)


	def terminate(self, err, err_new, eps, count, count_max):
		return self.terminate_count(count, count_max) or self.terminate_error(err, err_new, eps)


	def lloyd_clustering(self, eps = 0.0001, count_max = 1000):
		self.init_X()
		self.init_random_centroids()
		self.clustering()
		err = self.err()
		err_new = 0
		count = 0
		while not self.terminate(err, err_new, eps, count, count_max):
			err = self.err()
			count += 1
			self.recalculate_centroids()
			self.clustering()
			err_new = self.err()
		print(count)
