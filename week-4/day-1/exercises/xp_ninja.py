print(3 <= 3 < 9) # True
print('expected: True')
print(3 == 3 == 3) # True
print('expected: True')
print(bool(0)) # False
print('expected: False')
print(bool(5 == "5")) # False
print('expected: False')
print(bool(4 == 4) == bool("4" == "4")) # True
print('expected: True')
print(bool(bool(None))) # False
print('expected: False')


x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

my_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.'''

print(len(my_text) - my_text.count(' '))

longest_string_with_no_A = ''

while(True):
    user_input = input('Please enter the longest possible sentence without the character A: ')
    if user_input.count('A') == 0:
        longest_string_with_no_A = user_input
        print('Congrats!')
    else:
        print('Try harder...')
