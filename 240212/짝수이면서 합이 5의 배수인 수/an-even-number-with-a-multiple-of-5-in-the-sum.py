n = input()

def f(a):
    if (int(a[0]) + int(a[1]) % 5 == 0) and int(n) % 2 == 0:
        print("Yes")
    print("No")
        
f(n)