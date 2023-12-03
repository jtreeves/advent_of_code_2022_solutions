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
    first_value = mixed_list[first_modulo]["value"]
    second_value = mixed_list[second_modulo]["value"]
    third_value = mixed_list[third_modulo]["value"]
    return [
        first_value,
        second_value,
        third_value
    ]


def find_index_of_zero(mixed_list):
    for i in range(len(mixed_list)):
        if mixed_list[i]["value"] == 0:
            return i


def mix_list(list):
    for i in range(len(list)):
        value = find_value_based_on_original_index(i, list)
        current_index = find_current_index_of_value_based_on_original_index(
            i, list)
        list = move_element(value, current_index, i, list)
    return list


def move_element(value, current_index, original_index, list):
    length = len(list)
    new_index = value + current_index
    abs_index = abs(new_index)
    if abs_index >= length:
        if new_index > 0:
            new_index %= length
            new_index += 1
        else:
            new_index %= (-1 * length)
            new_index -= 1
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


def find_value_based_on_original_index(original_index, list):
    for i in range(len(list)):
        if list[i]["original_index"] == original_index:
            return list[i]["value"]


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


def solve_problem():
    data = extract_data_from_file(20, True)
    numbers = list_all_numbers(data)
    numbers = mix_list(numbers)
    summed = sum_key_values(numbers)
    return summed


def extract_data_from_file(day_number, is_official):
    if is_official:
        name = "data"
    else:
        name = "practice"
    file = open(f"day{day_number}/{name}.txt", "r")
    data = file.read()
    file.close()
    return data


result = solve_problem()
print(result)
