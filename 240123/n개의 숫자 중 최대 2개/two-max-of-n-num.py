n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=False)
print(arr[-1], arr[-2])