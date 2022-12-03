def convert_letter_to_priority(letter):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = letters.index(letter)
    priority = index + 1
    return priority

print(convert_letter_to_priority("A"))
