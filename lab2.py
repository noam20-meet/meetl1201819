number=(int(input"write a number"))
is_prime=True
for i in range(2,number):
 	if number%i==0:
        is_prime=False
if is_prime==True:
	print("your number is prime")
if is_prime==False:
	print("your number isn't prime")







