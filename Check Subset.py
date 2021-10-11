for i in range(int(input())):
    lena = int(input())
    conjuntoa = set(map(int, input().split()))
    lenb = int(input())
    conjuntob = set(map(int, input().split()))

    if (conjuntoa.issubset(conjuntob)):
        print("True")
    else:
        print("False")
        