for _ in range(int(input())):
    y=0
    k=0
    for _ in range(9):
        a,b=map(int,input().split())
        y+=a
        k+=b
    print('Yonsei' if y>k else 'Korea' if y<k else 'Draw')