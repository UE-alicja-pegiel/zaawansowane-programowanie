

def is_even(number: int) -> bool:
    if number % 2 != 0:
        return False
    return True


even = is_even(8)

if even:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
    