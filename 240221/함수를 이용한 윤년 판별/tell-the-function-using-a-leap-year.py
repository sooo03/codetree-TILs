year = int(input())

def leap_year(y)
    if y % 4 != 0
        return false
    if y % 100 != 0
        return true
    if y % 400 == 0
        return true
    return false

if leap_year(year):
    print("true")
else:
    print("false")