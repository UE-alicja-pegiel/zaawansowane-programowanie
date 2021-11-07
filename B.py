
def multi_for(numbers: list):
    for idx, number in enumerate(numbers):
        numbers[idx] = number*2
    return numbers


def multi_list_comprehension(numbers : list):
    return [number * 2 for number in numbers]


print("Test for list with for loop:", multi_for([-4, -3, -2, -1, 0, 2, 3, 4]))
print("Test for list with list comprehension:", multi_list_comprehension([-4, -3, -2, -1, 0, 2, 3, 4]))
