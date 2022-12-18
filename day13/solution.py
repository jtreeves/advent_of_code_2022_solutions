import json

def solve_problem():
    data = extract_data_from_file(13)
    pairs = list_all_formatted_packet_pairs(data)
    packets = list_all_packets_together_with_divider_packets(pairs)
    total = sum_all_indices_of_pairs_in_correct_order(pairs)
    return {
        "part1": total,
        "part2": packets
    }

def sum_all_indices_of_pairs_in_correct_order(pairs):
    indices = list_all_indices_of_pairs_in_correct_order(pairs)
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

def list_all_packets_together_with_divider_packets(pairs):
    all_packets = []
    for pair in pairs:
        all_packets.append(pair["left"])
        all_packets.append(pair["right"])
    first_divider_packet = [[2]]
    second_divider_packet = [[6]]
    all_packets.append(first_divider_packet)
    all_packets.append(second_divider_packet)
    return all_packets

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
