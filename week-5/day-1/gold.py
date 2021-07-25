#----------EX1------------#

import math

class Circle:

    definition = 'A circle is a shape consisting of all points in a plane that are at a given distance from a given point, the centre'

    def __init__(self, radius = 1.0) -> None:
        self.radius = radius

    def calc_perimeter(self):
        return 2 * self.radius * math.pi
    
    def calc_area(self):
        return (self.radius**2) * math.pi
    
    def printDefinition(self):
        print(Circle.definition)

#----------EX2------------#

import random

class MyList:
    def __init__(self, letters: list) -> None:
        self.letters = letters

    def get_list(self):
        return self.letters

    def get_reversed_list(self):
        return self.letters[::-1]

    def get_sorted_list(self):
        return sorted(self.letters)

    def get_random_list(self):
        return [random.randint(0, 100)for i in range(len(self.letters))]

new_list = MyList(['H','e','l','l','o', ' ', 'W', 'o', 'r', 'l', 'd'])

print(new_list.get_list())
print(new_list.get_reversed_list())
print(new_list.get_list())
print(new_list.get_sorted_list())
print(new_list.get_list())
print(new_list.get_random_list())


#----------EX3------------#

import menu_manager

my_menu = menu_manager.MenuManager()

my_menu.add_dish('Soup', 10, 'B', False)
my_menu.add_dish('Hamburger', 15, 'A', True)
my_menu.add_dish('Salad', 18, 'A', False)
my_menu.add_dish('French Fries', 5, 'C', False)
my_menu.add_dish('Beef bourguignon', 25, 'B', True)

my_menu.show_dishes()
print('----------------------------------------')
my_menu.remove_dish('Memulawach')
my_menu.remove_dish('Hamburger')
my_menu.show_dishes()
print('----------------------------------------')
my_menu.update_dish('Salad', 20, 'A', False)
my_menu.show_dishes()
print('----------------------------------------')
