'''
Lesson 1 ex 7: Tic-tac-toe
'''

class TicTacToe:

    def __init__(self):
        """ play a game of tic-tac-toe """
        self.play = {}
        self.board = """
             {s1:^3} | {s2:^3} | {s3:^3} 
            -----+-----+-----
             {s4:^3} | {s5:^3} | {s6:^3} 
            -----+-----+-----
             {s7:^3} | {s8:^3} | {s9:^3} 
        """

    def initialize_board(self):
        for n in range(9):
            self.play["s{}".format(n+1)] = ""

    def show_board(self):
        """ display the playing board.  We take a dictionary with the current state of the board
        We rely on the board string to be a global variable"""
        print(self.board.format(**self.play))

    def get_move(self, n, xo):
        """ ask the current player, n, to make a move -- make sure the square was not 
        already played.  xo is a string of the character (x or o) we will place in
        the desired square """
        valid_move = False
        while not valid_move:
            idx = input("player {}, enter your move (1-9)".format(n))
            if self.play["s{}".format(idx)] == "":
                valid_move = True
            else:
                print("invalid: {}".format(self.play["s{}".format(idx)]))
                
        self.play["s{}".format(idx)] = xo
     
    def winner(self): 
        all_combinations=[["s1", "s2", "s3"], ["s4", "s5", "s6"], ["s7", "s8", "s9"], 
                          ["s1", "s4", "s7"], ["s2", "s5", "s8"], ["s3", "s6", "s9"],
                          ["s1", "s5", "s9"], ["s3", "s5", "s7"]]
        for combination in all_combinations: 
            if self.play[combination[0]] != '' and self.play[combination[1]] != '' and self.play[combination[2]] != '':
                if self.play[combination[0]] == self.play[combination[1]] == self.play[combination[2]]:
                    return True
    
    def play_game(self):
        """ play a game of tic-tac-toe """
        
        self.initialize_board()
        self.show_board()
        n_turns = 0 
        player = 1
        symbol = "x"
        while n_turns < 9:
            self.get_move(player, symbol)
            self.show_board()
            winner_player = self.winner()
            if winner_player == True: 
                print(f"The winner is player {player}. \nThis match is finished.")
                break

            if player == 1 : 
                player = 2
                symbol = 'o'
            else:
                player = 1
                symbol = 'x'

            n_turns += 1 
    
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()