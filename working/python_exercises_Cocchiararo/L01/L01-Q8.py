'''
Lesson 1 ex 8: Shopping cart
'''
class Item:
    """ an item to buy """
    
    def __init__(self, name, quantity=1):
        """keep track of an item that is in our inventory"""
        if name not in INVENTORY:
            raise ValueError("invalid item name")
        self.name = name
        self.quantity = quantity
        
    def __repr__(self):
        return "{}: {}".format(self.name, self.quantity)
        
    def __eq__(self, other):
        """check if the items have the same name"""
        return self.name == other.name
    
    def __add__(self, other):
        """add two items together if they are the same type"""
        if self.name == other.name:
            return Item(self.name, self.quantity + other.quantity)
        else:
            raise ValueError("names don't match")

class ShoppingCart:
    
    def __init__(self):
        # the list of items we control
        self.items = []
        
    def subtotal(self):
        """ return a subtotal of our items """
        total = 0
        for item in self.items:
            total += INVENTORY[item.name] * item.quantity
        return total

    def add(self, name, quantity):
        """ add an item to our cart -- the an item of the same name already
        exists, then increment the quantity.  Otherwise, add a new item
        to the cart with the desired quantity."""
        new_item = Item(name, quantity)
        for i, item in enumerate(self.items):
            if item == new_item:
                self.items[i] = item + new_item
                return
        self.items.append(new_item)

    def remove(self, name):
        """ remove all of item name from the cart """
        self.items = [item for item in self.items if item.name != name]
        
        
    def report(self):
        """ print a summary of the cart """
        for item in self.items:
            print(f"{item.name} : {item.quantity}")

if __name__ == "__main__":
    INVENTORY_TEXT = '''
apple, 0.60
banana, 0.20
grapefruit, 0.75
grapes, 1.99
kiwi, 0.50
lemon, 0.20
lime, 0.25
mango, 1.50
papaya, 2.95
pineapple, 3.50
blueberries, 1.99
blackberries, 2.50
peach, 0.50
plum, 0.33
clementine, 0.25
cantaloupe, 3.25
pear, 1.25
quince, 0.45
orange, 0.60
    '''

    INVENTORY = {}
    for line in INVENTORY_TEXT.splitlines():
        if line.strip() == '':
            continue
        item, price = line.split(',')
        INVENTORY[item] = float(price)
    #print(INVENTORY)
    sc = ShoppingCart()
    sc.add('orange', 2)
    sc.add('apple', 3)
    sc.add('banana', 5)
    print('shopping cart')
    sc.report()
    print('shopping cart + 1 apple')
    sc.add('apple', 1)
    sc.report()
    print('shopping cart total:', sc.subtotal())
    sc.remove('apple')
    sc.report()
    print('shopping cart total removing the apples:', sc.subtotal())

    