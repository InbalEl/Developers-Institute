def is_legal_move(player_move: str, state: list) -> bool:
    return (player_move.isnumeric() and
    1<= int(player_move) <= 9 and
    (state[int(player_move)-1]).isnumeric())

def check_if_won(player: str, player_move: int, state: list) -> bool:
    winning_paths = [
        [[3,6],[1,2],[4,8]], [[0,2],[4,7]], [[0,1],[5,8],[4,6]],
        [[0,6],[4,5]], [[3,5],[1,7],[2,6],[0,8]], [[2,8],[3,4]],
        [[0,3],[7,8],[2,4]],[[1,4],[6,8]], [[2,5],[0,4],[6,7]],
    ]

    for option in winning_paths[player_move]:
        print(f'option is: {option}')
        if player == state[option[0]] and player == state[option[1]]:
            return True

    return False

    #Ugly, but I wanted to experiment with syntax
    # return (
    #     True for options_list in winning_paths for option in options_list if () else False
    # )

def updateBoard(state: list) -> str:
    return f'''
    BOARD
    ***************
    *  {state[6]} | {state[7]} | {state[8]}  *
    *-------------*
    *  {state[3]} | {state[4]} | {state[5]}  *
    *-------------*
    *  {state[0]} | {state[1]} | {state[2]}  *
    ***************
    '''

def play_round():
    players = ['X', 'O']
    moves = 9
    state = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    board = updateBoard(state)

    while (moves):
        print(board)
        player_move = input(f'Player {players[0]}, make a move:\n')

        while not is_legal_move(player_move, state):
            print('Sorry, that move was illegal')
            player_move = input(f'Player {players[0]}, make a move:\n')

        moves -= 1
        player_move = int(player_move) - 1

        state[player_move] = players[0]
        board = updateBoard(state)

        if check_if_won(players[0], player_move, state):
            print(board)
            print(f'Player {players[0]}, well done! You\'re the winner')
            return

        elif (not moves):   
            print('I gues it\'s a draw')
            return

        else:
            players.reverse()

