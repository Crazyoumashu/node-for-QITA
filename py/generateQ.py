import matplotlib.pyplot as plt
import math
import random
import numpy as np

file = open('q.txt', 'w')

mu = 50
sigma = 20
n = 150
data = np.random.normal(mu, sigma, n)
q = []
for j in range(0, n):
	q.append(int(abs(data[j])))

file.write(str(q[0]))
for j in range(1, n):
	file.write('\t')
	file.write(str(q[j]))
