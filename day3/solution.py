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

# print(convert_letter_to_priority("A"))
# print(split_items_in_half("uxjeYYednJ"))
# print(find_common_character_across_halves(["auiop", "qwear"]))
# print(get_priority_of_sack("vJrwpWtwJgWrhcsFMMfFFhFp"))
print(calculate_total_across_all_sacks(["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]))