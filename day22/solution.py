class Cell:
    def __init__(self, x, y, character, name):
        self.x = x
        self.y = y
        self.character = character
        self.name = name
        self.open = self.check_if_open()
    
    def __repr__(self):
        return f"({self.x}, {self.y}) -> {self.open}"
    
    def check_if_open(self):
        if self.character == ".":
            return True
        else:
            return False

class Board:
    def __init__(self, description, instructions):
        self.instructions = instructions
        self.description = description.split("\n")
        self.height = len(self.description)
        self.width = len(self.description[0])
        self.cells = self.create_cells()
    
    def __repr__(self):
        return f"{self.cells} -> {self.instructions}"

    def create_cells(self):
        cells = {}
        for row in range(self.height):
            for column in range(self.width):
                character = self.description[row][column]
                if character != " ":
                    name = f"x{column}y{row}"
                    new_cell = Cell(column, row, character, name)
                    cells[name] = new_cell
        return cells

def solve_problem():
    data = extract_data_from_file(22, False)
    partitioned = data.split("\n\n")
    board = Board(partitioned[0], partitioned[1])
    return board

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
