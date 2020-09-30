class Board():
    ''' A simple Tic Tac Toe Board

        1  2  3
    -------------   
    1 |  |  |  |  
     ------------  
    2 |  |  |  |  
     ------------  
    3 |  |  |  |  
    '''

    def __init__(self):
        self.grid11 = ''
        self.grid12 = ''
        self.grid13 = ''
        self.grid21 = ''
        self.grid22 = ''
        self.grid23 = ''
        self.grid31 = ''
        self.grid32 = ''
        self.grid33 = ''

    def is_valid_play(self, posX, posY):
        if getattr(self, f'grid{posX}{posY}'):
            return False
        return True

    def place_marker(self, posX, posY, marker):
        if not getattr(self, f'grid{posX}{posY}'):
            setattr(self, f'grid{posX}{posY}', marker)
        else:
            pass #Display an error message

    def check_win_conditions(self):
        #rows
        for i in range(1,4):
            if (getattr(self, f'grid{i}{1}') 
                == getattr(self, f'grid{i}{2}')
                == getattr(self, f'grid{i}{3}')
                != ''):
                return True
            
        #cols
        for i in range(1,4):
            if (getattr(self, f'grid{1}{i}') 
                == getattr(self, f'grid{2}{i}')
                == getattr(self, f'grid{3}{i}')
                != ''):
                return True
        #diags
        if (getattr(self, f'grid{1}{1}') 
                == getattr(self, f'grid{2}{2}')
                == getattr(self, f'grid{3}{3}')
                != ''):
                return True
        elif (getattr(self, f'grid{1}{3}') 
                == getattr(self, f'grid{2}{2}')
                == getattr(self, f'grid{3}{1}')
                != ''):
                return True
        return False
  
    def __str__(self):
        return f'''
            1   2   3
        ---------------  
        1 | {self.grid11 or ' '} | {self.grid12 or ' '} | {self.grid13 or ' '} |
        ---------------  
        2 | {self.grid21 or ' '} | {self.grid22 or ' '} | {self.grid23 or ' '} |
        ---------------  
        3 | {self.grid31 or ' '} | {self.grid32 or ' '} | {self.grid33 or ' '} |
    '''

class TicTacToe():
    def __init__(self):
        self.turn = 0
        self.board = Board()
        self.game_over = False
        self.markers = {
            1:'X',
            2:'O',
        }
        while not self.game_over:
            self.take_turn()

    def prompt_for_input(self):
        print(self.board)
        tup = input(f''' \tIt\'s Player {self.whos_turn()}\'s turn 
        Input your play as <row><col> (for example \'13\' plays on row 1, column 3 \n\t''')
        x,y = int(tup[0]), int(tup[1])
        return x,y
    def whos_turn(self):
        if self.turn %2==0:
            return 1
        return 2
    def reset(self):
        self.turn = 0
        self.board = Board()
        self.game_over = False
    
    def take_turn(self):
        while True:
            posX, posY = self.prompt_for_input()
            if self.board.is_valid_play(posX, posY):
                break
            else:
                print('That is not a valid move, try again')
        self.board.place_marker(posX, posY, self.markers[self.whos_turn()])
        self.game_over = self.board.check_win_conditions()

        if self.game_over:
            print(self.board)
            print(f'\tPlayer {self.whos_turn()} Wins!')
            again = input('\tPlay again??? Y/N\t')
            if again == 'Y' or again == 'y':
                self.reset()
                return
        self.turn +=1


g = TicTacToe()





