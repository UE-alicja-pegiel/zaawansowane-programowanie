def print_names(name_list: list):
    if len(name_list) != 0:
        for idx, name in enumerate(name_list):
            print(f"Name no.{idx+1}: {name}")
    else:
        print("List of names can't be empty.")


test_name_list1 = []
test_name_list2 = ['Anna', 'Marcin', 'Kacper', 'Magda']

print("Empty list test:")
print_names(test_name_list1)
print("Name list test:")
print_names(test_name_list2)