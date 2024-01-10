cm, kg = map(int, input().split())
m = cm * 0.01
bmi = int(kg // (m**2))

print(bmi)
if bmi >= 25:
    print("Obesity")