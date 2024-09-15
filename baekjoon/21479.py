import sys

input = sys.stdin.readline

l = []
while 1:
    try:
        l.append(input().rstrip())
    except:
        break
m = 0
for d in l:
    m = max(m, len(d))
m *= 2
a = []
for d in l:
    q = d * (m // len(d))
    for i in range(m % len(d)):
        q += d[i]
    a.append((q, len(d)))
a.sort(reverse=True)
r = ""
for n, l in a:
    for i in range(l):
        r += n[i]

print(0 if r[0] == "0" else r)
