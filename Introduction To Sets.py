def average(array):
    y=sum(set(array))/len(set(array))
    return y
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)