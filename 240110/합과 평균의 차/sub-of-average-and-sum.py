a, b, c = map(int, input().split())

s = a+b+c
mean = s // 3

print(f"{s}\n{mean}\n{s-mean}")