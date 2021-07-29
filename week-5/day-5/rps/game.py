from rock_paper_scissors import RockPaperScissors

def isValidMenuChoice(user_menu_choice: str) -> bool:
    return user_menu_choice.isdigit() and 1 <= int(user_menu_choice)<= 3

def get_user_menu_choice() -> int:
    prompt_str = '''
Main Menu
[1]: Play a new game
[2]: Show scores
[3]: Quit
: '''

    user_menu_choice = input(prompt_str)
    
    while (not isValidMenuChoice(user_menu_choice)):
        print('Invalid input, please try again')
        user_menu_choice = input(prompt_str)

    return int(user_menu_choice)

def print_results(results: dict) -> None:
    
    print('Game score:')

    for key, val in results.items():
        print(f'{key}: {val}')

    print('Thanks for playing!')

def main():

    user_choice = get_user_menu_choice()

    game_results = {
        'wins': 0,
        'draws': 0,
        'losses': 0
    }

    while user_choice != 3:
        new_rps_game = RockPaperScissors()
        
        if user_choice == 1:

            round_res = new_rps_game.play()

            if round_res == 1:
                game_results['wins'] += 1
            elif round_res == 0:
                game_results['draws'] += 1
            else:
                game_results['losses'] += 1
            
        else:
            print_results(game_results)

        user_choice = get_user_menu_choice()
    
    print_results(game_results)


if __name__ == "__main__":
    main()