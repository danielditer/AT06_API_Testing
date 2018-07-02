

from DanielCaballero.python.exam.Employee import *

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('application.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

class CommercialEmployee(Employee):

    def __init__(self, id, name, departament, pieces_selled):
        super().__init__(id, name, departament)
        self.pieces_selled = pieces_selled

    def calculate_global_salary(self):
        self.global_salary = self.pieces_selled * 2.5
        return self.global_salary
