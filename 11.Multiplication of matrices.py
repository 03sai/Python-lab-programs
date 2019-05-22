print("Matrix A row size and column size")
m=int(input("Enter matrix row size:"))
n=int(input("Enter matrix column size:"))
print("Matrix B row size and column size")
p=int(input("Enter matrix row size:"))
q=int(input("Enter matrix column size:"))

A=[[0]*n for i in range(m)]
B=[[0]*q for i in range(p)]
result=[[0]*m for k in range(q)]

print("Enter the value for A matrix")
for i in range(m):
    for j in range(n):
        A[i][j]=int(input())
print("Print A matrix")
for a in A:
    print(a)
    
print("Enter the value for B matrix")
for i in range(p):
    for j in range(q):
        B[i][j]=int(input())
print("Print B matrix")
for b in B:
    print(b)

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j]+=A[i][k]*B[k][j]

print("Multiplication of matrices is:")
for r in result:
    print(r)
