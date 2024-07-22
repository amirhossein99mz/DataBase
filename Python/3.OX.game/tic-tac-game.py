import random as r

def play_OX():
    
    matrix = []

    for i in range(3):
        new = []
        for j in range(3):
            new.append("-")
        matrix.append(new)

    for i in range(len(matrix)):
        print(" ".join(str(x) for x in matrix[i]))
    
    count = 0
    winner = None
    count = 0
    while winner == None:
        
        row1 = int(input("Enter a number as row (1,2,3):"))
        col1 = int(input("Enter a number as column (1,2,3):"))
        
        count += 1
        
        row1 -= 1
        col1 -= 1

        row2 = r.randint(0,2)
        col2 = r.randint(0,2)
        
        
        if row1 > 2 or row1 < 0:
            pass
        else:
            if col1 > 2 or col1 < 0:
                pass
            else:
                if matrix[row1][col1] != "-":
                    pass
                else:
                    matrix[row1][col1] = "O"
                     
        if matrix[row2][col2] != "-":
            pass
        else:
            matrix[row2][col2] = "X" 

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j],end=" ")
            print()
        
        

        for i in range(len(matrix)):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] == "O":
                winner = "USER"
            elif matrix[i][0] == matrix[i][1] == matrix[i][2] == "X":
                winner = "PC"
            else:
                for j in range(len(matrix[i])):
                    if matrix[0][j] == matrix[1][j] == matrix[2][j] == "O":
                        winner = "USER"
                    elif matrix[i][0] == matrix[i][1] == matrix[i][2] == "X":
                        winner = "PC"
                    else:
                        if matrix[1][1] == matrix[0][-1] == matrix[2][0] == "O":
                            winner = "USER"
                        elif matrix[1][1] == matrix[0][-1] == matrix[2][0] == "X":
                            winner = "PC"
                        else:
                            if matrix[1][1] == matrix[0][0] == matrix[2][2] == "O":
                                winner = "USER"
                            elif matrix[1][1] == matrix[0][0] == matrix[2][2] == "X":
                                winner = "PC"
    
    print(f"'{winner}' wins the match after {count} iteration")                        

play_OX()