# G0 = 0
# G1 = 1
# G2 = 1
# G3 = 2
# G4 = 2
# G5 = 2
# G6 = 3
# 1 1 2 2 2 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5

dp=[0]*1000001
c=1
for i in range(1,447):
    n=i*(i+1)//2
    for j in range(c+1):dp[n+j]=c
    c+=1
n=int(input())
l=list(map(int,input().split()))
r=0
for i in range(n):
    r^=dp[l[i]]
print('koosaga' if r else 'cubelover')