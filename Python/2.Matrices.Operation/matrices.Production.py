def read_file(filename):
    try:
        with open(filename) as file1:
            file2 = file1.read().split("\n")
        mat = []
        for i in range(len(file2)):
            file2[i] = [int(number) for number in file2[i].split()]
            row = file2[i][0]
            col = file2[i][1]
            col1 = 0
            col2 = col
            new = [[row,col]]
            new2 = file2[i][2:]
            new3 = []

            while len(new2) > col1:
                new3.append(new2[col1:col2])
                col1 += col
                col2 += col
            
            new.append(new3)
            mat.append(new)
        
        return mat

    except OSError as err:
        print(err)
    

def prodcution(mat1,mat2):


    mat = []
    for i in range(len(mat1)): 
        new = []
        for k in range(len(mat2[0])): 
            element = 0
            for j in range(len(mat1[0])) : 
                element += (mat1[i][j]*mat2[j][k])
            new.append(element)
        mat.append(new)
    
    return mat

def process(mat):

    print("The begining matrix is:")
    for i in range(len(mat)):
        row = mat[i][0][0]
        col = mat[i][0][1]
        print(f"matrix {row} x {col}:")
        for j in range(len(mat[i][1])):
            for t in range(len(mat[i][1][j])):
                print(mat[i][1][j][t],end=" ")
            print()
        print()
    print()
    
    mat2 = []
    for i in range(len(mat)):
        if i < len(mat)-1:
            if i % 2 == 0:
                if mat[i][0][1] == mat[i+1][0][0]:
                    mat2.append([[mat[i][0][0],mat[i+1][0][1]]])
    

    for j in range(len(mat2)):
        for i in range(len(mat)):
            if i < len(mat)-1 and i % 2 == 0:
                if mat[i][0][0] == mat2[j][0][0] and mat[i+1][0][1] == mat2[j][0][1]:
                    matrix1 = mat[i][1]
                    matrix2 = mat[i+1][1]
                    final = prodcution(matrix1,matrix2)
        mat2[j].append(final)

    print()
  
    row1 = mat2[0][0][0]
    col1 = mat2[1][0][1]
    
    matrix11 = mat2[0][1]
    matrix22 = mat2[1][1]
    
    final = prodcution(matrix11,matrix22)
    print(f"The final matrix {row1} x {col1} is:")
    for i in range(len(final)):
        print(" ".join(str(y) for y in final[i]))

def main():
    mat = read_file("matrices.Multiplication.txt")
    process(mat)
main()