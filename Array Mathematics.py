import numpy

m,n=map(int,input().split())
a=[]
b=[]
for i in range(m):
    a.append(list(map(int,input().split())))
for j in range(m):    
    b.append(list(map(int,input().split())))

a=numpy.array(a)
b=numpy.array(b)

print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))