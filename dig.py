dig=int(10)

while True:
	f=int(dig%10)
	r=dig/10
	se=int(r%10)
	s=f+se
	print("number is ",dig,"sum digits*3",s*3)
	if(s*3==dig):
		print("The nunber is",dig)
		break;
	dig=dig+1;	 
