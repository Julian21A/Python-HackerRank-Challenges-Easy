from typing import NewType
import numpy as np

def arrays(arr):
    return np.flip(np.array(arr,float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)