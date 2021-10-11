import numpy as np

n=int(input())
l=[]
m=[]
for i in range(n):
        l.append(list(map(int,input().split())))
for i in range(n):
        m.append(list(map(int,input().split()))) 
        
print(np.dot(np.array(l),np.array(m)))