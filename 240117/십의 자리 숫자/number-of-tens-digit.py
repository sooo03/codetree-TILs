arr = list(map(int, input().split()))
count = [0] * 10

for elem in arr:
    if elem == 0:
        break
    if elem < 10:
        continue
    count[elem//10] += 1

for i in range(1, 10):
    print(f"{i} - {count_arr[i]}")