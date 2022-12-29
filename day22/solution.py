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
        self.starting_position = self.determine_starting_position()
    
    def __repr__(self):
        return f"{self.starting_position.name} >>> {self.cells}"

    def create_cells(self):
        cells = {}
        for row in range(self.height):
            for column in range(self.width):
                character = self.description[row][column]
                if character != " ":
                    x = column + 1
                    y = row + 1
                    name = f"x{x}y{y}"
                    new_cell = Cell(x, y, character, name)
                    cells[name] = new_cell
        return cells
    
    def determine_starting_position(self):
        open_tops = []
        for cell in self.cells.values():
            if "y1" in cell.name and cell.name.split("y1")[1] == "" and cell.open:
                open_tops.append(cell.x)
        open_tops.sort()
        first_x = open_tops[0]
        starting_name = f"x{first_x}y1"
        starting_cell = self.find_cell_by_name(starting_name)
        return starting_cell
    
    def find_cell_by_name(self, name):
        cell = self.cells[name]
        return cell

class Step:
    def __init__(self, characters):
        self.characters = characters
        self.distance = self.determine_distance()
        self.direction = self.determine_direction()

    def __repr__(self):
        return f"{self.distance} -> {self.direction}"

    def determine_distance(self):
        if self.characters == "R" or self.characters == "L":
            return 0
        else:
            return int(self.characters)
    
    def determine_direction(self):
        if self.characters == "R":
            return 1
        elif self.characters == "L":
            return -1
        else:
            return 0

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

class Traveler:
    def __init__(self, board, instructions):
        self.board = board
        self.instructions = instructions
        self.current_position = board.starting_position
        self.facing = 0
        self.step_index = 0

    def __repr__(self):
        return f"{self.current_position} >>> {self.facing}"
    
    def update_facing(self, direction):
        new_direction = self.facing + direction
        if new_direction == 4:
            new_direction = 0
        elif new_direction == -1:
            new_direction = 3
        self.facing = new_direction
    
    def update_position(self, distance):
        pass

    def execute_next_step(self):
        next_step = self.instructions[self.step_index]
        self.update_facing(next_step.direction)
        self.update_position(next_step.distance)
        self.step_index += 1
    
    def determine_password(self):
        row = self.current_position.y
        column = self.current_position.x
        facing = self.facing
        password = 1000 * row + 4 * column + facing
        return password

def solve_problem():
    data = extract_data_from_file(22, False)
    partitioned = data.split("\n\n")
    board = Board(partitioned[0])
    instructions = Instructions(partitioned[1])
    traveler = Traveler(board, instructions)
    password = traveler.determine_password()
    return password

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
