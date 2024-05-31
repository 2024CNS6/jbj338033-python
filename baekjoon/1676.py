n=int(input())
for i in range(2,n):
    n*=i
c=0
if n==0:print(0)
else:
    for i in str(n)[::-1]:
        if i=='0':c+=1
        else:break
    print(c)