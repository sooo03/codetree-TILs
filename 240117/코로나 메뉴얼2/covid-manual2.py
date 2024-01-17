count_arr = [0] * 5

for _ in range(3):
	s, t = input().split()
	t = int(t)

	if t >= 37 and s == 'Y':
		type_num = 1;
	elif t >= 37:
		type_num = 2;
	elif s == 'Y':
		type_num = 3;
	else:
		type_num = 4;
		
	count_arr[type_num] += 1
	
for i in range(1, 5):
	print(count_arr[i], end=" ")
	
if count_arr[1] >= 2:
	print("E")