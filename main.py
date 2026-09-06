class Ingredient:
    def __init__(self, name, price, shelf_life):
        self.name = name
        self.price = price
        self.shelf_life = shelf_life

    def change_price(self, newPrice):
        self.price = newPrice

    def change_shelf_life(self, newShelfLife):
            self.shelf_life = newShelfLife

Recipe = [
     {
          "Food_Name": "Pancake",
          "ingredient_needed" : {"flour" : 2, 
                                  "milk": 3, 
                                  "egg": 2, 
                                  "butter" : 1, 
                                  "sugar": 5}
     }
]

class inventory:
    def __init__(self, ItemName, Item, Count):
        self.storage = {ItemName : {"Item" : Item, "Quantity": Count}}
# Dictionary, first parameter ItemName (String), Second Ingredient Dict

    def add_item(self, name, Item, Count):
         self.storage[name] = {"Item" : Item, "Quantity": Count}

corn = Ingredient("corn", 0.50, 7)
corn.change_price(1.0)
corn.change_shelf_life(10)
print(corn.price, corn.shelf_life)
simon_storage = inventory("corn", corn, 3)
print(simon_storage.storage["corn"]["Item"].price)
simon_storage.add_item("sugar", Ingredient("sugar", 0.25, 20), 10)
print(simon_storage.storage)