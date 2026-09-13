from main import Ingredient
from main import Inventory
from main import Recipe
from main import check_inventory
from main import cook_recipe


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
simon_storage.add_item("flour",item1,3)
simon_storage.add_item("milk", item2, 3)
simon_storage.add_item("egg", item3, 3)
simon_storage.add_item("butter", item4, 1)
simon_recipe = Recipe()
simon_recipe.add_recipe("Pancake", {"flour" : 2, 
                      "milk": 3, 
                      "egg": 2, 
                      "butter" : 1})
cur_recipe = simon_recipe.Recipe_List
food = "Pancake"

# print(cur_recipe[food])    
simon_storage.add_item(food, cook_recipe(food, cur_recipe, simon_storage),1)
print(simon_storage.storage)