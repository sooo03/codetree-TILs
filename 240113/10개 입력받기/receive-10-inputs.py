arr = list(map(int, input().split()))
result = []
sum_val, cnt = 0, 0
for i in range(len(arr)):
    cnt += 1
    if arr[i] == 0:
        avg = sum_val / (cnt - 1)
        break
    else:
        sum_val += arr[i]
print(f"{sum_val} {avg:.1f}")