from xp import Dog
import random
class PetDog(Dog):
    
    def __init__(self, name, age, weight, trained: bool=False) -> None:
        Dog.__init__(self, name, age, weight)
        self.trained = trained

    def train(self):
        print(f'{self.bark()}')
        self.trained = True
    
    def play(self, *args):
        
        dog_names = []

        for dog in args[0]:
            print(type(args))
            print(type(dog))
            print(dog)
            dog_names.append(dog.name)

        print(f'{dog_names} all play together')

    def do_a_trick(self):
        tricks = ['does a barrel roll',
                  'stands on his back legs',
                  'shakes your hand',
                  'plays dead']

        if self.trained:
            print(f'{self.name} {tricks[random.randint(0,3)]}')

print('#----------------------------EX3-----------------------------------#')

my_pet_dogs = [PetDog('Bob', 11, 22),
               PetDog('Malcowitz', 7, 17),
               PetDog('Matilde', 5, 16)]

for dog in my_pet_dogs:
    print(dog.bark())

dog.play(my_pet_dogs)

my_pet_dogs[0].train()

my_pet_dogs[0].do_a_trick()
my_pet_dogs[1].do_a_trick()