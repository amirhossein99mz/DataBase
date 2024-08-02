def read_file(filename):
    try:
        with open(filename) as file:
            matrix = [list(map(int,line.split()))for line in file]
        
        return matrix
    
    except FileNotFoundError as err:
        print(err)

def sort_list1(matrix):

    print("Beginning matrix:")
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            print(matrix[m][n],end=" ")
        print()
    print()
    
    #sort each list of matrix(ascending order)

    for t in range(1000):  # to access all elements of a matrix, first 'for loop' shoud be assigned to a range of very large number
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j > 0:
                    if matrix[i][j-1] <= matrix[i][j]:
                        pass
                    else:
                        matrix[i][j-1],matrix[i][j] = matrix[i][j],matrix[i][j-1]
                elif j < len(matrix[i])-1:
                    if matrix[i][j] <= matrix[i][j+1]:
                        pass
                    else:
                        matrix[i][j],matrix[i][j+1]=matrix[i][j+1],matrix[i][j]

    # print the sorted lists 
    print("Sorted version:")       
    for k in range(len(matrix)):
        print(" ".join(str(x) for x in matrix[k]))
    #look at ech row from left ot right 
 


def main():
    
    matrix = read_file("listOfNumbers.txt")
    sort_list1(matrix)

if __name__ == "__main__":
    main()

# Note : 1.try to implement less for or while loops and also more def to have more efficient program
