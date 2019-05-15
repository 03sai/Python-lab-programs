def prime(lower,upper):
    for n in range(lower,upper):
        if n>1:
            for i in range(2,n):
                if(n%i)==0:
                    break
            else:
                print(n,"is prime number")
lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
prime(lower,upper)
