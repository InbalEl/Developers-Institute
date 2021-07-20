def encrypt(user_input: dict) -> str:

    user_input['result'] = ''
    for letter in user_input['message']:
        user_input['result'] += chr(ord(letter) + user_input['shift'])

    return user_input['result']

def decrypt(user_input: dict) -> str:

    user_input['result'] = ''
    for letter in user_input['message']:
        user_input['result'] += chr(ord(letter) + user_input['shift'])

    return user_input['result']


def parse_input(user_input: str) -> str:
    input_list = user_input.split(', ')
    input_dict = {
        'type': input_list[0],
        'shift': int(input_list[1]),
        'message': ' '.join(input_list[2:])
    }

    if input_dict['type'] == 'dec':
        return decrypt(input_dict)
    else:
        return encrypt(input_dict)

#------------------------------------------------------------------------------#

# user_input = input('Please enter: <dec/enc>, <shift>, <message>\n(or exit to leave program):\n')

# while (user_input != exit):
#     print(parse_input(user_input))

#     user_input = input(
#     'Please enter: <dec/enc>, <shift>, <message>\n(or exit to leave program):\n')

result = parse_input('enc, 12, hello world')

print(result)
print(parse_input(f'dec, -12, {result}'))