arr = list(map(int, input().split()))
sum_val, cnt = 0, 0

for i in arr:
    if i == 0:
        break
    sum_val += i
    cnt += 1
avg = sum_val / cnt

print(f"{sum_val} {avg:.1f}")