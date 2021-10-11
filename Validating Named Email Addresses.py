import re

n=int(input())
for i in range(n):
    texto=input()
    nombre,correo=texto.split(' ')
    caracteres="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(caracteres,correo)):
        print (nombre,correo)
