n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)

line = [0] * n

def happy_sequence():
    same_cnt = 1

    for i in range(1, n):
        if same_cnt == m:
            return True
        if line[i-1] == line[i]:
            same_cnt += 1 
        else:
            same_cnt = 1
    return False

happy_cnt = 0

# 가로로 행복한 수열 
for r in range(n):
    line = graph[r][:]
    # print("가로")
    # print(line)

    if happy_sequence():
        print(r) #가로
        happy_cnt += 1

# 세로로 행복한 수열
line = [0] * n
for c in range(n):
    for r in range(n):
        line[r] = graph[r][c]     # 세로로 숫자들을 모아 새로운 수열 만들기
    # print("세로")
    # print(line)
    
    if happy_sequence():
        print(c) #세로
        happy_cnt += 1

print(happy_cnt)