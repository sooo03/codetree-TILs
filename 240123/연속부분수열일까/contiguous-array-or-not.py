n1, n2 = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

idx = 0
for i in range(n1):
    if arr[i] == brr[0]:
        idx = i
        break

result = 0
for i in range(idx, min(idx + n2, n1)):
    if arr[i] != brr[i - idx]:
        result = 1
        break

if result == 0:
    print("Yes")
else:
    print("No")