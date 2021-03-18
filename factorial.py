import time
f=int(input())
startTime=time.time()
fa=f+1
x=1
for i in range(1, fa):
    x=i*x
print("факториал=",x)
print("Time:",time.time()-startTime)
