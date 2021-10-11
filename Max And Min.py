import numpy

n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
arr=numpy.array(l)

print(numpy.max(numpy.min(arr,axis=1)))