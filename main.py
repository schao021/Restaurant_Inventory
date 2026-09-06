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
    def __init__(self):
         self.storage = {}
    # Dictionary, first parameter ItemName (String), Second Ingredient Dict
    def add_item(self, name, Item, Count):
        if (name in self.storage):
             self.storage[name]["Quantity"] += Count
        else:
             self.storage[name] = {"Item" : Item, "Quantity": Count}

    def remove_item (self, name, Count):
        if (name in self.storage):
              # Can either remove the item completely, or change count to 0
            if Count <= self.storage[name]["Quantity"]:
                self.storage[name]["Quantity"] -= Count
                print(f"{Count} {name} were removed from inventory")
            else:
                cur_count = self.storage[name]["Quantity"]
                print(f"There are only {cur_count} {name} left, we are unable to remove {Count}")
        else:
             print(f"There are no {name} in the inventory, please enter another item") 

corn = Ingredient("corn", 0.50, 7)
corn.change_price(1.0)
corn.change_shelf_life(10)
print(corn.price, corn.shelf_life)
simon_storage = inventory()
simon_storage.add_item("corn", corn, 3)
print(simon_storage.storage["corn"]["Item"].price)
simon_storage.add_item("sugar", Ingredient("sugar", 0.25, 20), 10)
simon_storage.add_item("corn", corn, 20)
print(simon_storage.storage)
simon_storage.remove_item("corn", 50)
print(simon_storage.storage)