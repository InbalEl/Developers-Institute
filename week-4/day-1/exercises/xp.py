print('Hello world\n' * 5)

print((99^3) * 8)
print((99**3) * 8)
print(5 < 3)
print(3 == 3)
print(3 == '3')
# print("3" > 3)
print('Hello' == 'hello')

def greet1(name, question):
    return (f'hello {name}! How\'s it {question}?')
def greet2(name, question):
    return ('hello {name}! How\'s it {question}?'.format())

import dis

dis.dis(greet1)

print('--------------------------------')

dis.dis(greet2)

print('--------------------------------')

my_comp = 'Dell Inspiron'

print(f'I have a {my_comp} computer')

print('--------------------------------')

name = 'Inbal'
age = 32
shoe_size = 42
info = f'Hi, my name is {name} and I\'m {age}yo. My shoe size is {shoe_size} so feel free to get me a pair.'

print(info)
print('--------------------------------')

a = 6
b = 5

if a > b:
    print('Hello world!')

print('--------------------------------')

user_name = input ('What is your name? ')

if (name == user_name):
    print('that\' a beautiful name!')
else:
    print('you suck.')

user_height = input ('What is your height in inches? ')

if int(user_height)*2.54 < 145:
    print('Sorry shortie')
else:
    print('You may pass!')