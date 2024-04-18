n, x = map(int, input().split())
print(*list(map(str, filter(lambda a: a < x, map(int, input().split())))))