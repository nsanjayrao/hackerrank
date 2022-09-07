# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
a=defaultdict(list)
import sys
n=int(sys.stdin.readline())

for i in range(n):
    s=list(input().split())
    if len(s)>2:
        item=' '.join(s[0:2])
        price=int(s[2])
        a[item].append(price)
    else:
        item=s[0]
        price=int(s[1])
        a[item].append(price)

#print(a)
for i,j in a.items():
    
    print(i, sum(j),sep=' ')
    
    
