class cal():
    def __init__(self ,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0:Exit")
    print("1:ADD")
    print("2:SUB")
    print("3:Mul")
    print("4:Div")

    choice=int(input("Enter choice:"))

    if choice==1:
        print("Result:",obj.add())

    elif choice==2:
        print("Result:",obj.sub())

    elif choice==3:
        print("Result:",obj.mul())

    elif choice==4:
        print("Result:",obj.div())

    elif choice==0:
        print("Exit")

    else:
        print("Inavlid choice")
print()    