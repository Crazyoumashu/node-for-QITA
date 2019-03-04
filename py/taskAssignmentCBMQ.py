import matplotlib.pyplot as plt
import math
import random
import numpy as np

# input data
file = open('dataset.txt', 'r')
worker = []
xw = []
yw = []
for line in file:
	data = [s for s in line.split('\t')]
	worker.append(data[0])
	xw.append(float(data[1]))
	yw.append(-float(data[2]))

#############################################################
# generate tasks
# 74.0 74.25 : 40.70 40.95
# 20 tasks, 15 redundancy
n = len(worker)
m = 10
R = 10
ymin = 74.0
ymax = 74.25
xmin = 40.75
xmax = 40.95
xt = []
yt = []
# for i in range(0, m):
# 	xt.append(np.random.rand()*(xmax-xmin)+xmin)
# 	yt.append(np.random.rand()*(ymax-ymin)+ymin)

fileTasks = open('tasks.txt', 'r')
for line in fileTasks:
	data = [float(s) for s in line.split('\t')]
	xt.append(data[0])
	yt.append(data[1])

# plt.scatter(xw, yw, color = 'green')
# plt.scatter(xt, yt, color = 'red')
# plt.show()

#############################################################
# calculate cost
# c = base+dist*bonus
def dist(xw, yw, xt, yt):
	return math.sqrt((xw-xt)*(xw-xt)+(yw-yt)*(yw-yt))

base = 1.0
bonus = 100
c = []
for i in range(0, m):
	c.append([])
	for j in range(0, n):
		c[i].append(base+bonus*dist(xw[j], yw[j], xt[i], yt[i]))


#############################################################
# MWM
# minimum complete matching
# km algorithm
# left: m*R  right: n

# calculate new cost
cMWM = []
maxCost = base+bonus*dist(xmin, ymin, xmax, ymax)
for i in range(0, m):
	for k in range(0, R):
		cMWM.append([])
	for j in range(0, n):
		for k in range(0, R):
			cMWM[i*R+k].append(int((maxCost-c[i][j])*100))

#############################################################
# km algorithm
global taskExpectaion	# task expectation
global workerExpectation	# worker expectaion
global taskVisited
global workerVisited
global assignedWorker # assigned worker for each task
global slackWorker
taskExpectaion = []	# task expectation
workerExpectation = []	# worker expectaion
taskVisited = []
workerVisited = []
assignedTask = [] # assigned task for each worker
slackWorker = []
INF = 99999

def dfs(task):

	global taskExpectaion	# task expectation
	global workerExpectation	# worker expectaion
	global taskVisited
	global workerVisited
	global assignedWorker # assigned worker for each task
	global slackWorker

	taskVisited[task] = True

	for worker in range(0, n):
		if workerVisited[worker] == True:
			continue
		gap = taskExpectaion[task] + workerExpectation[worker] - cMWM[task][worker]
		if gap == 0:
			workerVisited[worker] = True
			if assignedTask[worker] == -1 or dfs(assignedTask[worker]):
				assignedTask[worker] = task
				return True
		else:
			slackWorker[worker] = min(slackWorker[worker], gap)

	return False

# initialization
for i in range(0, n):
	assignedTask.append(-1)
	workerExpectation.append(0)
	workerVisited.append(False)
	slackWorker.append(INF)
for i in range(0, m*R):
	taskExpectaion.append(0)
	taskVisited.append(False)
for i in range(0, m*R):
	taskExpectaion[i] = cMWM[i][0]
	for j in range(0, n):
		taskExpectaion[i] = max(taskExpectaion[i], cMWM[i][j])

# find worker for each task

for i in range(0, m*R):

	for t in range(0, n):
		slackWorker[t] = INF

	while True:

		for t in range(0, n):
			workerVisited[t] = False
		for t in range(0, m*R):
			taskVisited[t] = False

		if dfs(i) == True:
			break

		d = INF
		# lower the expactation
		for j in range(0, n):
			if workerVisited[j] == False:
				d = min(d, slackWorker[j])

		for j in range(0, m*R):
			if taskVisited[j] == True:
				taskExpectaion[j] -= d

		for j in range(0, n):
			if workerVisited[j] == True:
				workerExpectation[j] += d
			else:
				slackWorker[j] -= d



#############################################################
# km result: assignedTask
# dp
# calculate new cost for dp
cDP = []
cmax = 0
for i in range(0, m):
	cDP.append([])
	for j in range(0, n):
			cDP[i].append(int((c[i][j])))

costFile = open('cost.txt', 'w')
for i in range(0, m):
	for j in range(0, n):
		costFile.write(str(cDP[i][j])+'\t')
	costFile.write('\n')

workerOutput = open('restWorkers.txt', 'w')
restWorkers = []
res = 0
for j in range(0, n):
	if assignedTask[j] != -1:
		res += cDP[int(assignedTask[j]/R)][j]
	else:
		workerOutput.write(str(j) + '\t')
workerOutput.write(str(res))

#############################################################
# input DP result
assignedTaskDP = [-1 for j in range (0, n)]
fileDPresult = open('DPresult.txt', 'r')
for line in fileDPresult:
	data = [int(s) for s in line.split('\t')]
	assignedTaskDP[data[1]] = data[0]


# #############################################################
# combining step

assignedTaskFinal = [-1 for j in range (0, n)]

for j in range(0, n):
	if assignedTask[j] != -1:
		assignedTaskFinal[j] = int(assignedTask[j]/R)
		continue
	if assignedTaskDP[j] != -1:
		assignedTaskFinal[j] = assignedTaskDP[j]

res = 0
for j in range(0, n):
	if assignedTaskFinal[j] != -1:
		res += c[assignedTaskFinal[j]][j]

file = open('q.txt','r')
for line in file:
	q = [int(s) for s in line.split('\t')]

resQ = 0
for j in range(0, n):
	if assignedTaskFinal[j] != -1:
		resQ += q[j]

output = open('output.txt', 'a')
output.write(str(resQ)+'\t')