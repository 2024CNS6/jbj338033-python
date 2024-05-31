# n=int(input())
# f=[0,1]
# a=1000000//10*15
# for i in range(2,a):
#     f.append((f[i-1]+f[i-2])%1000000)
# print(f[n%a])

n=int(input())%1500000
a,b=1,1
for i in range(n-1):
    a,b=b,(a+b)%1000000
print(a)