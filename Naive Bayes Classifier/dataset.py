from sklearn import datasets
from matplotlib import pyplot as plt
import numpy as np
from naive_bayes import Naive_Bayes

iris = datasets.load_iris()

Bayes = Naive_Bayes(iris.data)
Bayes.stats()
