n=int(input())
set1=set(map(int,input().split()))
n2=int(input())
set2=set(map(int,input().split()))

setin=set1.symmetric_difference(set2)
print(len(setin))