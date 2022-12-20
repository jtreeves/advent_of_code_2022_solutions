def solve_problem():
    data = extract_data_from_file(20)
    numbers = list_all_numbers(data)
    move_element(1, 0, 0, numbers)
    move_element(2, 0, 1, numbers)
    move_element(-3, 1, 2, numbers)
    # index = find_index_of_zero(numbers)
    # mixed_list = [1, 2, -3, 4, 0, 3, -2]
    # total = sum_key_values(mixed_list)
    # unique = check_unique(numbers)
    # print(f"ORIGINAL NUMBERS: {numbers}")
    return numbers

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

def move_element(value, current_index, original_index, list):
    new_index = value + current_index
    updated_details = {
        "original_index": original_index,
        "value": value
    }
    del list[current_index]
    list.insert(new_index, updated_details)
    return list

def find_current_index_of_value_based_on_original_index(original_index, list):
    for i in range(len(list)):
        if list[i]["original_index"] == original_index:
            return i

def list_all_numbers(data):
    string_numbers = data.split("\n")
    numbers_data = []
    for i in range(len(string_numbers)):
        integer = int(string_numbers[i])
        details = {
            "original_index": i,
            "value": integer
        }
        numbers_data.append(details)
    return numbers_data

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
