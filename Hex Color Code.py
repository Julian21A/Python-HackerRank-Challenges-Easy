import re

n = int(input())
llaves = False
for i in range(n):
    dato = input()
    if '{' in dato:
        llaves = True
    elif '}' in dato:
        llaves = False
    elif llaves:
        for color in re.findall('#[0-9a-fA-F]{3,6}', dato):
            print (color)
