import matplotlib.pyplot as plt
import math
import random
import numpy as np

# file = open('experiment6.txt', 'r')
# data = []
# for line in file:
# 	data.append([float(s) for s in line.split('\t')])

# x = [20, 30, 40, 50, 60, 70, 80]

# plt.plot(x, data[0], color = 'green', marker = '^', label = 'Budget = 400')
# plt.plot(x, data[1], color = 'red', marker = 'o', label = 'Budget = 450')
# plt.plot(x, data[2], color = 'skyblue', marker = 's', label = 'Budget = 500')
# plt.plot(x, data[3], color = 'blue', marker = '*', label = 'Budget = 550')
# plt.xlabel('Mean of qualities')
# plt.ylabel('Total quality')

# plt.legend()
# plt.show()

file = open('experiment7.txt', 'r')
data = []
for line in file:
	data.append([float(s) for s in line.split('\t')])

x = [400, 425, 450, 475, 500, 525, 550, 575, 600]
plt.plot(x, data[1], color = 'green', marker = 'o', label = 'Worker quality')
plt.plot(x, data[0], color = 'skyblue', marker = 's', label = 'Coverage quality')
plt.xlabel('Cost', fontsize = 18)
plt.ylabel('Total quality', fontsize = 18)
plt.legend(fontsize = 18)
plt.show()

# file = open('experiment5.txt', 'r')
# data = []
# for line in file:
# 	data.append([float(s) for s in line.split('\t')])

# x = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# y = [530, 1020, 1550, 2000, 2550, 3070, 3520, 4030, 4540, 5080]
# plt.plot(x, y, color = 'green', marker = 'o', label = 'Worker quality')
# plt.plot(x, data[3], color = 'skyblue', marker = 's', label = 'Coverage quality')
# plt.xlabel('Quality bound', fontsize = 18)
# plt.ylabel('Real total quality', fontsize = 18)
# plt.legend(fontsize = 18)
# plt.show()