m=int(input("Enter matrix row size:"))
n=int(input("Enter matrix column size:"))
A=[[0]*n for i in range(m)]
B=[[0]*n for i in range(m)]
result=[[0]*n for j in range(m)]

print("Enter the value for A matrix")
for i in range(m):
    for j in range(n):
        A[i][j]=int(input())
print("Print A matrix")
for a in A:
    print(a)
    
print("Enter the value for B matrix")
for i in range(m):
    for j in range(n):
        B[i][j]=int(input())
print("Print B matrix")
for b in B:
    print(b)

for i in range(len(A)):
    for j in range(len(A[0])):
                   result[i][j]=A[i][j]*B[i][j]

print("Sum of matrices is:")
for r in result:
    print(r)
