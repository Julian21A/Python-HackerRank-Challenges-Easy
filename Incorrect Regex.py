import re
for i in range(int(input())):
    output = True
    try:
        regex = re.compile(input())
    except re.error:
        output = False
    print(output)