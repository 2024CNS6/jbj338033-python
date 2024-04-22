n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)
for i in range(n):
    if i==0:continue
    print(' '*i+'*'*(n-i))