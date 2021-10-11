import itertools as it

a=list(map(int,input().split()))
b=list(map(int,input().split()))

#axb=([(i,j)for i in a for j in b])
axb=((list(it.product(a,b))))

for i in axb:
    print(i)