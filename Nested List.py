if __name__ == '__main__':
    estudiantesgrado=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        estudiantesgrado.append([name,score])
    
    valoresordenados=sorted(list(set([x[1]for x in estudiantesgrado])))
    segundomenor=valoresordenados[1]
    listamenores=[]
    
    for estudiante in estudiantesgrado:
        if segundomenor == estudiante[1]:
            listamenores.append(estudiante[0])
    
    for estudiante in sorted(listamenores):
        print(estudiante)