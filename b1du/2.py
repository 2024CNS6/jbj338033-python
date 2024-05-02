a=[]
b=[]
c=[]
d=[]
e=[]
for _ in range(int(input())):
    n,m=input().split()
    m=int(m)
    if m>=90:
        a.append(n)
    elif m>=80:
        b.append(n)
    elif m>=70:
        c.append(n)
    elif m>=60:
        d.append(n)
    else:
        e.append(n)
a.sort()
b.sort()
c.sort()
d.sort()
e.sort()
for i in a:
    print(i, 'A')
for i in b:
    print(i, 'B')
for i in c:
    print(i, 'C')
for i in d:
    print(i, 'D')
for i in e:
    print(i, 'E')