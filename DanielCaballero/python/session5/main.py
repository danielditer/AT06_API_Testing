# 1. Lets’ assume you are a user for an online shopping page (like amazon)
#  Define initial data for :
# 	Items
# 	Prices
# 	Amount
# 2. Create a class to pickup items
# 3. According the amount of items picked . Create a class considering :
#   Initial  amount of items to buy are 0
#   Initial list of items with the specific price for each one
#   Initial list of items with the quantity of each one
# 4. Create a class to perform purchase an item(ask for the item and for the amount,
# after an item is buy, you should decrease the amount of data,
# also need to calculate the total price, after this is calculated need to ask
# if the user would like to buy any other item.
# 5. Create a logger for each action
# 6. Print the list of items selected and the price calculated for each one
# 7. Print the balance of each item.


from DanielCaballero.python.session5.PurchaseItem import PurchaseItem
from DanielCaballero.python.session5.Shopping import Shopping

shop = Shopping()
shop.add_item("001", 12.5, 10)
shop.add_item("002", 15.0, 200)
shop.add_item("003", 124.2, 5)
shop.add_item("004", 63.0, 52)
shop.display_products()

# cart = Shopping_cart()
# cart.buy_product(shop, "001", 7)
# cart.buy_product(shop, "002", 200)
# cart.buy_product(shop, "003", 1)
# cart.buy_product(shop, "004", 50)
# shop.display_products()


cart = PurchaseItem()
cart.ask_for_buying(shop)
cart.display_cart()
shop.display_products()


# print(shop.exist_item("008"))
# print(shop.available_amount(11, "001"))