print('#------------------------EX1------------------------------#')

class Family:
    def __init__(self, last_name: str, members: list) -> None:
        self.last_name = last_name
        self.members = members
    
    def born(self, **kwargs):
        self.members.append(kwargs)
        print('Congrats!')

    def is_18(self, name):
        for member in self.members:
            if name == member['name']:
                return member['age'] >= 18

        print('member not found!')

    def show_family(self):
        for member in self.members:
            print(member)



smith_members = [{'name':'Michael','age':35,'gender':'Male','is_child':False},
                 {'name':'Sarah','age':32,'gender':'Female','is_child':False}]


smiths = Family('Smith', smith_members)

smiths.show_family()

smiths.born(name='Jason', age=0, gender='Male', is_child=True)

smiths.show_family()

smiths.is_18('Michael')
smiths.is_18('Sarah')
smiths.is_18('Jason')
smiths.is_18('Matilde')

print('#------------------------EX2------------------------------#')

class TheIncredibles(Family):
    def __init__(self, last_name: str, members: list) -> None:
        super().__init__(last_name, members)

    def use_power(self, name):

        for member in self.members:
            if name == member['name']:
                if self.is_18(member['name']):
                    print(member['power'])
                else:
                    raise Exception('Not over 18 yet!')
    
    def incredible_presentation(self):
        for member in self.members:
            print(f"{member['incredible_name']}: {member['power']}")


incredibles_members = [
    {'name':'Michael','age':35,'gender':'Male',
     'is_child':False, 'power': 'Flying', 'incredible_name': 'SuperFly'},
    {'name':'Sarah','age':32,'gender':'Female',
     'is_child':False, 'power': 'Super strength', 'incredible_name': 'IronMom'}
    ]


incredibles = TheIncredibles('Incredibles', incredibles_members)

incredibles.show_family()
incredibles.incredible_presentation()
incredibles.born(name='JR',age=0,gender='Female',
     is_child=True, power='Nonstop pooping', incredible_name='Poop Machine')
incredibles.show_family()
incredibles.incredible_presentation()
incredibles.use_power('Michael')
incredibles.use_power('Sarah')
incredibles.use_power('JR')