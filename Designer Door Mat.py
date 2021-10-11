N,M = map(int,input().split())

for x in range(1,N,2):
    print(('.|.'*x).center(M,'-'))
print('WELCOME'.center(M,'-'))
for x in range(N-2,-1,-2):
    print(('.|.'*x).center(M,'-'))