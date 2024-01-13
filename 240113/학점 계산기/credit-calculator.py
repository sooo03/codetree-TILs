n = int(input())
arr = list(map(float, input().split()))
sum_val = 0
for i in range(n):
    sum_val += arr[i]

avg = sum_val / n

if avg>=4.0:
    grade = "Perfect"
elif avg>=3.0:
    grade = "Good"
elif avg<3.0:
    grade = "Poor"

print(f"{avg:.1f}\n{grade}")