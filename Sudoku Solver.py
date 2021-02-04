import numpy as np

# Checking if a number can be placed in perticular position  
def If_Possible(y,x,n):
    global sudoku
    for i in range(0,9):
        if sudoku[y][i]==n:
            return False
    for i in range(0,9):
        if sudoku[i][x]==n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+i][x0+j] == n:
                return False
    return True

# The recusive function which also uses back_tracking 
def solver():
    global sudoku
    for y in range(9):
        for x in range(9):
            #Finding the empty positions and checking what number can be placed
            if sudoku[y][x] == 0:  
                for n in range(1,10):
                    if If_Possible(y,x,n):
                        sudoku[y][x] = n  # filling it up if the solution is possible
                        solver()          # calling it again coz problem is reduced further
                        sudoku[y][x] = 0  # changing it to '0' again if choices are bad
                
                return # returning 
            
    print(np.matrix(sudoku))  # displaying the solved sudoku
    print("\n=========================================\n") 
    input("Do you want more Solution? (if there any!)")  # asking to user if he wants more possible solution 
    print("\n=========================================\n") 
       
if __name__ == '__main__':

    sudoku = []
    for _ in range (9):
        sudoku.append([int(i) for i in input().split()])

    print("\n=========================================\n")
    print("Unsolved Soduku")
    print("\n=========================================\n")

    print(np.matrix(sudoku))
    
    print("\n=========================================\n")   
    solver()