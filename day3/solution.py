def find_common_character_in_halves(halves):
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

# print(convert_letter_to_priority("A"))
# print(split_items_in_half("uxjeYYednJ"))
print(find_common_character_in_halves(["auiop", "qwear"]))