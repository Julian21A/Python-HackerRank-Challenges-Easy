import re

s=input().strip()
m = re.search(r'([a-zA-Z0-9])\1+',s)

if m: print (m.group(1))
else: print(-1)
