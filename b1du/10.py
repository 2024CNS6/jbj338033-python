cnt=0
for _ in range(int(input())):
    a=input().lstrip()
    
    s=a.split('>')
    if s[1]=='':del s[1]
    firsttag=s[0]+'>'

    if len(s) == 1:
        if firsttag.startswith('</'):
            cnt-=2
        else:
            firsttag = firsttag[1:-1]
            print((' '*cnt)+firsttag+':')
            cnt+=2
    else:
        firsttag = firsttag[1:-1]
        value,_ = s[1].split('<')
        print((' '*cnt)+firsttag+': "'+value+'"')

# O