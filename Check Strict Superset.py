A = set(input().split())
print(all(A > set(input().split()) for i in range(int(input()))))