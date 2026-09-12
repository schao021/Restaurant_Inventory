class Ingredient:
    def __init__(self, name, price, shelf_life):
        self.name = name
        self.price = price
        self.shelf_life = shelf_life

    def change_price(self, newPrice):
        self.price = newPrice

    def change_shelf_life(self, newShelfLife):
            self.shelf_life = newShelfLife

# Recipe = {
#           "Pancake": {"flour" : 2, 
#                       "milk": 3, 
#                       "egg": 2, 
#                       "butter" : 1,
#           }
#      }

class Recipe:
    def __init__ (self):
          self.Recipe_List = {}

    def add_recipe(self, food_name, Food_Recipe):
        if food_name in self.Recipe_List:
            print(f"There are already a recipe for {food_name}")
        else:
            self.Recipe_List[food_name] = Food_Recipe

    def remove_recipe(self, food_name):
        self.Recipe_List.pop(food_name, f"There are no {food_name} in the cook book")


class Inventory:
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


