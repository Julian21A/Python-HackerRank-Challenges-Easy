# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
for i in range(n):
    s=''.join(sorted(input().strip()))
    if s.isalnum() and len(s)==10: 
        m = not(re.search(r'([a-zA-Z0-9])\1+',s)) and re.search(r'[0-9]{3}',s) and re.search('[A-Z]{2}',s)
        if m: print('Valid')
        else: print('Invalid') 
    else: print('Invalid')

