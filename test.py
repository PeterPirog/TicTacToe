import numpy as np
def reverse_board(board):
    board=-1*board
    return board

def check_if_end(board):
    #Function checks if current plyer won
    # horrizontal check if current player wins
    if board[0] + board[1] + board[2] == 3: return 1
    if board[3] + board[4] + board[5] == 3: return 1
    if board[6] + board[7] + board[8] == 3: return 1

    # vertical check if current player wins
    if board[0] + board[3] + board[6] == 3: return 1
    if board[1] + board[4] + board[7] == 3: return 1
    if board[2] + board[5] + board[8] == 3: return 1


    # diagonals check if current player wins
    if board[0] + board[4] + board[8] == 3: return 1
    if board[2] + board[4] + board[6] == 3: return 1

    if 0 not in board: #no empty places but no winner
        return 2
    else:
        return 0  # there are empty places, no winner
    
def render_board(board):
    print('----------------------------------------')
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print('----------------------------------------')

if __name__ == '__main__':

    games = 1
    turns = 5

    player1_reward=None
    player2_reward = None

    #players moves for the episode
    #player 1 win
    #player1_moves=[0,2,1]
    #player2_moves=[4,7,8]  #8 is neccesssary id doen conditionno exist

    #no winner
    player1_moves=[4,2,3,1,8]
    player2_moves=[0,6,5,7]  #8 is neccesssary id doen conditionno exist



    for game in range(games):
        #create empty board
        board= np.zeros(9, dtype=int)
        #declary empty state lists
        states = []  # states player 1 view
        states_inv = []  # inverted states for player 2 view

        states.append(board.copy())
        states_inv.append(reverse_board(board.copy()))
        #print('states=',states)
        #print('states_inv=', states_inv)
        winner_player=0

        for turn in range(turns):
            print('----------------------------------------')
            print('----------------------------------------')
            print(f'Turn:{turn}')
            #Player 1 side
            action=player1_moves[turn] #agent action
            board[action]=1
            print(f'Player 1 move:{action}')
            states.append(board.copy())
            #tutaj sprawdz czy koniec
            is_winner=check_if_end(board)
            if is_winner==1:
                winner_player=1
            print('is_winner=',is_winner,'winner player=',winner_player)
            render_board(board)

            board=reverse_board(board)
            states_inv.append(board.copy())

            print('states=',states)
            print('states_inv=', states_inv)

            if winner_player !=0:
                turn=9
                break


            action = player2_moves[turn]  # agent action
            print(f'Player 2 move:{action}')
            board[action] = 1
            states_inv.append(board.copy())
            # tutaj sprawdz czy koniec
            is_winner=check_if_end(board)
            if is_winner==1:
                winner_player=2
            print('is_winner=',is_winner,'winner player=',winner_player)
            render_board(board)

            board = reverse_board(board)
            states.append(board.copy())

            print('states=',states)
            print('states_inv=', states_inv)

            if winner_player !=0:
                turn = 9
                break