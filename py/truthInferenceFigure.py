import numpy as np
import matplotlib.pyplot as plt
from functools import reduce  

file = open("experiment0.txt", "r")

dataString = []
dataLine = []
data = []
for line in file:
	dataLine = []
	dataString = [s for s in line.split(" ")]
	dataString[7] = dataString[7].replace('\n', '')
	for d in dataString:
		dataLine.append(float(d))
	data.append(dataLine)

x = [9, 12, 15, 18, 21, 24, 27, 30]
plt.plot(x, data[0], color = 'red', label = 'Sensing times = 20', marker = 'o')
plt.plot(x, data[1], color = 'green', label = 'Sensing times = 40', marker = 'v')
plt.plot(x, data[2], color = 'skyblue', label = 'Sensing times = 60', marker = '^')
plt.plot(x, data[3], color = 'blue', label = 'Sensing times = 80', marker = 's')
plt.plot(x, data[4], color = 'black', label = 'Sensing times = 100', marker = '*')
plt.xlabel('Number of workers')
plt.ylabel('Square deviation error (e-05)')
plt.legend()
plt.show()

# file = open('experiment2.txt', 'r')

# line = file.read()
# data = [float(s) for s in line.split(" ")]
# x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# plt.plot(x, data, color = 'red', label = 'Number of workers = 20', marker = 's')
# plt.xlabel('Sensing times')
# plt.ylabel('Square deviation error (e-05)')
# plt.ylim(1, 6)
# plt.legend()
# plt.show()