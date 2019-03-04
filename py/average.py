import matplotlib.pyplot as plt
import math
import random
import numpy as np
import os

file = open('output.txt', 'r')
output = open('experiment7.txt', 'a')
q = []
for line in file:
	data = line[:-1]
	q = [float(s) for s in data.split('\t')]

res = 0
for item in q:
	res += item
res /= len(q)
output.write(str(res)+'\t')