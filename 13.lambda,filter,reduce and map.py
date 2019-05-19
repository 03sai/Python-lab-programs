from functools import reduce
print("Lambda function")
x=int(input("Enter the number:"))
g=lambda x:x**2
print(g(x))

print("Filter function")
my_list=[1,5,4,6,8,11,3,12]
new_list=list(filter(lambda x:(x%2==0),my_list))
print(new_list)

print("Map function")
my_list=[1,5,4,6,8,11,3,12]
new_list=list(map(lambda x:x*2,my_list))
print(new_list)

print("Reduce function")
my_list=[1,2,3,4,5,6,7,8,9,10]
new_list=reduce(lambda x,y:x+y,my_list)
print(new_list)
