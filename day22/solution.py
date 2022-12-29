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
    def __init__(self, description):
        self.description = description.split("\n")
        self.height = len(self.description)
        self.width = len(self.description[0])
        self.cells = self.create_cells()
    
    def __repr__(self):
        return f"{self.cells}"

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

class Step:
    def __init__(self, characters):
        self.characters = characters

    def __repr__(self):
        return f"{self.characters}"

class Instructions:
    def __init__(self, notes):
        self.notes = notes
        self.steps = self.create_steps()

    def __repr__(self):
        return f"{self.steps}"
    
    def create_steps(self):
        steps = []
        characters = self.notes
        while characters:
            current_character = characters[0]
            characters = characters[1:]
            if current_character == "R" or current_character == "L":
                new_step = Step(current_character)
            else:
                digits = current_character
                while characters and characters[0] != "R" and characters[0] != "L":
                    digits += characters[0]
                    characters = characters[1:]
                new_step = Step(digits)
            steps.append(new_step)
        return steps

def solve_problem():
    data = extract_data_from_file(22, False)
    partitioned = data.split("\n\n")
    board = Board(partitioned[0])
    instructions = Instructions(partitioned[1])
    return instructions

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
