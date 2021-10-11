import itertools as it

a,k=(list(map(str,input().split())))

x=(sorted(list(it.combinations_with_replacement(sorted(a),int(k)))))
print(*[''.join(i) for i in x],sep='\n')