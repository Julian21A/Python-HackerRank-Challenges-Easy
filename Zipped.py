x=list(map(int,input().split()))
b = [map(float, input().split()) for i in range(x[1])]
notasxestu=zip(*b)
notas=list(notasxestu)

i=0
while i<x[0]:
    promedio=(float(sum(notas[i]))/((x[1])))
    i+=1
    print(promedio)
