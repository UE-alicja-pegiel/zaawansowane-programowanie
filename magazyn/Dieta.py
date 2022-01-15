class Dieta:
    def __init__(self, data_rozpoczecia: str, data_zakonczenia: str, typ: str, kalorie: int, cena: float):
        self._data_rozpoczecia = data_rozpoczecia
        self._data_zakonczenia = data_zakonczenia
        self._typ = typ
        self._kalorie = kalorie
        self._cena = cena

    @property
    def data_rozpoczecia(self) -> str:
        return self._data_rozpoczecia

    @property
    def data_zakonczenia(self) -> str:
        return self._data_zakonczenia

    @property
    def typ(self) -> str:
        return self._typ

    @property
    def kalorie(self) -> int:
        return self._kalorie

    @property
    def cena(self) -> float:
        return self._cena

    def __str__(self):
        return f"Czas trwania diety: {self.data_rozpoczecia}-{self.data_zakonczenia}.\nKalorie: {self.kalorie}." \
               f"\nCena: {self.cena}"
