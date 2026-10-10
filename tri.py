for i in range(1,4):
	for j in range(0,i):
		print("*",end='');
	print("");


for i in range(1,4):
	for j in range(4-i,1,-1):
		print("*",end='');
	print("");

print("")

for i in range(1,4):
	for j in range(4-i,1,-1):
		print(" ",end='');
	for j in range(2*i,1,-1):
		print("*",end='')
	print("")


for i in range(1,3):
	for j in  range(0,i):
		print(" ",end='')
	for j in range(1,(3-i)*2):
		print("*",end='')
	print("")

