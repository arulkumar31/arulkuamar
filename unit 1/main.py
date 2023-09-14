#1.1 implement a recursive function to calculate the factorial of a given number
def recur_factorial(n):
if n==1:
return n
else:
return n*recur_factorial(n-1)
#take input form the user
num =int(input(“enter a number:”))
#check is the number is negative
If num<0;
print(“Sorry, factorial does not exists for negative numbers”)
elif num==0:
print(“The factorial of”,num,”is”,recur_factorial(num))
