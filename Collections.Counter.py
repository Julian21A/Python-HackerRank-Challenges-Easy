import collections

stockTotal= int(input())
#texto=input()
#arr=list(texto.split())
#intarr=[int(x) for x in arr]
counterInvetario = collections.Counter(map(int, input().split()))
compradores = int(input())

venta = 0

for i in range(0,compradores):
    talla, precio = map(int,input().split())
    if counterInvetario[talla]: 
        venta += precio
        counterInvetario[talla] -= 1
print (venta)
