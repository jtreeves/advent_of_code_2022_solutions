import json

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