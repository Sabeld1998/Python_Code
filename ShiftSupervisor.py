from Employee import Employee

class ShiftSupervisor(Employee):
    def __init__(self, name, employee_ID_number, address_obj, annual_salary, annual_production_bonus):
        super().__init__(name, employee_ID_number, address_obj)
        self.__annual_salary = annual_salary
        self.__annual_production_bonus = annual_production_bonus

    def __str__(self):
        return f"{super().__str__()}\nAnnual Salary: {self.__annual_salary}\nAnnual Production Bonus: {self.__annual_production_bonus}"

# Program 4: Main
