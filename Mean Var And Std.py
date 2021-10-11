import numpy as np

m,n=map(int,input().split())
l=[]

for i in range(m):
    l.append(list(map(int,input().split())))


print(np.mean(np.array(l),axis=1))
print(np.var(np.array(l),axis=0))
print(round(np.std(np.array(l)),11))
