
def sum_is_larger(num1: int, num2: int, num3: int) -> bool:
    if num1 + num2 >= num3:
        return True
    return False


number1 = 3
number2 = 3
number3 = 6

if sum_is_larger(number1, number2, number3):
    print(f"{number1} plus {number2} is {number1+number2}, which is more or equal to {number3}.")
else:
    print(f"{number1} plus {number2} is {number1+number2}, which is less than {number3}.")
