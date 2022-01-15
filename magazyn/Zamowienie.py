from osoby import Dietetyk
from osoby import Pacjent


class Zamowienie:
    def __init__(self, pacjent: Pacjent, prowadzacy: Dietetyk, diety: list, nr_faktury: int):
        self._pacjent = pacjent
        self._prowadzacy = prowadzacy
        self._diety = diety
        self._nr_faktury = nr_faktury

    @property
    def pacjent(self) -> Pacjent:
        return self._pacjent

    @pacjent.setter
    def pacjent(self, value: Pacjent) -> None:
        self._pacjent = value

    @property
    def prowadzacy(self) -> Dietetyk:
        return self._prowadzacy

    @prowadzacy.setter
    def prowadzacy(self, value: Dietetyk):
        self._prowadzacy = value

    @property
    def diety(self) -> list:
        return self._diety

    @diety.setter
    def diety(self, value: list):
        self._diety = value

    @property
    def nr_faktury(self) -> int:
        return self._nr_faktury

    @nr_faktury.setter
    def nr_faktury(self, value: int):
        self._nr_faktury = value

    def wartosc_zamowienia(self):
        koszt = 0
        for dieta in self.diety:
            koszt = koszt + dieta.cena
        return koszt

    def liczba_kalorii(self):
        kalorie = 0
        for kal in self.diety:
            kalorie = kalorie + kal.kalorie
        return kalorie

    def __str__(self):
        return f"Zamówienie numer {self.nr_faktury} dla pacjenta {self.pacjent.imie} {self.pacjent.nazwisko}.\n" \
               f"Dietetyk prowadzący: {self.prowadzacy.imie} {self.prowadzacy.nazwisko}.\n" \
               f"Zawarte diety: {[dieta.typ for dieta in self.diety]}. Koszt zamówienia: {self.wartosc_zamowienia()}." \
               f"\nLiczba kalorii: {self.liczba_kalorii()}."
