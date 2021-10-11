if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if n>=2 and n<=10:
        arr=set(arr)
        lista=sorted(list(arr))
        print(lista[-2])