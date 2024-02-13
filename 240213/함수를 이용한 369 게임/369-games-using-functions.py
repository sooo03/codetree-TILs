a, b = map(int, input().split())

def is_369(n, m):
    num = []
    for i in range(n, m+1):
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            num.append(i)
    return len(num)

print(is_369(a, b))