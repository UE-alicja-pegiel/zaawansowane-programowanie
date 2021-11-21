

def is_length(register: list, number: int) -> bool:
    if len(register) != number:
        return False
    return True


reg = [1, 2, 3, 4, 5]

if is_length(reg, 5):
    print(f"The number is the same length to {len(reg)}.")
else:
    print(f"The number is different length to {len(reg)}.")
