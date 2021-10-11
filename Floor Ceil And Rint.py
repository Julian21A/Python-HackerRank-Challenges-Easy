import numpy as np

np.set_printoptions(sign=' ')
l=np.array(list(map(float,input().split())))

print(np.floor(l))
print(np.ceil(l))
print(np.rint(l))

