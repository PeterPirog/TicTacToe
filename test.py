import numpy as np
def reverse_board(board):
    board=-1*board
    return board

if __name__ == '__main__':

    games = 1
    turns = 3

    player1_reward=None
    player2_reward = None

    #players moves for the episode
    player1_moves=[0,2,1]
    player2_moves=[4,7,8]  #8 is neccesssary id doen conditionno exist



    for game in range(games):
        #create empty board
        board= np.zeros(9, dtype=int)
        #declary empty state lists
        states = []  # states player 1 view
        states_inv = []  # inverted states for player 2 view

        states.append(board.copy())
        states_inv.append(reverse_board(board.copy()))
        print('states=',states)
        print('states_inv=', states_inv)
        for turn in range(turns):
            print(f'Turn:{turn}')
            #Player 1 side
            action=player1_moves[turn] #agent action
            board[action]=1
            states.append(board.copy())
            #tutaj sprawdz czy koniec
            board=reverse_board(board)
            states_inv.append(board.copy())
            action = player2_moves[turn]  # agent action
            board[action] = 1
            states_inv.append(board.copy())
            # tutaj sprawdz czy koniec
            board = reverse_board(board)
            states.append(board.copy())

            print('states=',states)
            print('states_inv=', states_inv)