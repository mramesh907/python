x=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
y=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(x)):
    for j in range(len(x[0])):
        y[j][i]=x[i][j]
print("The transpose of the matrix is:")
for i in y:
    print(i)