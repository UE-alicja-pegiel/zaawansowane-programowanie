class Pacjent:
    def __init__(self, imie: str, nazwisko: str, waga: float, plan: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._waga = waga
        self._plan = plan

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def nazwisko(self) -> str:
        return self._nazwisko

    @property
    def waga(self) -> float:
        return self._waga

    @property
    def plan(self) -> str:
        return self._plan

    def __str__(self):
        return f"Pacjent {self.imie} {self.nazwisko}.\nWaga: {self.waga}.\nPlan: {self.plan}"
