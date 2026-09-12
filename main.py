class Ingredient:
    def __init__(self, name, price, shelf_life):
        self.name = name
        self.price = price
        self.shelf_life = shelf_life

    def change_price(self, newPrice):
        self.price = newPrice

    def change_shelf_life(self, newShelfLife):
            self.shelf_life = newShelfLife

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



def check_inventory(food, cur_recipe, cur_storage):
    if food in cur_recipe:
        valid_recipe = True
        for key, value in cur_recipe[food].items():
            cur_item_name = key
            cur_item_count = value
            print(cur_item_name,cur_item_count)
            if cur_item_name in cur_storage.storage:
                in_inventory = cur_storage.storage[cur_item_name]
                if in_inventory["Quantity"] >= cur_item_count:
                    print(f"Your inventory have {in_inventory['Quantity']} in stock, you have enough units")
                else:
                    in_inventory = cur_storage.storage[cur_item_name]
                    print(f"There are not enough {cur_item_name}, the inventory only has {in_inventory['Quantity']} {cur_item_name}")
                    valid_recipe = False
            else:
                print(f"There are no {cur_item_name} in your inventory")
    else:
        print(f"We do not have any recipe for {food} in our cook book")

    if valid_recipe == False:
        print("This is not a valid recipe")
    else:
        print("This is a valid recipe")