import gym
import numpy as np

class TicTacToe(gym.Env):
    def __init__(self):
        #Define rewards per game
        self.reward_for_winning=1
        self.reward_for_loosing=-1
        self.reward_for_draw=-0.5
        self.reward_intermediate=0 #reward when no winer and game is in progress

        self.reset()


    def reset(self):
        self.active_player=1
        self.done=False
        self.turn=-1 #using -1 not 0 to use +1 ietartor after each turn
        self.move_possible=True # change status to True if current move is not possible for some reason

        #boards
        self.board= np.zeros(9, dtype=int)
        self.board_inverted = np.zeros(9, dtype=int)

        #states lists
        self.states_list = []
        self.states_inverted_list = []

        #actions lists
        self.actions_list = []
        self.actions_inverted_list = []


    def step_player1(self,action):

        self.turn+=1 #iterate rurn when player 1 moves

        self.active_player = 1

        self.actions_list.append(action)
        self.board[action] = 1
        #check if player 1 wins if true add board to states list and board inverted to states_inverted list
        #check if player 1 moves is the last and no winner
        #check if no winner, next move available


        self.board_inverted=-1*self.board

        self.states_list.append(self.board.copy())
        self.states_inverted_list .append(self.board_inverted.copy())







    def step_player2(self,action):
        self.active_player = 2

        self.actions_inverted_list.append(action)
        self.board_inverted[action] = 1

        self.board=-1*self.board_inverted
        self.states_list.append(self.board.copy())
        self.states_inverted_list .append(self.board_inverted.copy())



    def show_info(self):
        print('\n----------------------------------------------------------------------------')
        print(f'Turn:{self.turn}, Player: {self.active_player}')
        self.render_board(player=1)
        print(f'States player 1 list={self.states_list}')
        print(f'Actions player 1 list={self.actions_list}')
        print(f'States player 2 list ={self.states_inverted_list}')
        print(f'Actions player 2 list={self.actions_inverted_list}')

    def render_board(self,player=1):
        if player==1:
            board=self.board
        else:
            board=self.board_inverted

        print('----------------------------------------')
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print('----------------------------------------')

    def check_terminating_condition(self):
        pass
        #Check if there are empty fields

        #Check if there is the winner



if __name__ == '__main__':
    games = 1

    #no winner
    player1_moves=[4,2,3,1,8]
    player2_moves=[0,6,5,7]  #8 is neccesssary id doen conditionno exist

    env=TicTacToe()

    for i in range(games):
        env.reset()

        while not env.done:

            #Player 1 side
            try:
                action=player1_moves[env.turn] #agent action
                print('env.turn=',env.turn,'Action=',action)
            except:
                print('Out of range player 1 move')
                break
            env.step_player1(action)
            env.show_info()

            #Player 2 side
            try:
                action=player2_moves[env.turn] #agent action
            except:
                print('Out of range player 2 move')
                break
            env.step_player2(action)
            env.show_info()



