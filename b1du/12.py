l=list(map(int,input().split()))
l.sort()
c=0
for i in range(len(l)):
    print(l[-i-1],end=' ')
    c+=1

    if c==2:
        print()
        c=0

print('호준이')

# ?