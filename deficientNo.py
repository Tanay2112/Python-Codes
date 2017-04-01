n=int(input("Enter number to be checked"))
sum=0
for i in range(2,n):
	if n%i==0:
		sum=sum+i
if sum<n:
	print("Deficient")
else:
	print("Not deficient")