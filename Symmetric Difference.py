n=int(input())
set1=set(map(int, input().split()))
n2=int(input())
set2=set(map(int, input().split()))

set3 = (set1.difference(set2))
set4 = (set2.difference(set1))

setfinal=set3.union(set4)

for i in sorted(list(setfinal)):
    print(i)