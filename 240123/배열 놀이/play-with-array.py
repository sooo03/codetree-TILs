n, q = map(int, input().split())
element = list(map(int, input().split()))
first_ques, a1 = map(int, input().split())
second_ques, a2 = map(int, input().split())
third_ques, a3, b3 = map(int, input().split())

#1 a
print(element[a1-1])

#2 a
cnt = -1
for i in range(len(element)):
    if a2 != element[i]: #숫자 a가 없는 경우
        cnt = 0
    #숫자 a가 있는 경우
    else:
        cnt = i + 1
        break
print(cnt)

#3 a b
for i in range(a3-1, b3):
    print(element[i], end=' ')