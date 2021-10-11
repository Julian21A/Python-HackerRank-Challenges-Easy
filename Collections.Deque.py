from collections import deque
n=int(input())
d = deque()

for _ in range(n):
    args = input().strip().split()
    if (args[0] == 'append'):
        d.append(args[1])
    elif (args[0] == 'appendleft'):
        d.appendleft(args[1])
    elif (args[0] == 'pop'):
        d.pop()
    elif (args[0] == 'popleft'):
        d.popleft()
    
print (' '.join(d))