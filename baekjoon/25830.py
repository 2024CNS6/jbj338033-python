h,m=map(int,input().split(':'))
s=(h*3600+m*60)-h*60-m
print(f'{s//3600:02}:{s%3600//60:02}:{s%3600%60:02}')