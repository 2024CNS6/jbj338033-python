n=int(input())
l=[input() for _ in range(n)]
k=int(input())
q='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
f=[]
s=0
p=[]
for i in l:
    t=[]
    t.extend(i)
    p.append(t)
    s+=int(i,36)
for i in q:
    v=0
    for j in p:
        t=''
        for n in j:
            if n==i:t+='Z'
            else:t+=n
        v+=int(t,36)
    f.append(v-s)
m=s+sum(sorted(f,reverse=True)[:k])
r=''
while m:
    r=q[m%36]+r
    m//=6
print(r if r else '0')