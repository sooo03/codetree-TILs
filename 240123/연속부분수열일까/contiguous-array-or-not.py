n1, n2 = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

result = 0
j = 0

for i in range(n1):
    if arr[i] == brr[j]:
        j += 1

    if j == n2:
        result = 1
        break

if result == 1:
    print("Yes")
else:
    print("No")