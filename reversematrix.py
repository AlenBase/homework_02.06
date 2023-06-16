N=4

mat=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

def rotateMatrix(mat):
    i = N-1
    while(i>=0):
        j = N-1
        while(j>=0):
            print(mat[i][j], end=" ")
            j = j-1
        i=i-1
        print()    
            
rotateMatrix(mat)