n = int(input())
arr = list(map(int, input().split()))
new_arr = []
for i in arr:
    new_arr.append(i*i)
print(*new_arr)