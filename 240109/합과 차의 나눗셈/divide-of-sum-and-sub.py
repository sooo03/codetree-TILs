a, b = map(int, input().split())


result = (a + b) / (a - b)
rounded_result = round(result, 2)
print(rounded_result)