import numpy as np

import gym


# Press the green button in the gutter to run the script.

class TicTacToe(gym.Env):
    def __init__(self):
        self.board = np.zeros(9, dtype=int)  # size of board =9
        self.active_player = 1

        self.done = False

    def reset(self):
        self.board = np.zeros(9, dtype=int)
        self.winner_player = 0  #there is no winner
        self.end_by_wrong_move=False
        self.player_symbol = 1

        # information about state
        self.obs = self.board
        self.action = None
        self.reward = None
        self.done = False
        self.info = 'Not implemented'
        return self.obs

    def step(self, action, player):
        self.active_player = player
        self.reward=None

        if self.active_player == 1:
            self.player_symbol = 1
        else:
            self.player_symbol = -1

        # end game by forbiden player move (field isn't empty)
        if not self.board[action]==0:
            self.end_by_wrong_move=True
            self.done=True
            self.player_symbol*=2 #set

            #winning/losing by forbiden move
            if self.player_symbol<0:
                self.winner_player=1 #player 1 wins if player 2 makes forbiden move
                self.reward=0 #dont train model if model wins by oponent forbiden move
                self.info="Player 1 wins by oponet forbiden move"
            else:
                self.winner_player=2 #player 1 wins if player 2 makes forbiden move
                self.reward=-10 #penalty for player for forbiden move
                self.info = "Player 2 wins by oponet forbiden move"
        else:   #player move isn't forbiden

            self.winner_player=self.__get_winner__()
            if self.winner_player==0:
                self.info = "Game in progress.."
                self.reward = 0
            elif self.winner_player==1:
                self.info = "Player 1 wins"
                self.reward = 1
            elif self.winner_player==2:
                self.info = "Player 2 wins"
                self.reward = -1

        self.board[action] = self.player_symbol
        if not self.winner_player==0: self.done=True #finish game if thereis the winner
        return self.obs, self.reward, self.done, self.info

    def render(self):
        print('----------------------------------------')
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print('----------------------------------------')

    def __invert_state__(self):  # special function to invert state for player 2
        return self.board

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



if __name__ == '__main__':
    print('aa')
    games = 5
    turns = 9
    env = TicTacToe()

    for game in range(games):
        obs= env.reset()
        print('obs=',obs)
        for turn in range(turns):

            #   Player 1 move

            action = np.random.randint(3) #conunt action for obs
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
