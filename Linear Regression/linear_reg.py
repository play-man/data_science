import numpy as np

class LinReg:

	def __init__(self):
		self.about = "Linear regression by youngster31"
		self.W = []


	def random_w(self, low, high, m):
		return np.random.uniform(low, high, m)


	def err(self, y_real, y_exp):
		return np.linalg.norm(y_real - y_exp)


	def derr_dw(self, dy, X):
		return 2 * np.dot (dy, X) / len(dy)


	def gradient_iteration(self, X, W, dy, step):
		return W - step * self.derr_dw(dy, X)


	def terminate_count(self, count, count_max):
		return count > count_max


	def terminate_error(self, err, err_new, eps):
		return (err - err_new < eps) or (err_new > err)


	def terminate(self, err, err_new, eps, count, count_max):
		return self.terminate_count(count, count_max) or self.terminate_error(err, err_new, eps)


	def gradient_descent(self, x_real, y_real, step = 1.0, count_max = 5000, eps = 0.0001):
		err = 1
		err_new = 0
		count = 0
		m = x_real.shape[0]
		n = x_real.shape[1]
		x_real = np.hstack((np.ones(m).reshape(m, 1), x_real))
		Wi = self.random_w(0.0, 1.0, n + 1)
		y_exp = np.dot(x_real, Wi)
		while not self.terminate(err, err_new, eps, count, count_max):
			count += 1
			dy = y_exp - y_real
			err = self.err(y_real, y_exp)
			Wi = self.gradient_iteration(x_real, Wi, dy, step)
			y_exp = np.dot(x_real, Wi)
			err_new = self.err(y_real, y_exp)
		self.W = Wi
		print(count)
		return self.W

	def predict(self, x):  # here x is an array
		return np.dot([1] + x, self.W)

	def predict_values(self, X):  # X is a matrix
		m = X.shape[0]
		return np.dot(np.hstack((np.ones(m).reshape(m, 1), X)), self.W)
