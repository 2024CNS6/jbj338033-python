import math
n = int(input())
l = 1
r = 1000000
while l <= r:
    m=(l+r)//2
    f=math.factorial(m)
    if f==n:
        print(m)
        break
    elif f<n:
        l=m+1
    else:
        r=m-1