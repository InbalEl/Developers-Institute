print('Hello world\n' * 5 + 'I love python\n' * 5)

user_month = int(input('What is the current month? enter number from 1 to 12 :'))

if 3 <= user_month <= 5:
    print('Spring!') 
elif 6 <= user_month <= 8:
    print('Summer!') 
elif 9 <= user_month <= 11:
    print('Autumn!') 
else:
    print('Winter!') 