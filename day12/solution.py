class Cell:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

class Grid:
    def __init__(self, description):
        self.description = description.split("\n")
        self.height = self.calculate_height()
        self.width = self.calculate_width()
    
    def calculate_height(self):
        return len(self.description)
    
    def calculate_width(self):
        return len(self.description[0])

def convert_letter_to_number(letter):
    if letter == "S":
        return 1
    elif letter == "E":
        return 26
    else:
        return ord(letter) - 96

print(convert_letter_to_number('a'))
print(convert_letter_to_number('u'))