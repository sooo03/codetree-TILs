given1 = input()
given2 = input().split()

even_arr = []
for i in given2:
    if int(i) % 2 == 0:
        even_arr.append(i)

rev_arr = even_arr[::-1]
for e in rev_arr:
    print(e, end=" ")