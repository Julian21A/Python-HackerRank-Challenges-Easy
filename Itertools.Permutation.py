import itertools as it

x=list(map(str,input().split()))
permutacion=sorted(list(it.permutations(list(x[0]),int(x[1]))))

print(*[''.join(i) for i in permutacion],sep='\n')