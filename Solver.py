class Board:

    # Board array is initialised
    board = [[0 for col in range(0,9)] for row in range(0,9)]
    
    # Function to print board
    def print_Board(self):

        for row in range(len(self.board)):
            if row % 3==0 and row != 0 and row != len(self.board):
                print("- - - - - - - - - - -")
            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    print("| ", end="")
                if col== 8:
                    if self.board[row][col] != 0:
                        print(self.board[row][col])
                    else:
                        print(" ")
                else: 
                    if self.board[row][col] != 0:
                        print(str(self.board[row][col]) + " ", end="")
                    else:
                        print(" " + " ", end="")

    # Function to find empty places on the board            
    def find_Empty(self):

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)  # row, col

        return False

    # Function used to input board
    def board_Input(self):

        row = 0

        while row < 9:
            current_Row = row
            row_Input = input("\nEnter row " + str(row+1) + ":")
            if self.row_Input_Validation(row_Input):
                str_row_Input = str(row_Input)
                for col in range(len(str_row_Input)):
                    self.insert(int(str_row_Input[col]), (row, col))
                row += 1
            else:
                print("\nENTER ROW AGAIN")
                row = current_Row

    # Validating row that is inputted by user            
    def row_Input_Validation(self, input):

        try:
            if len(input) == 9:
                return True
            else:
                print("\nERROR: MAKE SURE ROW ENTRY HAS 9 DIGITS (REPLACE BLANK SPACES WITH 0)")
                return False

        except ValueError:
            print("\nERROR: MAKE SURE ROW ENTRY ONLY CONTAINS NUMBERS")
            return False
    
    # Function to insert single digit into a specific place on the board
    def insert(self, num, pos):
        self.board[pos[0]][pos[1]] = num
        
class Solver():

    def __init__(self, board):
        self.board = board

    # Backtracking algorithm implemented through this function
    def solve(self):

        if not self.board.find_Empty():
            return True
        else:
            row, col = self.board.find_Empty()

        for val in range(1, 10):
            if self.valid(val, (row, col)):
                self.board.insert(val, (row, col))
                if self.solve():
                    return True
                self.board.insert(0, (row, col))

        return False

    # Function to check if inserted digit is valid
    def valid(self, num, pos):

        for row in range(len(self.board.board[0])):
            if self.board.board[pos[0]][row] == num:
                if pos[1] != row:
                    return False

        for col in range(len(self.board.board)):
            if self.board.board[col][pos[1]] == num and pos[0] != col:
                return False       

        box_X = pos[1] // 3
        box_Y = pos[0] // 3

        for row in range(box_Y * 3, box_Y * 3 + 3):
            for col in range(box_X * 3, box_X * 3 + 3):
                if self.board.board[row][col] == num and (row, col) != pos:
                    return False

        return True

    # Function to ensure the entire board that is inputted is valid
    def board_Input_Validation(self):

        for row in range(9):
            for col in range(9):
                if self.board.board[row][col] != 0:
                    if not solver.valid(self.board.board[row][col], (row, col)):
                        print("\nBoard That Was Entered Is Not Valid")
                        return False
 
        return True

board = Board()
solver = Solver(board)

# Loop to keep the program running
while True:

    menu_Option = input("\n1. Enter Sudoku Board\n2. Exit\nEnter 1 or 2: ")

    if menu_Option == "1":
        print("\nEnter each row without spaces when prompted \nFor Example: \n1   3 |   5 6 | 7   8 would be entered as 103056708 with the empty spaces represented as 0\n")
        board.board_Input()

        print("\nYour Input\n")
        board.print_Board()

        if solver.board_Input_Validation():
            print("\nSolution\n")
            solver.solve()
            board.print_Board()
        
    elif menu_Option == "2":
        print("\nThank you for using this solver")
        quit()
    else:
        print("\nEnter Valid Menu Option")
