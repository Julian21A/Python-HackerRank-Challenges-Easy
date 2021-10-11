import numpy as np

l=(list(map(int,input().split())))
m=(list(map(int,input().split()))) 

print(np.inner(np.array(l),np.array(m)))
print(np.outer(np.array(l),np.array(m)))

