

def power_of_three(reg1: list, reg2: list) -> list:
    new_reg = list(set(reg1 + reg2))
    for idx, element in enumerate(new_reg):
        new_reg[idx] = element**3
    return new_reg


register1 = [1, 1, 2, 3, 4]
register2 = [4, 5, 5, 6, 7]

print(power_of_three(register1, register2))
