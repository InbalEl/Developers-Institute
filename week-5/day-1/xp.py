#----------EX1------------#

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
def get_oldest_cat(*args):
    cat_list = list(args)
    cat_list.sort(key=lambda cat: cat.age)
    return cat_list[-1]


Mitzi = Cat('Mitzi', 9)
Methuselah = Cat('Methuselah', 16)
Doctor = Cat('Doctor', 6)

print(f'Youngest cat is: {min(Mitzi.getAge(), Methuselah.getAge(), Doctor.getAge())}')
oldest_cat = get_oldest_cat(Mitzi, Methuselah, Doctor)

print(f'The oldest cat is {oldest_cat.getName()}, and is {oldest_cat.getAge()} years old')

#----------EX2------------#

class Dog:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height

    def getName(self):
        return self.name

    def getHeight(self):
        return self.height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high!')

davids_dog = Dog('Rex', 50)

print(f'{davids_dog.getName()} is {davids_dog.getHeight()}cm tall')
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(f'{sarahs_dog.getName()} is {sarahs_dog.getHeight()}cm tall')
sarahs_dog.bark()
sarahs_dog.jump()

if (davids_dog.getHeight() > sarahs_dog.getHeight()):
    print(f'{davids_dog.getName()} is bigger!')

elif (davids_dog.getHeight() < sarahs_dog.getHeight()):
    print(f'{sarahs_dog.getName()} is bigger!')

else:
    print('I guess they\'re both the same height..')

#----------EX3------------#

class Song:
    def __init__(self, lyrics: list) -> None:
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#----------EX4------------#

class Zoo:
    def __init__(self, zoo_name) -> None:
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        if (animal_sold in self.animals):
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        self.animals.sort()
        self.groups = dict(map(self.animals, numbers))
    
    def get_groups(self):
        if hasattr(self, 'groups'):
            for group in self.groups:
                print(group)

ramat_gan_safari = Zoo('ramat_gan_safari')


ramat_gan_safari.add_animal('Lion')
ramat_gan_safari.add_animal('Giraffe')
ramat_gan_safari.add_animal('Rino')
ramat_gan_safari.add_animal('Hippo')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('Elephant')
ramat_gan_safari.add_animal('Python')
ramat_gan_safari.add_animal('Ape')

ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Baboon')
ramat_gan_safari.sell_animal('cockatoo')
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
