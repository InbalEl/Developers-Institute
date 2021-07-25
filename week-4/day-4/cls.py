my_name = "Jack"
hello = "Hello World"
my_age = 27
# Lists
my_list = [my_name, my_age, hello]
my_list2 = [1,2,3,'hello', 45, 78]
#Accessing data 
hello_var = my_list2[3]
# reassigning data
my_list2[3] = 'hello world'
# updating data
my_list2[0] += 23
# Tuples
my_tuple = (my_name, my_age, hello)
# Tuple with a single object. Note the comma
my_tuple1 = (my_age,)
# Not a tuple
notatuple = (1)
# Convert tuple to list, vice versa
my_tuple_as_list = list(my_tuple)
my_converted_tuple = tuple(my_tuple_as_list)
# result = 7 * (8 + 1)
# Strings are sequences
hello_string = 'hello world'
#access the e by index
print(hello_string[1])
for letter in hello_string:
    print(letter)
list1 = [5, 10, 15, 20, 25, 50, 20]
index_of_20 = list1.index(20)
list1[index_of_20] = 200
print(list1)
# ranges
num_list = list(range(0,100))
for num in range(0,100):
    if num % 3 == 0:
        print('im divisable by 3')
    print(num)
fruits = ['apple', 'banana', 'kiwi', 'pear']
for fruit in fruits:
  print(fruit)
cities = ["Tel Aviv", "San Francisco", "Paris", "Barcelona"]
for city in cities:
    print("I once went to", city)
# Enumerate
for index, city_name in enumerate(cities):
    print(index, city_name)
while True:
    user_input = input('Give us a number between 1-100: ')
    if not user_input.isnumeric():
        print('not a number')
    elif int(user_input) > 100:
        print('too large') 
    elif int(user_input) < 1:
        print('too small')
    else:
        print('valid input')
        break
print('ended loop')
not_valid = True
while not_valid:
    user_input = input('Give us a number between 1-100: ')
    if not user_input.isnumeric():
        print('not a number')
    elif int(user_input) > 100:
        print('too large') 
    elif int(user_input) < 1:
        print('too small')
    else:
        print('valid input')
        not_valid = False
active = True
visited_cities = []
while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)
        visited_cities.append(city)
print('these are the cities youve visited:')
for city in visited_cities:
    print(f'\t* {city}')
print("Goodbye !")