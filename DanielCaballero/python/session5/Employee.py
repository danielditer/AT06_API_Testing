from DanielCaballero.python.session5.Person import Person


class Employee(Person):
    def __init__(self, name, last_name, age, ci, employee_id, departament):
        super().__init__(name, last_name, age, ci)
        self.employee_id = employee_id
        self.departament = departament


employee1 = Employee("Juan", "Perez", 28, 5635467, 123, "IT")

print(f"My name is {employee1.name} {employee1.lastname} I am {employee1.age} years old")
print(f"My ci is {employee1.ci}, my id is {employee1.employee_id} and I work in {employee1.departament} departament")
