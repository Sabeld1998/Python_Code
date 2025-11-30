# Program 5: ProductionWorker class
from Employee import Employee

class ProductionWorker(Employee):
    def __init__(self, name, employee_ID_number, address_obj, shift_number, hourly_pay_rate):
        super().__init__(name, employee_ID_number, address_obj)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def setShiftNumber(self, shift_number):
        self.__shift_number = shift_number

    def setHourlyPayRate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def getShiftNumber(self):
        return self.__shift_number

    def getHourlyPayRate(self):
        return self.__hourly_pay_rate

    def __str__(self):
        return f"{super().__str__()}\nShift Number: {self.__shift_number}\nHourly Pay Rate: {self.__hourly_pay_rate}"
