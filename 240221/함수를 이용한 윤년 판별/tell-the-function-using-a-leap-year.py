year = int(input())

def leap_year(y)
    if y % 4 != 0
        return False
    if y % 100 != 0
        return Ture
    if y % 400 == 0
        return True
    return false

if leap_year(year):
    print("true")
else:
    print("false")