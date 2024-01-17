n = int(input())
arr = [1, n]
sum_val = 0

for i in range(100):
    if sum_val > 100:
        break
    arr.append(arr[-1]+arr[-2])
    sum_val += arr[i]

print(*arr)