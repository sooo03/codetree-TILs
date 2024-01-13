arr = list(map(int, input().split()))

new_arr = list()
sum_val, mean = 0, 0

for i in range(len(arr)):
    if arr[i] >= 250:
        break
    sum_val += arr[i]

if i != 0:
    mean = sum_val / i
else:
    mean = 0

print(f"{sum_val} {mean:.1f}")