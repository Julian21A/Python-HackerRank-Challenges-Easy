from collections import namedtuple

n = int(input())
cols = input().split()

suma = 0
for i in range(n):
    name = namedtuple('student',cols)
    col1,col2,col3,col4 = input().split()
    name = name(col1,col2,col3,col4)
    suma += int(name.MARKS)
print(round((suma/n),2))