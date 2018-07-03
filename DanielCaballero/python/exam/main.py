# Module: main

import logging

from DanielCaballero.python.exam.CommercialEmployee import CommercialEmployee
from DanielCaballero.python.exam.ProductionEmployee import ProductionEmployee
from DanielCaballero.python.exam.utils.calculations import generate_id

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

handler = logging.FileHandler('application.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

employees = []


class Main():

    def register_new_employee(self):
        logger.info("Executing main program")
        employees_quantity = int(input("Insert the quantity of employees to be registered: "))
        if 2 < employees_quantity < 16:
            for i in range(employees_quantity):
                employee_name = input("Insert the name of the employee: ")
                employee_department = input("Insert the departament: ")
                if employee_department.lower() == "commercial":
                    amount_of_pieces_sell = int(input("Employee amount of pieces sell?: "))
                    logger.info("Creating commercial employee")
                    commercialEmployee = CommercialEmployee(generate_id("CE_0", i), employee_name, employee_department,
                                                            amount_of_pieces_sell)
                    commercialEmployee.calculate_global_salary()
                    commercialEmployee.calculate_discount()
                    commercialEmployee.calculate_net_salary()
                    logger.debug('Registrys: %s', commercialEmployee.print_employee())
                    employees.append(commercialEmployee)
                elif employee_department.lower() == "production":
                    logger.info("Creating production_employee")
                    pieces_produced = int(input("Insert the quantity of pieces produced?: "))
                    defective_pieces = int(input("Insert the quantity of defective pieces?: "))
                    productionEmployee = ProductionEmployee(generate_id("PE_0", i), employee_name, employee_department,
                                                            pieces_produced, defective_pieces)
                    productionEmployee.calculate_global_salary()
                    productionEmployee.calculate_discount()
                    productionEmployee.calculate_net_salary()
                    logger.debug('Registrys: %s', productionEmployee.print_employee())
                    employees.append(productionEmployee)
        else:
            print("Invalid quantity")
            logger.info("Invalid quantity")

main = Main()
main.register_new_employee()
