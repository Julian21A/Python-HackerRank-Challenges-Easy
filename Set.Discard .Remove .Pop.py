n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    accion = input().split()
    if accion[0] == 'pop':
        s.pop()
    elif accion[0] == 'remove':
        s.remove(int(accion[1]))
    elif accion[0] == 'discard':
        s.discard(int(accion[1]))   
print (sum(s))
