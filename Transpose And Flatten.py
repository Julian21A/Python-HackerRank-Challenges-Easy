import numpy as np

m,n=map(int,input().split())
l=[]
for i in range(m):
    l.append(list(map(int,input().split())))
 
print(np.transpose(np.array(l)))
print(np.array(l).flatten())
