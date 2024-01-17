a, b = map(int, input().split())
arr = []
count = 0

while True:
    arr.append(a % b)
    a = a//b
    if a < 1:
        break
new_arr = [0] * len(arr)

for item in arr:
    new_arr[item] += 1

for value in new_arr:
    count += value * value
print(count)