import json

def solve_problem():
    data = extract_data_from_file(13)
    pairs = list_all_formatted_packet_pairs(data)
    return pairs

def check_if_entire_pair_in_correct_order(left, right):
    return

def check_if_elements_in_correct_order(left, right):
    left_type = type(left)
    right_type = type(right)
    return

def check_if_integers_in_correct_order(left, right):
    if right > left:
        return False
    else:
        return True

def check_if_lists_in_correct_order(left, right):
    if len(right) < len(left):
        return False
    else:
        for i in range(len(left)):
            correct_integers = check_if_integers_in_correct_order(left[i], right[i])
            if not correct_integers:
                return False
        return True

def list_all_formatted_packet_pairs(data):
    raw_pairs = list_all_raw_pairs(data)
    all_pairs = []
    for pair in raw_pairs:
        formatted_pair = create_formatted_packet_pair(pair)
        all_pairs.append(formatted_pair)
    return all_pairs

def create_formatted_packet_pair(original_pair):
    raw_packets = separate_raw_packets(original_pair)
    left = convert_string_to_list(raw_packets[0])
    right = convert_string_to_list(raw_packets[1])
    formatted_pair = {
        "left": left,
        "right": right
    }
    return formatted_pair

def convert_string_to_list(input):
    output = json.loads(input)
    return output

def separate_raw_packets(pair):
    packets = pair.split("\n")
    return packets

def list_all_raw_pairs(data):
    pairs = data.split("\n\n")
    return pairs

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
