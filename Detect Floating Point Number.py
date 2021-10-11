import re

for i in range(int(input())):
    print(str(bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$', input()))))