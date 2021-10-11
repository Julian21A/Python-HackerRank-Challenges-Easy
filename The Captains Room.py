import collections as c

n=int(input())
room=c.Counter(sorted((list(map(int,input().split())))))

for i in room:
    if room[i]==1:
        print (i)
