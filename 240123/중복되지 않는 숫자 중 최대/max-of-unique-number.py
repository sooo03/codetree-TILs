n = int(input())
arr = list(map(int, input().split()))

max_unique = float('-inf')

for num in arr:
    if arr.count(num) == 1 and num > max_unique:
        max_unique = num

if max_unique != float('-inf'):
    print(max_unique)
else:
    print(-1)