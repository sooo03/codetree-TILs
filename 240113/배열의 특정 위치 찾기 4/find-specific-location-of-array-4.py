arr = list(map(int, input().split()))
sum_val, count = 0, 0
for i in arr:
    if i==0:
        break
    if i%2==0:
        count += 1
        sum_val += i 
print(f"{count} {sum_val}")