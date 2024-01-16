arr = list(map(int, input().split()))

odd_list = sum(arr[::2])
even_list = sum(arr[1::2])

print(abs(odd_list - even_list))