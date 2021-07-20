# Ex 1 -----------------------------------------------------------------------#

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)

# Ex 2 -----------------------------------------------------------------------#

def calc_price_total(family_members: dict) -> int:
    ttl = 0
    for name, age in family_members.items():
        age = int(age)
        if 3 <= age <= 12:
            ttl += 10
        elif 12 < age:
            ttl += 15
    return ttl

print('Smith family price: ' + str(calc_price_total({"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8})))

# user_input = input('Please enter family members, one at a time, or type exit to stop entering data: ')

# names = []
# ages = []

# while (user_input != 'exit'):

#     person = user_input.split()
#     names.append(person[0])
#     ages.append(person[1])
#     user_input = input('Please enter family members, one at a time, or type exit to stop entering data: ')

# family_dict = dict(zip(names, ages))
# print(calc_price_total(family_dict))


# Ex 3 -----------------------------------------------------------------------#
brand = {
'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona', 
'type_of_clothes': 'men, women, children, home',
'international_competitors': 'Gap, H&M, Benetton', 
'number_stores': 7000,
'major_color': {
    'France': 'blue',
    'Spain': 'red',
    'US': 'pink, green'
    }
}

for key, val in brand.items():
    print(f'{key}: {val}')

brand['number_stores'] = 2

for key, val in brand.items():
    print(f'{key}: {val}')

print(f'{brand["name"]}\'s clients include anyone interested in clothes for {brand["type_of_clothes"]}')

brand['country_creration'] = 'Spain'

for key, val in brand.items():
    print(f'{key}: {val}')

if brand.get('international_competitors'):
    brand['international_competitors'] += ', Desigual'

for key, val in brand.items():
    print(f'{key}: {val}')

brand.pop('creation_date', None)

print(brand['international_competitors'].split(', ')[-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

more_on_zara = {
    'creation_date': 1975, 
    'number_stores': 10000
    }

brand.update(more_on_zara)

for key, val in brand.items():
    print(f'{key}: {val}')

print(brand['number_stores'])
# What happened is that we updated an exisitng K-V pair instead of inserting it :)

# Ex 3 -----------------------------------------------------------------------#

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
#1/

disney_users_A = {i:name for i, name in enumerate(users)}
print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

disney_users_B = {name:i for i, name in enumerate(users)}
print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

disney_users_C = {i:name for i, name in enumerate(sorted(users))}
print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

#4/

disney_users_D = {i:name for i, name in enumerate(users) if 'i' in name}
print(disney_users_D)

disney_users_F = {i:name for i, name in enumerate(users) if name.startswith('m') or name.startswith('p')}
print(disney_users_F)

disney_users_F = {i:name for i, name in enumerate(users) if name.startswith('M') or name.startswith('P')}
print(disney_users_F)