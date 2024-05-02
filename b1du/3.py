n=input()
s=0
for _ in range(int(input())):
    a=input()
    s+=1
    if n in a:
        s+=1
print(s)