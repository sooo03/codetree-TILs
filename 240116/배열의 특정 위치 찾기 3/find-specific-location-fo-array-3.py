arr = list(map(int, input().split()))
sum_val = 0
i = 0
while arr[i] != 0:
    sum_val += arr[i]
    i += 1
print(sum_val)