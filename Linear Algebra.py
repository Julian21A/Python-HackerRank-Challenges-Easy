import numpy as np

n=int(input())
a=[]
for i in range(n):
    a.append(list(map(float,input().split())))
    
print(round(np.linalg.det(np.array(a)),2))
