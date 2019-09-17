class Board:
    board = [[7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]]
    
    def print_Board(self):
        
        for row in range(len(self.board)):
            
                
            if row % 3==0 and row != 0 and row != len(self.board):
                print("- - - - - - - - - - -")
            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    print("| ", end="")
                
                if col== 8:
                    print(self.board[row][col])

                else: 
                    print(str(self.board[row][col]) + " ", end="")
                
    def find_Empty(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)  # row, col

        return False
    
    def insert(self, num, pos):
        self.board[pos[0]][pos[1]] = num
    


    
class Solver():

    
    def __init__( self, board):
        self.board = board

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



    


       
    
board = Board()

print("Sudoku")
board.print_Board()
print( " ")

solver = Solver(board).solve()

print("Solution")
board.print_Board()


 