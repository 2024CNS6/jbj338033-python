x=int(input())
c=0 #cnt
l=0 #len
m=32 #min
while l!=x:
    if x-l>=m:
        l+=m
        c+=1
    m/=2
    if m<1:break
print(c)