from hashlib import new
import requests
import time

def timeResponse(url: str):
    print(url)
    start = time.perf_counter()
    response = requests.get(url)
    end = time.perf_counter()
    
    print(response.status_code)
    print(f'response elapsed field: {response.elapsed.total_seconds()}')
    return end - start

print(f'delta, according to time lib: {timeResponse("https://www.ynet.co.il")}')
print(f'delta, according to time lib: {timeResponse("https://www.youtube.com/")}')
print(f'delta, according to time lib: {timeResponse("https://www.yellowheadinc.com/were-hiring/#career-opportunities")}')

#------------------------------ OOP QUIZ -------------------------------------#

# 1:
# A 'blueprint' for the creation of a user defined object.
# Can have methods and attributes.

# 2:
# An instance is an actual object of a calss - created according to its 'blueprint'

# 3:
# THe consept of controlling the user's access to certain parts of the code
# that are sensitive, or just ipmlementation related and so not relevant to her/him.

# 4:
# the process of generalizing a certain rule.

# 5:
# Inheritance is one techneque to accomplish polymorphim in code, i.e,
# creating objects that behave differently according to their type.
# Inheritance does this by creating a relationship between 2 classes,
# allowing a derived class to inherit methods, attributes and/or inteface
# from a base class.

# 6:
# A class which is derived of 2 or more base classes.
# Could be risky business, since it allows the occurance of the diamond problem.

# 7:
#  defined in the answer to 5.

# 8:
# The rules by with the python interperter searched for methods called on
# in the context of inheritance. in the code - according to scope, and for the most specific up to the general.

import random
class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
    
    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'

class Deck:

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    def __init__(self) -> None:
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
    
    def deal(self) -> Card:
        dealt_card = self.cards.pop(random.randint(0, len(self.cards)))
        return dealt_card

    def __str__(self) -> str:
        res = ''
        for card in self.cards:
            res += str(card)
            res += '\n'
        return res

new_deck = Deck()
print(new_deck)
print('--------SHUFFLING-----------')
new_deck.shuffle()
print(new_deck)
print('--------DEALING 4 CARDS-----------')
print(f'Dealt card: {new_deck.deal()}')
print(f'Dealt card: {new_deck.deal()}')
print(f'Dealt card: {new_deck.deal()}')
print(f'Dealt card: {new_deck.deal()}')
print('--------PRINTING DECK-----------')
print(new_deck)