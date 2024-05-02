word='양예성'*1000000
wjsdnwls=''
dbstpdnr=''
turn=0
for i in range(int(input())):
    if turn:
        wjsdnwls += word[i]
        turn = 0
    else:
        dbstpdnr += word[i]
        turn = 1
print(f'전우진 : {dbstpdnr}')
print(f'윤세욱 : {wjsdnwls}')