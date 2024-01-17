arr = list(map(int, input().split()))
new = []

for i in range(len(arr)):
    if arr[i] == 0:
        break
    if arr[i] % 2 != 0: #홀수
        new.append(arr[i]+3)
    if arr[i] % 2 == 0: #짝수
        new.append(arr[i]//2)

print(*new)