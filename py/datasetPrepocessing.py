import matplotlib.pyplot as plt
import math

file = open('dataset_TSMC2014_NYC.txt', 'r')
fileWrite = open('dataset.txt', 'w')

def find(worker, name):
	for index, s in enumerate(worker):
		if s == name:
			return index
	return -1

worker = []
x = []
y = []


for line in file:
	data = [s for s in line.split('\t')]
	position = find(worker, data[0])
	if position == -1 and float(data[4]) >= 40.75 and float(data[5]) <= -74.0:
		worker.append(data[0])
		x.append(float(data[4]))
		y.append(float(data[5]))
		write = data[0]+'\t'+data[4]+'\t'+data[5]+'\n'
		fileWrite.write(write)

print(len(worker)) 

plt.scatter(x, y, color = 'green')
plt.show()

