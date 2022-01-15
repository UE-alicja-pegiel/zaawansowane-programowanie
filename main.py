import magazyn.Dieta
import magazyn.Zamowienie
import osoby.Pacjent
import osoby.Dietetyk

dieta1 = magazyn.Dieta.Dieta("15.01.2022", "22.01.2022", "węglowodany", 2700, 500.99)
dieta2 = magazyn.Dieta.Dieta("22.01.2022", "29.01.2022", "niskotłuszczowa", 3000, 550)

pacjent = osoby.Pacjent.Pacjent("Anna", "Nowak", 89.47, "utrata wagi")
dietetyk = osoby.Dietetyk.Dietetyk("Adam", "Kowalski", "dr", 1500)

zamowienie = magazyn.Zamowienie.Zamowienie(pacjent, dietetyk, [dieta1, dieta2], 12345)
print(zamowienie)
