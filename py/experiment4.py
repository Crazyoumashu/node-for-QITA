import os
import time
for i in range(0, 20):
	os.system(r'"C:\Users\ChenlinLiu\Desktop\py\generateQ.py"')
	time.sleep(1)
	os.system(r'"C:\Users\ChenlinLiu\Desktop\py\DP2.exe"')
	time.sleep(1)
	os.system(r'"C:\Users\ChenlinLiu\Desktop\py\taskAssignmentCBMQ.py"')

time.sleep(1)
os.system(r'"C:\Users\ChenlinLiu\Desktop\py\average.py"')
os.remove("C:/Users/ChenlinLiu/Desktop/py/output.txt")
###########################################################################
# 	os.system(r'"C:\Users\ChenlinLiu\Desktop\py\generateQ.py"')
# 	time.sleep(1)
# 	os.system(r'"C:\Users\ChenlinLiu\Desktop\py\DP.exe"')
# 	time.sleep(2)
# 	os.system(r'"C:\Users\ChenlinLiu\Desktop\py\taskAssignmentQBMC.py"')

# time.sleep(1)
# os.system(r'"C:\Users\ChenlinLiu\Desktop\py\average.py"')
# os.remove("C:/Users/ChenlinLiu/Desktop/py/output.txt")
###########################################################################
# os.system(r'"C:\Users\ChenlinLiu\Desktop\py\DP2.exe"')
# time.sleep(2)

# for i in range(0, 20):
# 	os.system(r'"C:\Users\ChenlinLiu\Desktop\py\generateQ.py"')
# 	os.system(r'"C:\Users\ChenlinLiu\Desktop\py\taskAssignmentCBMQ.py"')
# 	time.sleep(1)

# os.system(r'"C:\Users\ChenlinLiu\Desktop\py\average.py"')
# os.remove("C:/Users/ChenlinLiu/Desktop/py/output.txt")