import numpy as np
import matplotlib.pyplot as plt
import math

global truth
truth = 5

def sense(mu, sigma, round): 
	data = np.random.normal(mu, sigma, round)
	return data

def inferData(data, q, k, redundancy):
	sum1 = 0
	sum2 = 0
	for i in range(0, redundancy):
		sum1 += data[i][k]*q[i]
		sum2 += q[i]
	return sum1/sum2

def inferQuality(data, y, j, labda):
	sum1 = 0
	for k in range(0, labda):
		sum1 += ((data[j][k]-y[k])*(data[j][k]-y[k]))
	return labda/sum1

def converge(y, yLast, labda):
	difference = 0
	for k in range(0, labda):
		difference += (y[k]-yLast[k])*(y[k]-yLast[k])
	difference /= labda
	if difference <= 0.0001:
		return True
	else:
		return False

def deviation(y, labda):
	sum1 = 0
	for item in y:
		sum1 += (item-truth)*(item-truth)
	sum1 /= labda
	return sum1


def truthInference(redundancy, labda):
	dataList = []
	badWorker = 1
	normalWorker = 0.1
	goodWorker = 0.01

	#initialization
	for i in range(0, int(redundancy/3)):
		dataList.append(sense(truth, badWorker, labda))
	for i in range(int(redundancy/3), int(redundancy/3)*2):
		dataList.append(sense(truth, normalWorker, labda))
	for i in range(int(redundancy/3)*2, redundancy):
		dataList.append(sense(truth, goodWorker, labda))

	q = []
	for j in range(0, redundancy):
		q.append(1)
	y = []
	for k in range(0, labda):
		y.append(truth)

	yLast = []
	qLast = []

	while True:
		for item in q:
			qLast.append(item)
		for item in y:
			yLast.append(item)

		for k in range(0, labda):
			y[k] = inferData(dataList, q, k, redundancy)
		for j in range(0, redundancy):
			q[j] = inferQuality(dataList, y, j, labda)

		if(converge(y, yLast, labda)):
			break

	return deviation(y, labda)

def qualityInference(redundancy, labda):
	dataList = []
	badWorker = 1
	normalWorker = 0.1
	goodWorker = 0.01

	#initialization
	for i in range(0, int(redundancy/3)):
		dataList.append(sense(truth, badWorker, labda))
	for i in range(int(redundancy/3), int(redundancy/3)*2):
		dataList.append(sense(truth, normalWorker, labda))
	for i in range(int(redundancy/3)*2, redundancy):
		dataList.append(sense(truth, goodWorker, labda))

	q = []
	for j in range(0, redundancy):
		q.append(1)
	y = []
	for k in range(0, labda):
		y.append(truth)

	yLast = []
	qLast = []

	while True:
		for item in q:
			qLast.append(item)
		for item in y:
			yLast.append(item)

		for k in range(0, labda):
			y[k] = inferData(dataList, q, k, redundancy)
		for j in range(0, redundancy):
			q[j] = inferQuality(dataList, y, j, labda)

		if(converge(y, yLast, labda)):
			break

	return q

accuracy = []
sumA = 0
times = 100

# for i in range(2, 11):
# 	for index in range (0, times):
# 		sumA += truthInference(i*3, 100)
# 	sumA /= times
# 	accuracy.append(sumA)

# for i in range (1, 11):
# 	for index in range (0, times):
# 		sumA += truthInference(20, i*10)
# 	sumA /= times
# 	accuracy.append(sumA)

# print(accuracy)

redundancy = 30
labda = 50
qFinal = []
for j in range(0, redundancy):
	qFinal.append(0)

for index in range(0, times):
	qTemp = qualityInference(redundancy, labda)
	print(qTemp)
	for j in range(0, redundancy):
		qFinal[j] += qTemp[j]

for j in range(0, redundancy):
	qFinal[j] /= times
	qFinal[j] = math.sqrt(qFinal[j])

print(qFinal)

	






# dataList = []
# redundancy = 10
# labda = 10
# badWorker = 1
# normalWorker = 0.1
# goodWorker = 0.01

# for i in range(0, int(redundancy/3)):
# 	dataList.append(sense(truth, badWorker, labda))
# for i in range(int(redundancy/3), int(redundancy/3)*2):
# 	dataList.append(sense(truth, normalWorker, labda))
# for i in range(redundancy-int(redundancy/3)*2+1, redundancy):
# 	dataList.append(sense(truth, goodWorker, labda))
# # print(dataList)
# # print(dataList[0][0])

# #initialization
# q = []
# for j in range(0, redundancy):
# 	q.append(1)
# y = []
# for k in range(0, labda):
# 	y.append(truth)



# yLast = []
# qLast = []
# count = 0
# while True:
# 	count = count+1
# 	for item in q:
# 		qLast.append(item)
# 	for item in y:
# 		yLast.append(item)

# 	for k in range(0, labda):
# 		y[k] = inferData(dataList, q, k, redundancy)
# 	for j in range(0, redundancy):
# 		q[j] = inferQuality(dataList, y, j, labda)

# 	if(converge(y, yLast, redundancy)):
# 		break


# print(y)
# print(q)
# print(count)
# print(deviation(y))
# print(count)




