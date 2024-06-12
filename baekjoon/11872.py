# G0 = 0
# G1 = 1
# G2 = 2
# G3 = 4
# G4 = 3
# 0 1 2 4 3 5 6 8 7 9 10 21 11

# 1 2 4 3
# 5 6 8 7

n=int(input())
l=list(map(int,input().split()))
r=0
for i in l:
    if i%4==0:i-=1
    elif i%4==3:i+=1
    r^=i
print('koosaga' if r else 'cubelove')