n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]
result = 0

for x in range(0, n-2):
    for y in range(0, n-2):
        key = 0
        for i in range(3):
            for j in range(3):
                if array[x+i][y+j] == 1:
                    key += 1    
        result = max(result, key)
print(result)