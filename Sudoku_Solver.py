from tkinter import *
from collections import defaultdict
    

board = Tk()
board.geometry('270x275')

# Solve the Sudoku
class SolveSudoku():
    def __init__(self):
        board=[['.' for _ in range(9)] for _ in range(9)]
        self.setBoard(board)
        self.solveSudoku(board)

    #set the board

    def setBoard(self,board):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() in ['1','2','3','4','5','6','7','8','9']:
                    board[i][j]=savedNumbers[i][j].get()

    # check if sudoku is valid

    def isValidSudoku(self, board):        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                if (board[i][j] in rows[i] 
                or board[i][j] in cols[j] 
                or board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[(i // 3, j // 3)].add(board[i][j])

        return True

    def solveSudoku(self, board):
        def solve(row, col):
            if row == 9:
                return True
            if col == 9:
                return solve(row+1, 0)
            
            if board[row][col] == ".":
                for i in range(1, 10):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)
                        
                        if solve(row, col + 1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)



        def isValid(row, col, ch):
            row, col = int(row), int(col)
            for i in range(9):
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False
                if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                    return False
            return True
        
        #if valid then solve using backtracking else clear screen
        if self.isValidSudoku(board):
            solve(0,0)
            self.setUI(board)
        else:
            Launch.clearAll(self)
        
    # set the UI to display solution
    def setUI(self,board):
        for i in range(9):
            for j in range(9):
                savedNumbers[i][j].set(board[i][j])
        
            
            
        
    

class Launch():
    
    # Set Title, Grid and Menu
    def __init__(self, master):
        
        # Title and settings
        self.master = master
        master.title("Sudoku Solver")

        font = ('Arial', 18)
        color = 'white'

        self.table = [[0 for _ in range(9)] for _ in range(9)]

        for i in range(0,9):
            for j in range(0,9):
                
                if (i < 3 or i > 5) and (j < 3 or j > 5):
                    color = 'orange'
                elif i in [3,4,5] and j in [3,4,5]:
                    color = 'orange'
                else:
                    color = 'white'

                self.table[i][j] = Entry(master, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 0,
                                          highlightcolor = 'yellow', highlightthickness = 1, highlightbackground = 'black',
                                          textvar = savedNumbers[i][j])
                self.table[i][j].bind('<Motion>', self.correctGrid)
                self.table[i][j].bind('<FocusIn>', self.correctGrid)
                self.table[i][j].bind('<Button-1>', self.correctGrid)
                self.table[i][j].grid(row=i, column=j)


        # Front-End Menu
        menu = Menu(master)
        master.config(menu = menu)

        file = Menu(menu)
        menu.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit', command = master.quit)
        file.add_command(label = 'Solve', command = self.solveInput)
        file.add_command(label = 'Clear', command = self.clearAll)


    # Correct the Grid if inputs are uncorrect
    def correctGrid(self, event):
        for i in range(9):
            for j in range(9):
                if savedNumbers[i][j].get() == '':
                    continue
                if len(savedNumbers[i][j].get()) > 1 or savedNumbers[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    savedNumbers[i][j].set('')


    # Clear the Grid
    def clearAll(self):
        for i in range(9):
            for j in range(9):
                savedNumbers[i][j].set('')


    # Calls the class SolveSudoku
    def solveInput(self):
        solution = SolveSudoku()

        
        


# Global Matrix where are stored the numbers
savedNumbers =[[0 for _ in range(9)] for _ in range(9)]
for i in range(0,9):
    for j in range(0,9):
        savedNumbers[i][j] = StringVar(board)


app = Launch(board)
board.mainloop()


