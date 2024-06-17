n,r,c=map(int,input().split())

def f(n,r,c):
    if n==0:return 0
    m=2**(n-1)
    if r<m:
        if c<m:return f(n-1,r,c)
        else:return m*m+f(n-1,r,c-m)
    else:
        if c<m:return 2*m*m+f(n-1,r-m,c)
        else:return 3*m*m+f(n-1,r-m,c-m)
print(f(n,r,c))
