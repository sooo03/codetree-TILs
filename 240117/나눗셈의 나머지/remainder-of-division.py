a, b = map(int, input().split())
arr = []
new_arr = [0] * b
count = 0

while True:
    c = a % b
    arr.append(c)
    new_arr[c] += 1
    a = a // b
    if a <= 1:
        break

for elem in new_arr:
    count += elem ** 2

print(count)