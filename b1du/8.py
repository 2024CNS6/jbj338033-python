n=int(input())
oneline=n*(n**2+1)//2
s=0
l=[]
for _ in range(n):
    li=list(map(int,input().split()))
    l.append(li)
    a=sum(li)
    s+=a
    if a!=oneline:
        print('노영재 화이팅')
        exit()
for i in range(n):
    su=0
    for j in range(n):su+=l[j][i]
    if su!=oneline:
        print('노영재화이팅')
        exit()
print('제민국화이팅' if (n**2)*(n**2+1)//2 == s else '노영재화이팅')