cube = lambda x:x**3

def fibonacci(n):
    def fibon(n):
        if n<2:
            return n
        else:
            return fibon(n-1)+fibon(n-2)
    f=[]
    for i in range(n):
        x=fibon(i)
        f.append(x)
    return(f)
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))