from main import Ingredient
from main import Inventory
from main import Recipe


# Recipe = {
#           "Pancake": {"flour" : 2, 
#                       "milk": 3, 
#                       "egg": 2, 
#                       "butter" : 1,
#           }
#      }


# Scenario 1, not enough ingredients
item1 = Ingredient("flour",3,10)
item2 = Ingredient("milk", 2, 10)
item3 = Ingredient("egg",3,10)
item4 = Ingredient("butter",1,10)
simon_storage = Inventory()
simon_storage.add_item("flousr",item1,3)
simon_storage.add_item("milk", item2, 2)
simon_storage.add_item("egg", item3, 3)
simon_storage.add_item("butter", item4, 1)
simon_recipe = Recipe()
simon_recipe.add_recipe("Pancake", {"flour" : 2, 
                      "milk": 3, 
                      "egg": 2, 
                      "butter" : 1})
cur_recipe = simon_recipe.Recipe_List
food = "Pancake"
if food in cur_recipe:
    for key, value in cur_recipe[food].items():
        cur_item_name = key
        cur_item_count = value
        print(cur_item_name,cur_item_count)
        if cur_item_name in simon_storage.storage:
            in_inventory = simon_storage.storage[cur_item_name]
            if in_inventory["Quantity"] >= cur_item_count:
                in_inventory["Quantity"] -= cur_item_count
                print(f"The inventory now has {in_inventory['Quantity']} {cur_item_name}")
            else:
                in_inventory = simon_storage.storage[cur_item_name]
                print(f"There are not enough {cur_item_name}, the inventory only has {in_inventory['Quantity']} {cur_item_name}")
        else:
            print(f"There are no {cur_item_name} in your inventory")
else:
    print(f"We do not have any recipe for {food} in our cook book")