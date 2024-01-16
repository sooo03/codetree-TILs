arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        k = i
        break
print(arr[k-3] + arr[k-2] + arr[k-1])