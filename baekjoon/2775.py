for _ in range(int(input())):
    k,n=map(int,(input(),input()))
    l=[i for i in range(1,n+1)]
    for i in range(k):
        for j in range(1,n):
            l[j]+=l[j-1]
    print(l[-1])