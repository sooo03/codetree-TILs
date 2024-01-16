arr = list(map(int, input().split()))
sum_val = 0
for i in range(len(arr)):
    if arr[i] == 0:
        break
    sum_val += arr[i]
print(sum_val)