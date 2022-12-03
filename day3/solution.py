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
print(split_items_in_half("uxjeYYednJ"))
