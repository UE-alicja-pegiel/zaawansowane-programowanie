class Odcinek:
    def __init__(self, odcinek: float):
        self.__odcinek = odcinek

    @property
    def odcinek(self) -> float:
        return self.__odcinek

    @odcinek.setter
    def odcinek(self, wartosc: float):
        self.__odcinek = wartosc

    def __str__(self):
        return f"Odcinek {[self.odcinek]} km."


class Pojazd:
    def __init__(self, marka: str, przebieg: float, kolor: str, drzwi: int):
        self.__marka = marka
        self.__przebieg = przebieg
        self.__kolor = kolor
        self.__drzwi = drzwi

    @property
    def marka(self) -> str:
        return self.__marka

    @marka.setter
    def marka(self, wartosc: str):
        self.__marka = wartosc

    @property
    def kolor(self) -> str:
        return self.__kolor

    @kolor.setter
    def kolor(self, wartosc: str):
        self.__kolor = wartosc

    @property
    def przebieg(self) -> float:
        return self.__przebieg

    @przebieg.setter
    def przebieg(self, wartosc: float):
        self.__przebieg = wartosc

    @property
    def drzwi(self) -> int:
        return self.__drzwi

    @drzwi.setter
    def drzwi(self, wartosc: int):
        self.__drzwi = wartosc

    def __str__(self):
        return f"Samochod {self.drzwi}-drzwiowy o kolorze {self.kolor}, marce {self.marka}, przebiegu {self.przebieg}."


class FirmaTransportowa:
    def __init__(self, nazwa: str, pojazdy: list, kierowcy: list):
        self.__nazwa = nazwa
        self.__pojazdy = pojazdy
        self.__kierowcy = kierowcy

    @property
    def nazwa(self) -> str:
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, wartosc: str):
        self.__nazwa = wartosc

    @property
    def pojazdy(self) -> list:
        return self.__pojazdy

    @pojazdy.setter
    def pojazdy(self, wartosc: list):
        self.__pojazdy = wartosc

    @property
    def kierowcy(self) -> list:
        return self.__kierowcy

    @kierowcy.setter
    def kierowcy(self, wartosc: list):
        self.__kierowcy = wartosc

    def __str__(self):
        return f"Firma {self.nazwa} o dostępnych pojazdach: {[pojazd.marka for pojazd in self.pojazdy]}.\nDostępni " \
               f"kierowcy: {self.kierowcy} "


class Kurs:

    def __init__(self, odcinki: list, cel: str, kierowca: str, firma: FirmaTransportowa, pojazd: Pojazd):
        self.__odcinki = odcinki
        self.__cel = cel
        self.__kierowca = kierowca
        self.__firma = firma
        self.__pojazd = pojazd

    @property
    def lista_odcinkow(self) -> list:
        return self.__odcinki

    @lista_odcinkow.setter
    def lista_odcinkow(self, wartosc: list):
        self.__odcinki = wartosc

    @property
    def cel(self) -> str:
        return self.__cel

    @cel.setter
    def cel(self, wartosc: str):
        self.__cel = wartosc

    @property
    def kierowca(self) -> str:
        return self.__kierowca

    @kierowca.setter
    def kierowca(self, wartosc: str):
        self.__kierowca = wartosc

    @property
    def firma(self) -> FirmaTransportowa:
        return self.__firma

    @firma.setter
    def firma(self, wartosc: FirmaTransportowa):
        self.__firma = wartosc

    @property
    def pojazd(self) -> Pojazd:
        return self.__pojazd

    @pojazd.setter
    def pojazd(self, wartosc: Pojazd):
        self.__pojazd = wartosc

    def suma_kilometrow(self):
        suma = 0
        for element in self.lista_odcinkow:
            suma += element.odcinek
        return suma

    def marka(self):
        return self.pojazd.marka

    def __str__(self):
        return f"Kurs na odcinkach {[element.odcinek for element in self.lista_odcinkow]}, czyli na trasie " \
               f"{self.suma_kilometrow():.2f} km do {self.cel} realizowany przez firmę {self.firma.nazwa}." \
               f"\nKierowcą samochodu marki {self.marka()} jest {self.kierowca}. "


class FirmaSpozywcza(FirmaTransportowa):
    def __init__(self, nazwa_firmy: str, lista_towarow: list, nazwa: str, pojazdy: list, kierowcy:list):
        super().__init__(nazwa, pojazdy, kierowcy)
        self.__nazwa_firmy = nazwa_firmy
        self.__lista_towarow = lista_towarow

    @property
    def nazwa_firmy(self) -> str:
        return self.__nazwa_firmy

    @nazwa_firmy.setter
    def nazwa_firmy(self, wartosc: str):
        self.__nazwa_firmy = wartosc

    @property
    def lista_towarow(self) -> list:
        return self.__lista_towarow

    @lista_towarow.setter
    def lista_towarow(self, wartosc: list):
        self.__lista_towarow = wartosc


odcinek1 = Odcinek(50.5)
odcinek2 = Odcinek(35.89)
odcinek3 = Odcinek(40.14)
odcinek4 = Odcinek(60.9)
odcinek5 = Odcinek(90.9)

pojazd1 = Pojazd("Reno", 3000, "biały", 2)
pojazd2 = Pojazd("Toyota", 2750, "niebieski", 4)
pojazd3 = Pojazd("Citroen", 400, "czarny", 6)
firmaT = FirmaTransportowa("PolTrans", [pojazd1, pojazd2, pojazd3],
                           ["Bogumił Placek", "Andrzej Kowalski", "Jan Nowak", "Beata Machalska"])

kurs = Kurs([odcinek1, odcinek2, odcinek3, odcinek4, odcinek5], "Amsterdam", firmaT.kierowcy[0], firmaT, pojazd2)

print(kurs)
