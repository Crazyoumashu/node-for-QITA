import numpy as np
import matplotlib.pyplot as plt

file = open('experiment3.txt', 'r')
line = file.read()
data = [float(s) for s in line.split(" ")]
data1 = data[0:10]
data2 = data[10:20]
data3 = data[20:30]

x1 = range(1, 11)
x2 = range(11, 21)
x3 = range(21, 31)
y1 = []
y2 = []
y3 = []
for i in range(0, 10):
	y1.append(1)
for i in range(10, 20):
	y2.append(10)
for i in range(20, 30):
	y3.append(100)


plt.scatter(x1, data1, color = 'red', label = 'Estimated qualities (1-10)')
plt.plot(x1, y1, color = 'black', label = 'q = 1')
plt.xlabel('Worker ID')
plt.ylabel('Quality')
plt.legend()
plt.ylim(0, 2)
plt.show()

# plt.scatter(x2, data2, color = 'green', label = 'Estimated qualities (11-20)')
# plt.plot(x2, y2, color = 'black', label = 'q = 10')
# plt.xlabel('Worker ID')
# plt.ylabel('Quality')
# plt.legend()
# plt.ylim(5, 15)
# plt.show()

# plt.scatter(x3, data3, color = 'skyblue', label = 'Estimated qualities (21-30)')
# plt.plot(x3, y3, color = 'black', label = 'q = 100')
# plt.xlabel('Worker ID')
# plt.ylabel('Quality')
# plt.legend()
# plt.ylim(80, 120)
# plt.show()
