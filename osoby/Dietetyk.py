class Dietetyk:
    def __init__(self, imie: str, nazwisko: str, tytul: str, koszt: float):
        self._imie = imie
        self._nazwisko = nazwisko
        self._tytul = tytul
        self._koszt = koszt

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def tytul(self) -> str:
        return self._tytul

    @property
    def koszt(self) -> float:
        return self._koszt

    def __str__(self):
        return f"{self.tytul} {self.imie} {self.nazwisko}: {self.koszt} zł."
