def parseUserInput(user_input):
    if len(user_input) < 10:
        print('string not long enough')
    elif len(user_input) > 10:
        print('string too long')

user_input = input('Please enter a string at least 10 characters long: ')

parseUserInput(user_input)

print(user_input[:1])
print(user_input[-1:])

for index, char in enumerate(user_input):
    print(user_input[:index+1])

import random

l = list(user_input)
random.shuffle(l)
shuffled_user_input = ''.join(l)
print(shuffled_user_input)