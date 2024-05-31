import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def dfs(v):
    global c
    visited[v]=c
    for i in graph[v]:
        if not visited[i]:
            c+=1
            dfs(i)
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
c=1
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()
dfs(r)
for i in range(1,n+1):
    print(visited[i])