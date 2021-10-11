import re

s = input()
k = input()

pat = re.compile(k)
find = pat.search(s)

if not find: 
    print('(-1, -1)')
    
while find:
    print('({0}, {1})'.format(find.start(), find.end() - 1))
    find = pat.search(s, find.start() + 1)