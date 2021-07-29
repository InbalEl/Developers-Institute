import random

class RockPaperScissors:
    def __init__(self) -> None:
        self.possible_items = ['rock', 'paper', 'scissors']

    def __get_user_item(self) -> int:


        self.__print_possible_items()
        user_pick = input('\tMake your pick: ')

        while not (user_pick.isdigit() and 1 <= int(user_pick) <= 3):

            self.__print_possible_items()
            user_pick = input('\tSorry, invalid pick. Try again: ')

        return int(user_pick)

    def __print_possible_items(self):
        for index, item in enumerate(self.possible_items):
            print(f'\t[{index+1}]: {item}')

    def __get_computer_item(self) -> int:
        
        # Was asked to use random.choice(), which returns the actual elem and not an index
        return random.randint(0,2)
    
    '''
    Returns 1 if user won, 0 for draw, -1 if computer won
    '''
    def __get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 0
        elif (user_item - computer_item == 1) or (user_item == 0 and computer_item == 2):
            return 1
        return -1


    def play(self):
        user_pick = self.__get_user_item()
        computer_pick = self.__get_computer_item()
        game_res = self.__get_game_result(user_pick-1, computer_pick)

        print(f'You chose {self.possible_items[user_pick-1]}, and the computer {self.possible_items[computer_pick]}.')
        if game_res == 0:
            print('It\'s a draw!')
        elif game_res == 1:
            print('You\'ve won!')
        else:
            print('The computer has won!')
        
        return game_res