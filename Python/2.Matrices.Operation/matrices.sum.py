def read_file(filename):
    try:
        with open(filename) as file1:
            file2 = file1.read().split("\n")
        mat = []
        for i in range(len(file2)):
            file2[i] = [int(j) for j in file2[i].split()]
            row = file2[i][0]
            col = file2[i][1]
            col1 = 0
            col2 = col
            new = [[row,col]]
            new2 = file2[i][2:]
            while len(new2) > col1:
                new.append(new2[col1:col2])
                col1 +=col
                col2 += col
            mat.append(new)  
        return mat
        
    except OSError as err:
        print(err)

def addition_matrices(matrix1,matrix2):

    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        final = []
        for i in range(len(matrix1)):
            new = []
            for j in range(len(matrix1[i])):
                new.append(matrix1[i][j]+matrix2[i][j])
            final.append(new)
        return final
        
def proces(mat):

    mat2 = []
    for i in range(len(mat)):
        size = mat[i][0]
        elements = mat[i][1:]
        mat2.append([size,elements])
    
    mat3 = []
    for line in mat2:
        if line[0] not in mat3:
            mat3.append(line[0])
    
    mat4 = [[line] for line in mat3]

    for i in range(len(mat2)):
        for j in range(len(mat4)):
            if mat2[i][0] == mat4[j][0]:
                mat4[j].append(mat2[i][1])

  
    
    for s in range(len(mat4)):
        matrix1 = mat4[s][1]
        matrix2 = mat4[s][2]
        final = addition_matrices(matrix1,matrix2)
        mat4[s].append(final)      
    
    return mat4
        
def print1_result(final):
    
    for i in range(len(final)):
        row = final[i][0][0]
        col = final[i][0][1]
        print(f"Sum of matrices {row} x {col}:")
        for j in range(len(final[i][-1])):
            print(" ".join(str(x) for x in final[i][-1][j]))
        print()
    print()

def main():
    
    mat = read_file("matrices.Addition.txt")
    final = proces(mat)
    print1_result(final)

if __name__ == "__main__":
    main()