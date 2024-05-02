l=0
for _ in range(int(input())):
    l+=int(input())
if 4700<=l and l<=5000:
    print('당신은 인간 저울이군.')
elif l==0:
    print('장난해?')
else:
    print('이 감자 네가 다 먹고 다시 가져와.')