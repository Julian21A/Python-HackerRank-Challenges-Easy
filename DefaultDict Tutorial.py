from collections import defaultdict

dic = defaultdict(list)
n, m = map(int, input().split())

for i in range(n):
    dic[input()].append(str(i + 1))
for j in range(m):
    print(' '.join(dic[input()]) or -1)