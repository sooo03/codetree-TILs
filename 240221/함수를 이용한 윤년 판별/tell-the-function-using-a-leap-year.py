function leap_year(y)
    if y % 4 != 0
        return false
    if y % 100 != 0
        return true
    if y % 400 == 0
        return true
    return false