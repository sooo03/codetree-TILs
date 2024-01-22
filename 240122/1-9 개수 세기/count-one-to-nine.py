n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, 10):
    for elem in arr:
        if elem == i:
            cnt += 1
    print(f"{cnt}")   
    cnt = 0