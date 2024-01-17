a, b = map(int, input().split())
arr = [a, b]

for i in range(8):
    arr.append(arr[-1] + arr[-2]*2)

print(*arr)