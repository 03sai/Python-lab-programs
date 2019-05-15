def recur_factorial(n):
    if(n==0):
        return 1
    else:
        return n*recur_factorial(n-1)
print("Factorial using recursion")
n=int(input("Enter a number:"))
print("The factorial of",n,"is",recur_factorial(n))
