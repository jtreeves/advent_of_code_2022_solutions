class Cell:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
        self.value = self.convert_letter_to_number()
    
    def __repr__(self):
        return f"({self.x}, {self.y}): {self.letter}"

    def convert_letter_to_number(self):
        if self.letter == "S":
            return 1
        elif self.letter == "E":
            return 26
        else:
            return ord(self.letter) - 96

class Grid:
    def __init__(self, description):
        self.description = description.split("\n")
        self.height = self.calculate_height()
        self.width = self.calculate_width()
        self.cells = self.create_cells()
    
    def calculate_height(self):
        return len(self.description)
    
    def calculate_width(self):
        return len(self.description[0])
    
    def create_cells(self):
        cells = []
        for row in range(self.height):
            for column in range(self.width):
                letter = self.description[row][column]
                new_cell = Cell(column, row, letter)
                cells.append(new_cell)
        return cells

def solve_problem():
    data = extract_data_from_file(12, False)
    grid = Grid(data)
    return grid.cells

def extract_data_from_file(day_number, is_official):
    if is_official:
        name = "data"
    else:
        name = "practice"
    file = open(f"day{day_number}/{name}.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
