n=int(input())
l=list(map(int,input().split()))
x=0
for i in l:x^=(i+1)//2 if i%2==1 else (i-2)//2
print("cubelover" if x == 0 else "koosaga")