import itertools as it

a,k=(list(map(str,input().split())))

for i in range(1,(int(k)+1)):
    x=(sorted(list(it.combinations(sorted(a),i))))
    print(*[''.join(i) for i in x],sep='\n')