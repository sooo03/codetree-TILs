n1, n2 = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

result = "No"

for i in range(n1 - n2 + 1):
    if arr[i:i + n2] == brr:
        result = "Yes"
        break

print(result)