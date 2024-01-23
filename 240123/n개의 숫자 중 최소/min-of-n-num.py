n = int(input())
arr = list(map(int, input().split()))
min_val = arr[0]
cnt = 0

for i in range(n):
    if min_val > arr[i]:
        min_val = arr[i]

for elem in arr:
    if elem == min_val:
        cnt += 1

print(min_val, cnt)