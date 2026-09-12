from main import Ingredient
from main import Inventory


corn = Ingredient("corn", 0.50, 7)
corn.change_price(1.0)
corn.change_shelf_life(10)
print(corn.price, corn.shelf_life)
simon_storage = Inventory()
simon_storage.add_item("corn", corn, 3)
print(simon_storage.storage["corn"]["Item"].price)
simon_storage.add_item("sugar", Ingredient("sugar", 0.25, 20), 10)
simon_storage.add_item("corn", corn, 20)
print(simon_storage.storage)
simon_storage.remove_item("corn", 50)
print(simon_storage.storage)