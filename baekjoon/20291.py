d={}
for _ in range(int(input())):
    s=input().split('.')[1]
    d[s]=d.get(s,0)+1
l=list(d.items())
l.sort(key=lambda i:i[0])
for i in l:
    print(*i)