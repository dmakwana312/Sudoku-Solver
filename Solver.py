class Board:
    board = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    
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
                    return (row, col) 

        return False
    
    def insert(self, num, pos):
        self.board[pos[0][1]] = num
    


    
class Solver():

    
    def __init__( self, board):
        self.board = board

    def solve(self):
        
        if not self.board.findEmpty():
            return True
        else:
            row, col = self.board.findEmpty()
        for val in range(0, 10):
            if valid(val, (row, col)):
                self.board.insert(val, (row, col))

                if solve():
                    return True
                
                self.board.insert(0, (row, col))

        return False

                

    def valid(self, num, pos):

        for row in range(len(self.board[0])):
            if self.board[pos[0][row]] == num and pos[1] != row:
                return False

        for col in range(len(self.board)):
            if self.board[col][pos[1]] == num and pos[0] != col:
                return False       

        box_X = pos[1] // 3
        box_Y = pos[0] // 3

        for row in range(box_Y * 3, box_Y * 3 + 3):
            for col in range(box_X * 3, box_X * 3 + 3):
                if self.board[row][col] == num and (row, col) != pos:
                    return False

        return True



    


       
    
Board().print_Board() 
 