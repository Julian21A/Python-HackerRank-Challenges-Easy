import numpy as np
m,n,p=map(int, input().split())

a=[]
b=[]

for i in range(m):
    a.append(list(map(int,input().split())))
    
for j in range(n):
    b.append(list(map(int,input().split())))
    
print(np.concatenate((np.array(a),np.array(b))))