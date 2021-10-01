from itertools import product
a = input().split()
b = input().split()
a = list(map(int, a))
b = list(map(int, b))
print(*product(a, b))