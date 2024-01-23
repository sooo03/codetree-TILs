n, m = map(int, input().split())
word = list(map(int, input().split()))
cnt = 0

for char in word:
    if char == m:
        cnt += 1
print(cnt)