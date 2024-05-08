n=int(input())

for i in range(n):
    if i==0:
        print(' '*(n-i-1)+'*'+' '*(2*i-1)+'*'*(i!=0))
    elif i==n-1:
        print('*'*(2*n-1))
    else:
        print(' '*(n-i-1)+'*'+' '*(2*i-1)+'*'+' '*(n-i-1))