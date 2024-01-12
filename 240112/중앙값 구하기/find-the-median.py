a,b,c = map(int, input().split())
if (b<=a and a<=c) or (c<=a and a<=b):
    print(a)
elif (a<=b and b<=c) or (c<=b and b<=a):
    print(b)
else:
    print(c)