from DanielCaballero.python.exam.Person import *
from DanielCaballero.python.exam.utils.calculations import calculate_discount, calculate_net_salary


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('application.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


class Employee(Person):

    def __init__(self, id, name, department):
        super().__init__(name)
        self.employee_id = id
        self.employee_department = department
        self.global_salary = 0
        self.total_discount = 0
        self.net_salary = 0


    def get_employee_id(self):
        return self.employee_id

    def get_employee_name(self):
        return self.name

    def get_employee_department(self):
        return self.employee_department

    def get_global_salary(self):
        return self.global_salary

    def get_total_discount(self):
        return self.total_discount

    def get_net_salary(self):
        return self.net_salary

    def print_employee(self):
        print("Employee ID | NAME | Department | Global Salary | Total Discount | Net Salary")
        print(
            f"{self.employee_id} | {self.name} | {self.employee_department} | {self.global_salary} | {self.total_discount} | {self.net_salary}")

    def calculate_global_salary(self):
        pass

    def calculate_discount(self):
        self.total_discount = calculate_discount(self.global_salary)
        return self.total_discount

    def calculate_net_salary(self):
        self.net_salary = calculate_net_salary(self.global_salary, self.total_discount)
        return self.net_salary