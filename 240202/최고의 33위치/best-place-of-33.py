# 재귀함수 기반의 백트래킹
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n) ]
max_sum=0

for x in range(0, n-2):
    for y in range(0, n-2):
        key = 0
        for i in range(3):
            for j in range(3):
                if array[x+i][y+j] == 1:
                    key += 1    
        max_sum= max(max_sum, key)
print(max_sum)