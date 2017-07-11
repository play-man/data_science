import numpy as np 
import string

alphabet = string.digits + string.lowercase + string.uppercase
base = len(alphabet)


def code(x, b = base):
	x = num
	residue = 0
	string = []
	while x:
		residue = x % b
		x /= b
		string.append(alphabet[residue])
	string.append(alphabet[residue])
	return string

def decode(string, b = base):
	num = 0
	for i in range(len(string)):
		num = num * b + alphabet.find(string[i])  
	return num