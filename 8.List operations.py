my_list=["Panipuri","Pizza","Idli"]
choice=1
while choice!=0:
    print("1:Insert")
    print("2:Append")
    print("3:Pop")
    print("4:Search")
    choice = int(input("Enter the choice:"))
    if choice==1:
        print("Insert")
        my_list.insert(0,"Kachori")
        print(my_list)
    elif choice==2:
        print("Append")
        my_list.append("Dosa")
        print(my_list)
    elif choice==3:
        print("Pop")
        new_list=my_list.pop()
        print(my_list)
    elif choice==4:
        print("Search")
        new_list=my_list.index("Pizza")
        print(new_list)
    else:
        print("Invalid choice")
