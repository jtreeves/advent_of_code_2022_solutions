import json

def calculate_difference_between_packets(left_packet, right_packet):
    left = left_packet if isinstance(left_packet, list) else [left_packet]
    right = right_packet if isinstance(right_packet, list) else [right_packet]
    for l, r in zip(left, right):
        if isinstance(l, list) or isinstance(r, list):
            difference = calculate_difference_between_packets(l, r)
        else:
            difference = r - l
        if difference != 0:
            return difference
    return len(right) - len(left)

def solve_problem():
    data = extract_data_from_file(13)
    pairs = list_all_formatted_packet_pairs(data)
    total = sum_all_indices_of_pairs_in_correct_order(pairs)
    return total

def sum_all_indices_of_pairs_in_correct_order(pairs):
    indices = list_all_indices_of_pairs_in_correct_order(pairs)
    print(indices)
    total = 0
    for index in indices:
        total += index
    return total

def list_all_indices_of_pairs_in_correct_order(pairs):
    indices = []
    for pair in pairs:
        difference = calculate_difference_between_packets(pair["left"], pair["right"])
        if difference > 0:
            indices.append(pair["index"])
    return indices

def check_if_elements_in_correct_order(left, right):
    left_is_int = isinstance(left, int)
    right_is_int = isinstance(right, int)
    if left_is_int and right_is_int:
        return check_if_integers_in_correct_order(left, right)
    elif not left_is_int and not right_is_int:
        return check_if_lists_in_correct_order(left, right)
    elif left_is_int and not right_is_int:
        if len(right) == 0:
            return False
        else:
            return check_if_elements_in_correct_order(left, right[0])
    elif not left_is_int and right_is_int:
        if len(left) == 0:
            return True
        else:
            return check_if_elements_in_correct_order(left[0], right)

def check_if_integers_in_correct_order(left, right):
    if right < left:
        return False
    else:
        return True

def check_if_lists_in_correct_order(left, right):
    if len(right) < len(left):
        return False
    else:
        for i in range(len(left)):
            correct_elements = check_if_elements_in_correct_order(left[i], right[i])
            if not correct_elements:
                return False
        return True

def list_all_formatted_packet_pairs(data):
    raw_pairs = list_all_raw_pairs(data)
    all_pairs = []
    for i in range(len(raw_pairs)):
        formatted_pair = create_formatted_packet_pair(raw_pairs[i], i + 1)
        all_pairs.append(formatted_pair)
    return all_pairs

def create_formatted_packet_pair(original_pair, index):
    raw_packets = separate_raw_packets(original_pair)
    left = convert_string_to_list(raw_packets[0])
    right = convert_string_to_list(raw_packets[1])
    formatted_pair = {
        "left": left,
        "right": right,
        "index": index
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

# RECEIVED HELP FROM THIS ANSWER: https://www.reddit.com/r/adventofcode/comments/zkmyh4/comment/j0cgmkb/?utm_source=reddit&utm_medium=web2x&context=3
