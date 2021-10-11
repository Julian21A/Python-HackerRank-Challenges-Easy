if __name__ == '__main__':
    N = int(input())
    
    arr= []
    
    for i in range(0,N):
        
        intento=input().split()
        
        if intento[0]=='insert':
            arr.insert(int(intento[1]), int(intento[2]))
        elif intento[0]=='print':
            print (arr)
        elif intento[0]=='remove':
            arr.remove(int(intento[1]))
        elif intento[0]=='append':
            arr.append(int(intento[1]))
        elif intento[0]=='sort':
            arr.sort()
        elif intento[0]=='pop':
            arr.pop(-1)
        elif intento[0]=='reverse':
            arr.reverse()
    