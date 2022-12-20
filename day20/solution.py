# print(1004 % 7)
# print(2004 % 7)
# print(3004 % 7)

def solve_problem():
    data = extract_data_from_file(20)
    numbers = list_all_numbers(data)
    index = find_index_of_zero(numbers)
    mixed_list = [1, 2, -3, 4, 0, 3, -2]
    total = sum_key_values(mixed_list)
    return total

def sum_key_values(mixed_list):
    key_values = determine_values_at_key_indices_after_zero(mixed_list)
    total = 0
    for value in key_values:
        total += value
    return total

def determine_values_at_key_indices_after_zero(mixed_list):
    length = len(mixed_list)
    index = find_index_of_zero(mixed_list)
    first_index = index + 1000
    second_index = first_index + 1000
    third_index = second_index + 1000
    first_modulo = first_index % length
    second_modulo = second_index % length
    third_modulo = third_index % length
    first_value = mixed_list[first_modulo]
    second_value = mixed_list[second_modulo]
    third_value = mixed_list[third_modulo]
    return [
        first_value,
        second_value,
        third_value
    ]

def find_index_of_zero(mixed_list):
    index = mixed_list.index(0)
    return index

def copy_original_list(original_list):
    copy = []
    for element in original_list:
        copy.append(element)
    return copy

def list_all_numbers(data):
    string_numbers = data.split("\n")
    integer_numbers = []
    for string in string_numbers:
        integer = int(string)
        integer_numbers.append(integer)
    return integer_numbers

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
