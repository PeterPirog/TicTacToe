import numpy as np

import gym

"""
# Press the green button in the gutter to run the script.

class TicTacToe(gym.Env):
    def __init__(self):
        self.board = np.zeros(9, dtype=int)  # size of board =9
        self.active_player = 1

        self.done = False

    def reset(self):
        self.board = np.zeros(9, dtype=int)
        #self.winner_player = 0  #there is no winner
        #self.end_by_wrong_move=False
        #self.player_symbol = 1

        # information about state
        #self.obs = self.board
        #self.action = None
        #self.reward = None
        #self.done = False
        #self.info = 'Not implemented'
        return self.board

    def step(self, action):
        self.board[action]=1
        return self.board


    def render(self):
        print('----------------------------------------')
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print('----------------------------------------')



    def __get_winner__(self):
        #horrizontal check is player 1 wins
        if self.board[0]+self.board[1]+self.board[2]==3: return 1
        if self.board[3]+self.board[4]+self.board[5]==3: return 1
        if self.board[6]+self.board[7]+self.board[8]==3: return 1

        #horrizontal check is player 2 wins
        if self.board[0]+self.board[1]+self.board[2]==-3: return 2
        if self.board[3]+self.board[4]+self.board[5]==-3: return 2
        if self.board[6]+self.board[7]+self.board[8]==-3: return 2

        # vertical check is player 1 wins
        if self.board[0] + self.board[3] + self.board[6] == 3: return 1
        if self.board[1] + self.board[4] + self.board[7] == 3: return 1
        if self.board[2] + self.board[5] + self.board[8] == 3: return 1

        # vertical check is player 1 wins
        if self.board[0] + self.board[3] + self.board[6] == -3: return 2
        if self.board[1] + self.board[4] + self.board[7] == -3: return 2
        if self.board[2] + self.board[5] + self.board[8] == -3: return 2

        #diagonals check is player 2 wins
        if self.board[0] + self.board[4] + self.board[8] == 3: return 1
        if self.board[2] + self.board[4] + self.board[6] == 3: return 1

        #diagonals check is player 2 wins
        if self.board[0] + self.board[4] + self.board[8] == -3: return 2
        if self.board[2] + self.board[4] + self.board[6] == -3: return 2


        return 0 #return 0 if no winner

    def revert_state(self,state):
        #function for reverte states between players
        return -1*state
"""
def reverse_board(board):
    return -1*board

if __name__ == '__main__':

    games = 1
    turns = 1

    player1_reward=None
    player2_reward = None

    #players moves for the episode
    player1_moves=[0,2,1]
    player2_moves=[4,7]



    for game in range(games):
        #create empty board
        board= np.zeros(9, dtype=int)
        #declary empty state lists
        states = []  # states player 1 view
        states_inv = []  # inverted states for player 2 view

        states.append(board)
        states_inv.append(reverse_board(board))
        print('states=',states)
        print('states_inv=', states_inv)
        for turn in range(turns):
            print(f'Turn:{turn}')
            #Player 1 side
            action=player1_moves[turn] #agent action
            board[action]=1
            states.append(board)
            print('states=',states)
            print('states_inv=', states_inv)

"""
            
            obs_, reward, done, info=env.step(action, player=1)
            print(f'game={game}, turn={turn},reward={reward},player:{env.active_player},{info}')
            print([obs, action, reward, obs_, done]) #place for storage sars
            env.render()
            obs=obs_
            if env.done == True: break  # check if game is ended

            #   Player 2 move

            action = np.random.randint(9)
            env.step(action, player=2)
            print(f'game={game}, turn={turn},reward={env.reward},player:{env.active_player},{env.info}')
            env.render()
            if env.done == True: break  # check if game is ended
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
