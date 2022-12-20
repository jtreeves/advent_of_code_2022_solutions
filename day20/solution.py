# print(1004 % 7)
# print(2004 % 7)
# print(3004 % 7)

def solve_problem():
    data = extract_data_from_file(20)
    numbers = list_all_numbers(data)
    index = find_index_of_zero(numbers)
    return index

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
