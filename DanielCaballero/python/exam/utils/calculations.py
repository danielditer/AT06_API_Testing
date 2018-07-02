CE = "CE_0"
PE = "PE_0"


def calculate_discount(global_salary):
    return (global_salary * 12.5) / 100


def calculate_net_salary(global_salary, discount):
    return global_salary - discount


def generate_id(identifier, number: int):
    if identifier is CE or identifier is PE:
        return identifier + str(number)
