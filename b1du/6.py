a=input().split()
s=0
print(len(a))
for i in a:s+=ord(i[0])-96
print(s)