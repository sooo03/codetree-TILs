arr = list(map(int, input().split()))

for i in range(1, 7):
    cnt = 0
    for elem in arr:
        if elem == i:
            cnt += 1
    print(f"{i} - {cnt}")