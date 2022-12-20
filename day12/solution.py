def convert_letter_to_number(letter):
    if letter == "S":
        return 1
    elif letter == "E":
        return 26
    else:
        return ord(letter) - 96

print(convert_letter_to_number('a'))
print(convert_letter_to_number('u'))