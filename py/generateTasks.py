import matplotlib.pyplot as plt
import math
import random
import numpy as np

file = open('tasks.txt', 'w')

m = 10
R = 10
ymin = 74.0
ymax = 74.25
xmin = 40.75
xmax = 40.95
xt = []
yt = []
for i in range(0, m):
	xt.append(np.random.rand()*(xmax-xmin)+xmin)
	yt.append(np.random.rand()*(ymax-ymin)+ymin)

for i in range(0, m):
	task = str(xt[i]) + '\t' + str(yt[i]) + '\n'
	file.write(task)

