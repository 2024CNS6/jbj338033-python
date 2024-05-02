n=input('100 보다 작은 수를 입력해주세요 : ')

def is_prime(n):
    if n==1:
        return True
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
if len(n)>2:
    print("잘못된 입력입니다.")
else:
    a,b=map(int,n)
    print(f'십의 자리: {a}, 일의 자리: {b}')

    if is_prime(a) and is_prime(b):
        print('오늘은 행운이 가득해요!!!')
    elif is_prime(a) or is_prime(b):
        print('오늘의 운세는 보통입니다~ 화이팅!')
    else:
        print('오늘의 운세는 꽝..ㅠ 그래도 킵고잉~')