def proper(a):
	sum=0
	for i in range(2,a):
		if a%i==0:
			sum=sum+i
	return sum+1
n=int(input("Enter first number"))
m=int(input("Enter second number"))
if n<=1 or m<=1:
	print("Invalid input")
else:
	if proper(n)==m and proper(m)==n:
		print("Yes")
	else:
		print("No")
