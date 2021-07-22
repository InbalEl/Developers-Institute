import tictactoe_mod as tictactoe


user_input = input('Do you want to play? (enter y or n):\n')

while (user_input == 'y'):
    tictactoe.play_round()
    user_input = input('Do you want to play? (enter y or n):\n')