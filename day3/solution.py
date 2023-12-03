def solve_problem():
    data = extract_data_from_file(3)
    sacks = convert_multiline_string_to_array(data)
    groups = partition_array_by_threes(sacks)
    total = calculate_total_across_all_groups(groups)
    return total


def calculate_total_across_all_groups(groups):
    total = 0
    for group in groups:
        priority = get_priority_of_group(group)
        total += priority
    return total


def calculate_total_across_all_sacks(sacks):
    total = 0
    for sack in sacks:
        priority = get_priority_of_sack(sack)
        total += priority
    return total


def get_priority_of_sack(sack):
    halves = split_items_in_half(sack)
    common_character = find_common_character_across_halves(halves)
    priority = convert_letter_to_priority(common_character)
    return priority


def get_priority_of_group(group):
    common_character = find_common_character_across_threes(group)
    priority = convert_letter_to_priority(common_character)
    return priority


def find_common_character_across_threes(threes):
    first_sack = set(threes[0])
    second_sack = set(threes[1])
    third_sack = set(threes[2])
    overlap = list(first_sack.intersection(second_sack).intersection(third_sack))
    common_character = overlap[0]
    return common_character


def find_common_character_across_halves(halves):
    first_half = set(halves[0])
    second_half = set(halves[1])
    overlap = list(first_half.intersection(second_half))
    common_character = overlap[0]
    return common_character


def split_items_in_half(items):
    length = len(items)
    half = int(length / 2)
    first_half = items[0:half]
    second_half = items[half:]
    return [first_half, second_half]


def convert_letter_to_priority(letter):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = letters.index(letter)
    priority = index + 1
    return priority


def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data


def partition_array_by_threes(original_array):
    new_array = []
    while len(original_array):
        sub_array = []
        sub_array.append(original_array[0])
        sub_array.append(original_array[1])
        sub_array.append(original_array[2])
        new_array.append(sub_array)
        original_array = original_array[3:]
    return new_array


def convert_multiline_string_to_array(multiline_string):
    rows = []
    while len(multiline_string):
        first_line_break = multiline_string.find("\n")
        if first_line_break != -1:
            content_before = multiline_string[0:first_line_break]
            rows.append(content_before)
            multiline_string = multiline_string[first_line_break + 1:]
        else:
            rows.append(multiline_string)
            multiline_string = ""
    return rows


result = solve_problem()
print(result)
