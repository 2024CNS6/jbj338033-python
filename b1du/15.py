n,m,k=map(int,input().split())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())

l=[[0] * n for _ in range(m)]
visited=[[0] * n for _ in range(m)]

visited[y2][x2] = 1

for _ in range(k):
    x3,y3=map(int,input().split())
    visited[y3][x3] = 1

for i in visited:
    print(*i)