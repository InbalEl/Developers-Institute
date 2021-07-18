username = input('Please enter a username: ')
password = input('Please enter a password: ')
pass_len = len(password)

print(f'{username}, the password {"*" * pass_len} is {pass_len} characters long')