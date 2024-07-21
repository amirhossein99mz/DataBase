import random as r

def create_matrix():
    
    row = 3 # int(input("Enter a number as row:"))
    col = 3  # int(input("Enter a number as column:"))
    matrix = []
    for i in range(row):
        new = []
        for j in range(col):
            number = r.randint(0,9)
            new.append(number) 
        matrix.append(new)
    
    return matrix

def prin1_matrix(main_matrix):

    #print matrix
    print("Original matrix is:")
    #type 1
    for i in range(len(main_matrix)):
        for j in range(len(main_matrix[i])):
            print(main_matrix[i][j],end=" ")
        print()
    print()
    print()
    #type 2
    #  for i in range(len(matrix)):
    #     print(" ".join(str(x)for x in matrix[i]))
    
    
    #print each column
    row = len(main_matrix)
    col = len(main_matrix[0])
    columns = []
    for i in range(max(row,col)):
        column = [row[i] for row in main_matrix]
        columns.append(column)
    print("columns of matrix:")
    for t in range(len(columns)):
        print("column",t,":",columns[t])
    print()
    print()
    
    main_diag = [main_matrix[i][i] for i in range(min(row,col))]
    anti_diag = [main_matrix[i][-1-i] for i in range(min(row,col))]
    print("The main diagonal is ")
    for line in  main_diag:
        print(line)
    print()
    print("The anti diagonal is ")
    for line in  anti_diag:
        print(line)
    print()
    


def transpose(main_matrix):
    
    mat2 = []

    for i in range(len(main_matrix[0])):
        new = []
        for j in range(len(main_matrix)):
            new.append(0)
        mat2.append(new)
    
    for i in range(len(mat2)):
        for j in range(len(mat2[i])):
            mat2[i][j] = main_matrix[j][i]
    
    print("Transpose of matrix is:")
    for s in range(len(mat2)):
        print(" ".join(str(x)for x in mat2[s]))
    print()
    print()

def inverse(main_matrix):
    
    if len(main_matrix) != len(main_matrix[0]):
        print("The matrix is NOT square;thus there is NO inverse of matrix.")
    else:
        if len(main_matrix) == 2:
            det = (main_matrix[0][0]*main_matrix[1][1])-(main_matrix[0][1]*main_matrix[1][0])
            if det == 0:
                print("The matrix is NOT invertibe")
            else:
                print("Inverse of matrix is:")
                for i in range(len(main_matrix)):
                    for j in range(len(main_matrix[i])):
                        main_matrix[i][j] = (1/det)*main_matrix[i][j]
                        print(main_matrix[i][j],end=" ")
                    print()
                print()
    print()
    print("Please scroll up to see the all.")
    

def main():
    
    main_matrix = create_matrix()
    prin1_matrix(main_matrix)
    transpose(main_matrix)
    inverse(main_matrix)
if __name__ == "__main__":
    main()