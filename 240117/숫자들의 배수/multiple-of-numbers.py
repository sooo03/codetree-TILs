n = int(input())
arr = []
count = 0

for i in range(10):
    arr.append(n*(i+1))
    if arr[i] % 5 == 0:
        count += 1
        if count == 2:
            break

print(*arr)