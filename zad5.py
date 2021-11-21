

def is_in(register: list, number: int) -> bool:
    if number in register:
        return True
    return False


reg = [1, 2, 3, 4, 5]
num = 5

if is_in(reg, num):
    print(f"Number {num} is in list {reg}.")
else:
    print(f"Number {num} is not in list {reg}.")
