terms=int(input("How many terms:"))
result=list(map(lambda x:2**x,range(terms)))
print("The total terms is:",terms)
for i in range(terms):
    print("2 raised to power",i,"is",result[i])
my_list=[1,2,3,4,5]
new_list=list(map(lambda x:x**x ,my_list))
print(new_list)
