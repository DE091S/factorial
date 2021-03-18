import time
def ran():
    x=1
    f=int(input(":"))
    startTime=time.time()
    fa=f+1
    for i in range(1, fa):
        x=i*x
    print("факториал=",x)
    print("Time:", time.time()-startTime)
ran()