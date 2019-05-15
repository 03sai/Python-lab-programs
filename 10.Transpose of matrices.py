m=int(input("Enter matrix row size:"))
n=int(input("Enter matrix column size:"))
A=[[0]*n for i in range(m)]

result=[[0]*m for j in range(n)]

print("Enter the value for A matrix")
for i in range(m):
    for j in range(n):
        A[i][j]=int(input())
print("Print A matrix")
for a in A:
    print(a)
    
for i in range(len(A)):
    for j in range(len(A[0])):
                   result[j][i]=A[i][j]

print("Transpose of matrices is:")
for r in result:
    print(r)
