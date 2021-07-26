print('#-----------------------EX1----------------------------#')

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class British(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_bengal_cat = Bengal('Brad', 5)
my_chartreux_cat = Chartreux('Layla', 3)
my_british_cat = British('Sean', 8)

my_pets = Pets([my_bengal_cat, my_chartreux_cat, my_british_cat])
my_pets.walk()

print('#-----------------------EX2----------------------------#')

class Dog():
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return (self.weight / self.age * 10)

    def fight(self, other_dog):
        winner = ''
        if ((self.run_speed() * self.weight) > (other_dog.weight * other_dog.weight)):
            winner = self.name
        else:
            winner = other_dog.name

        return f'{winner} won the fight'


dog_list = [Dog('Pickachu', 2, 12), Dog('Charmander', 4, 15),Dog('Bulbazour', 5, 18)]

for dog in dog_list:
    dog.bark()

for dog in dog_list:
    print(dog.run_speed())

print(dog_list[0].fight(dog_list[1]))
print(dog_list[1].fight(dog_list[2]))
print(dog_list[0].fight(dog_list[2]))

print('#-----------------------EX3----------------------------#')

