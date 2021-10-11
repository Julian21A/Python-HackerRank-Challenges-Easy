n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    accion = input().split()
    secondset=set(map(int,input().split()))
    if accion[0] == 'intersection_update':
        s.intersection_update(secondset)
    elif accion[0] == 'update':
        s.update(secondset)
    elif accion[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(secondset)
    elif accion[0] == 'difference_update':
        s.difference_update(secondset)
print (sum(s))