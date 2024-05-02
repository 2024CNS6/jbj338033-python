from collections import deque
n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
result=[deque([]) for _ in range(n)]

for i in range(n):
    for j in range(n):
        result[j].appendleft(l[i][j])

for i in result:
    print(*i)
