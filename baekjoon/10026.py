from collections import deque
def bfs(x,y,c):
	q=deque()
	q.append((x,y))
	while q:
		x,y=q.popleft()
		if not visited[x][y]:
			visited[x][y]=1
			for i in range(4):
				nx,ny=x+d[i][0],y+d[i][1]
				if 0<=nx<n and 0<=ny<n:
					if graph[nx][ny]==c:q.append((nx,ny))		
n=int(input())
d=(0,1),(0,-1),(1,0),(-1,0)
graph=[[]*n for _ in range(n)]
visited=[[0]*n for _ in range(n)]
for i in range(n):
	for j in input():graph[i].append(j)
c1=0
for i in range(n):
	for j in range(n):
		if not visited[i][j]:
			c=graph[i][j]
			bfs(i,j,c)
			c1+=1
visited=[[0]*n for _ in range(n)]
for i in range(n):
	for j in range(n):
		if graph[i][j]=='G':graph[i][j]='R'
c2=0
for i in range(n):
	for j in range(n):
		if not visited[i][j]:
			c=graph[i][j]
			bfs(i,j,c)
			c2+=1
print(c1,c2)