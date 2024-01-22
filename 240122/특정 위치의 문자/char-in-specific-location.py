words = ['L','E','B','R','O','S']
x = input()
idx = -1

for i in range(len(words)):
    if words[i] == x:
        idx = i 

if idx == -1:
    print("None")
else:
    print(idx)