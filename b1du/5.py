m,s=map(int,input().split())
a=m/(s/60)
if m>=1000:
    print('%.2fkm/min'%(a/1000))
else:
    print('%.2fmin/km'%a)