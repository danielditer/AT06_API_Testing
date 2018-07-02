import logging

from DanielCaballero.python.session5.Item import Item

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('Test_Log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Shopping:
    def __init__(self):
        self.list_items = []

    def add_item(self, item, price, amount):
        prod = Item(item, price, amount)
        self.list_items.append(prod)
        logger.debug('Adding product to store')

    def display_products(self):
        print("List Products")
        print("ITEMS \t | PRICES \t | AMOUNT")
        for prod in self.list_items:
            prod.print_item()
        logger.info('Show products of store')

    def exist_item(self, item):
        for prod in self.list_items:
            if prod.name == item:
                return True
        return False

    def available_amount(self, amount, item):
        for prod in self.list_items:
            if prod.name == item and int(prod.amount) >= int(amount):
                logger.info('item {0} available for sell'.format(prod.name))
                return True
        return False

    def get_product(self, item):
        for prod in self.list_items:
            if prod.name == item:
                logger.info('Get item: {0}'.format(prod.name))
                return prod

    def sell_item(self, item, amount):
        for prod in self.list_items:
            if prod.name == item and prod.amount >= int(amount):
                prod.set_amount(prod.get_amount() - int(amount))
                logger.debug('Product {0} was sold'.format(prod.name))
