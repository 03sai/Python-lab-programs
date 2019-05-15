n=input("Enter String:")
length=int(len(n))
for i in range(0,int(length/2+1)):
    if n[i]==n[-i-1]:
        continue
    else:
        break
if i<int(length/2):
    print("Not a palindrome")
else:
    print("The given string is palindrome")
