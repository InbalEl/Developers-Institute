class MenuManager:
    def __init__(self) -> None:
        self.menu = []
    
    def add_dish(self, name, price, spice, gluten):
        self.menu.append({'name': name, 'price': price,
                          'spice': spice, 'gluten': gluten})    
    
    def remove_dish(self, name):
        for dish in self.menu:
            if dish['name'] == name:
                self.menu.remove(dish)
                return
        else:
            print('dish is not in the menu')

    def update_dish(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish['name'] == name:
                dish['price'] = price
                dish['spice'] = spice
                dish['gluten'] = gluten
        

    def show_dishes(self):
        for dish in self.menu:
            print(dish)

