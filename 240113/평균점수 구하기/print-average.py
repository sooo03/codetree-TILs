arr = list(map(float, input().split()))
avg = 0
for i in arr:
    avg += i
avg /= 8
print(f"{avg:.1f}")