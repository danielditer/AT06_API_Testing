from DanielCaballero.python.session5.Item import Item


class PurchaseItem:
    def __init__(self):
        self.shopping_cart = []

    def ask_for_buying(self, products):
        while (True):
            print("Enter item to buy: ", end='')
            item = str(input())
            print("Enter quantity that you want buy: ", end='')
            amount = input()
            if self.buy_product(products, item, amount):
                item_to_buy = products.get_product(item)
                item = Item(item, item_to_buy.get_price(), amount)
                self.shopping_cart.append(item)
            print("Do you want to continue buying? [y/n]: ", end='')
            asnwer = input()
            if asnwer == 'n':
                return

    def buy_product(self, products, item, quantity):
        if products.available_amount(quantity, item):
            products.sell_item(item, quantity)
            return True
        return False

    def display_cart(self):
        total = 0.0
        print("List Products Buying")
        print("ITEMS \t | PRICES \t | AMOUNT")
        for prod in self.shopping_cart:
            prod.print_item()
            total += (prod.get_price() * float(prod.get_amount()))
        print('==================')
        print("TOTAL: {0} $us.".format(total))
        print('==================')