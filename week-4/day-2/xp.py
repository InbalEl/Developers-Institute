my_fav_numbers = {42, 18, 5, 33}
print(my_fav_numbers)
print(type(my_fav_numbers))
my_fav_numbers.pop()
print(my_fav_numbers)
friend_fav_numbers = {41, 19, 5, 32}
print(type(friend_fav_numbers))

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)
print(type(our_fav_numbers))

# Tuples - immutable, cannot be changed once created

for item in range(1, 21):
    print(item)

# float - a decimal number.
# division between to ints would result in a float always

float_list = [num/2 for num in range(3, 11)]

print(float_list)


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
basket.pop()
print(basket)
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

my_name = 'The king of Rock N Roll'
user_name = input("Please enter your name: ")

#while (user_name != my_name):
#    user_name = input("Please enter your name: ")

ex_7_list = [0,1,2,3,4,5,6,7,8,9]

for index, item in enumerate(ex_7_list):
    if index % 2 == 0:
        print(item)

for index, item in enumerate(list(range(1500, 2501))):
    if index % 5 == 0 and index % 7 == 0:
        print(item)

user_fav_fruit_str = input('Please enter your favorite fruits, separated by a space: ')
user_fruits = list(user_fav_fruit_str.split(' '))

user_picked_fruit = input('Pick a fruit: ')

if user_picked_fruit in user_fruits:
    print('You picked one of your favorite fruits! Enjoy!')
else:
    print('You picked a new fruit, I hope you enjoy')

def CalculateTicketPriceTotal(ages: list) -> int:
    total = 0
    for person_age in ages:
        if 3 <= person_age <= 12:
            total += 10
        elif person_age > 12:
            total += 15
    
    return total

family_ages = input('please enter family members\' age, separated by space: ')
family_total_price = CalculateTicketPriceTotal(list(map(int, family_ages.split())))
print(f'Family total price = {family_total_price}')

def ValidateAge(names: list) -> list:
    for name in names:
        user_age = int(input(f'{name}, how old are you?'))
        if user_age < 16:
            names.remove(name)

    print(names)

sandwich_orders = ['tuna', 'pastrami', 'sloppy joe', 'pastrami', 'egg', 'pastrami', 'chicken', 'cheese']
finished_sandwiches = []

print('Oh no! we\'ve out of pastrami!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)

for sandwich in finished_sandwiches:
    print(f'I made your {sandwich} sandwich')