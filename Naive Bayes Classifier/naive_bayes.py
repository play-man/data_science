import numpy as np
from scipy.stats import norm

class Naive_Bayes:

	def __init__(self):
		self.about = "Naive Bayes Classifier by youngster31"
		self.dataset = []


	def __init__(self, dataset):
		self.about = "Naive Bayes Classifier by youngster31"
		self.dataset = np.array(dataset)


	def write_dataset(dataset):
		self.dataset = np.array(dataset)


	#def split(self):


	def separate(self, index):
		separated_dataset = {}
		for i in range(len(self.dataset)):
			instance = self.dataset[i]
			try:
				separated_dataset[instance[index]].append(instance)
			except KeyError:
				separated_dataset[instance[index]] = []
				separated_dataset[instance[index]].append(instance)
		return separated_dataset


	def stats(self):
		transposed_dataset = np.transpose(self.dataset)
		stats = np.array(list([np.mean(attribute), np.std(attribute)] for attribute in transposed_dataset))
		self.stats = stats
		return stats


	def stats_for_separated(self):
		separated_dataset = self.separate(dataset, -1)
		stats = {}
		for class_value, instance in separated_dataset.iteritems():
			stats[class_value] = self.stats(instance)
		return stats


	def probabilities(self, input, index):
		probabilities = {}
		for class_value, class_stats in self.stats.iteritems():
			probabilities[class_value] = 1
			for i in range (len(class_stats)):
				mean, stdev = class_stats[i]
				x = input[i]
				probabilities[class_value] = norm.cdf(x, mean, stdev)
		self.probabilities = probabilities
		return probabilities


	def prediction(self):
		best_label, best_prob = None, -1
		for class_value, probability in self.probabilities.iteritems():
			if best_label is None or probability > best_prob:
				best_prob = probability
				best_label = class_value
		return best_label
