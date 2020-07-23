n=int(input("Enter the number to check whether it is prime or not"))
if n>1:
	for i in range(2,n):
		if (n%i==0):
			print(n," Is not a prime number")
			
		else:
			print(n,' Is a prime number')
			break
else:
			print(n,"Is not a Prime number")
			