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
                
            


       
    
Board().print_Board() 
 