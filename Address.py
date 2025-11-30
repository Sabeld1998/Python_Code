class Address:
    def __init__(self, street_address, city, state, zip_code):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code

    def __str__(self):
        return f"Street Address: {self.__street_address}\nCity: {self.__city}\nState: {self.__state}\nZip: {self.__zip_code}"