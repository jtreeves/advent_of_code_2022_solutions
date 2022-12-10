def determine_no_characters_repeat(characters):
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

print(determine_no_characters_repeat("abcb"))