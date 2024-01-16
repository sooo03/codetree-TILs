arr = list(map(int, input().split()))
sum_even = arr[1]+arr[3]+arr[5]+arr[7]+arr[9]
sum_three = arr[2]+arr[5]+arr[8]
print(f"{sum_even} {(sum_three/3):.1f}")