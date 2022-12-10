def solve_problem():
    data = extract_data_from_file(6)
    packet_marker = find_first_packet_marker_after_uniques(data)
    message_marker = find_first_message_marker_after_uniques(data)
    return {
        "packet": packet_marker,
        "message": message_marker
    }

def find_first_message_marker_after_uniques(characters):
    marker = 14
    first_fourteen_characters = extract_first_fourteen_characters(characters)
    checked_characters = check_no_characters_repeat(first_fourteen_characters)
    while not checked_characters:
        marker += 1
        characters = characters[1:]
        first_fourteen_characters = extract_first_fourteen_characters(characters)
        checked_characters = check_no_characters_repeat(first_fourteen_characters)
    return marker

def find_first_packet_marker_after_uniques(characters):
    marker = 4
    first_four_characters = extract_first_four_characters(characters)
    checked_characters = check_no_characters_repeat(first_four_characters)
    while not checked_characters:
        marker += 1
        characters = characters[1:]
        first_four_characters = extract_first_four_characters(characters)
        checked_characters = check_no_characters_repeat(first_four_characters)
    return marker

def extract_first_fourteen_characters(characters):
    return characters[0:14]

def extract_first_four_characters(characters):
    return characters[0:4]

def check_no_characters_repeat(characters):
    for character in characters:
        character_count = characters.count(character)
        if character_count != 1:
            return False
    return True

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

# result = solve_problem()
# print(result)

print(find_first_message_marker_after_uniques("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
print(find_first_message_marker_after_uniques("bvwbjplbgvbhsrlpgdmjqwftvncz"))
print(find_first_message_marker_after_uniques("nppdvjthqldpwncqszvftbrmjlhg"))
print(find_first_message_marker_after_uniques("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
print(find_first_message_marker_after_uniques("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))