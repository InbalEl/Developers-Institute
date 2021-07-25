class Farm:
    def __init__(self, name, info = 'E-I-E-I-0!') -> None:
        self.name = name
        self.info = info
        self.animals = {}

    def get_name(self):
        return self.name

    def add_animal(self, animal_name, animal_amount=1):

        if animal_name not in self.animals.keys():
            self.animals[animal_name] = animal_amount    

        else:
            self.animals[animal_name] += animal_amount

    def get_info(self):
        return self.info

    def get_short_info(self):
        animals = self.get_animal_types()
        animals_str = 's, '.join(animals[:-1]) + 's and ' + animals[-1]
        return f'{self.name}\'s farm has {animals_str}'

    def get_animals(self):
        return self.animals

    def get_animal_types(self):
        return sorted(self.animals.keys())

#--------------------------------------------------------------------------#

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_animals())
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())




'''

McDonald's farm

cow : 5
sheep : 2
goat : 12

    E-I-E-I-0!

'''