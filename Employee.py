class Employee:
    def __init__(self, name, employee_ID_number, address_obj):
        self.__name = name
        self.__employee_ID_number = employee_ID_number
        self.__address_obj = address_obj

    def setName(self, name):
        self.__name = name

    def setEmployeeIDNumber(self, employee_ID_number):
        self.__employee_ID_number = employee_ID_number

    def setAddress(self, address_obj):
        self.__address_obj = address_obj

    def getName(self):
        return self.__name

    def getEmployeeIDNumber(self):
        return self.__employee_ID_number

    def getAddress(self):
        return self.__address_obj

    def __str__(self):
        return f"Name: {self.__name}\nEmployee ID: {self.__employee_ID_number}\nAddress: {self.__address_obj}"
