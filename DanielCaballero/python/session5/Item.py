import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('Test_Log.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class Item:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def get_price(self):
        logger.debug('get price: %s', self.price)
        return self.price

    def get_amount(self):
        logger.debug('get amount: %s', self.amount)
        return self.amount

    def set_price(self, price):
        self.price = price
        logger.debug('set price: %s', self.price)

    def set_amount(self, amount):
        self.amount = amount
        logger.debug('set amount: %s', self.amount)

    def print_item(self):
        print("{0} \t | {1} \t | {2}".format(self.name, self.price, self.amount))