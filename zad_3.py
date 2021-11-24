

class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property in {self.address}. Property area is {self.area} with {self.rooms} rooms.\nPrice: {self.price} PLN."

class House(Property):
    def __init__(self, area : float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House with {self.plot}m2 plot in {self.address}. Property area is {self.area}m2. The house has {self.rooms} rooms.\nPrice: {self.price} PLN."

class Flat(Property):
    def __init__(self, area : float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat with {self.area}m2 area on floor {self.floor} in {self.address}. It has {self.rooms} rooms.\nPrice: {self.price} PLN."

house = House(900, 7, 1950000, "Pomorskie, Gdynia", 320)
flat = Flat(48, 2, 310000, "Świętokrzyskie, Domaszowice", 2)
print(house)
print(flat)