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
        self.height = self.calculate_height()
        self.width = self.calculate_width()
        self.cells = self.create_cells()
        self.starting_position = self.determine_starting_position()

    def __repr__(self):
        return f"{self.starting_position.name} >>> {self.cells}"

    def calculate_height(self):
        height = len(self.description)
        return height

    def calculate_width(self):
        rows = self.description
        widths = []
        for row in rows:
            width = len(row)
            widths.append(width)
        widths.sort()
        widest = widths[-1]
        return widest

    def create_cells(self):
        cells = {}
        for row in range(self.height):
            for column in range(self.width):
                try:
                    character = self.description[row][column]
                    if character != " ":
                        x = column + 1
                        y = row + 1
                        name = f"x{x}y{y}"
                        new_cell = Cell(x, y, character, name)
                        cells[name] = new_cell
                except IndexError:
                    continue
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
        try:
            cell = self.cells[name]
            return cell
        except KeyError:
            return None

    def find_adjacent_cell(self, current_cell, dimension, direction):
        if dimension == "x":
            adjacent_x = current_cell.x + direction
            adjacent_y = current_cell.y
        else:
            adjacent_x = current_cell.x
            adjacent_y = current_cell.y + direction
        adjacent_name = f"x{adjacent_x}y{adjacent_y}"
        adjacent_cell = self.find_cell_by_name(adjacent_name)
        return adjacent_cell

    def find_opposite_cell(self, current_cell, dimension, direction):
        opposite_cell = None
        if dimension == "x":
            opposite_y = current_cell.y
            if direction == 1:
                opposite_x = 0
                while opposite_cell == None:
                    opposite_x += 1
                    opposite_name = f"x{opposite_x}y{opposite_y}"
                    opposite_cell = self.find_cell_by_name(opposite_name)
            else:
                opposite_x = self.width
                while opposite_cell == None:
                    opposite_x -= 1
                    opposite_name = f"x{opposite_x}y{opposite_y}"
                    opposite_cell = self.find_cell_by_name(opposite_name)
        else:
            opposite_x = current_cell.x
            if direction == 1:
                opposite_y = 0
                while opposite_cell == None:
                    opposite_y += 1
                    opposite_name = f"x{opposite_x}y{opposite_y}"
                    opposite_cell = self.find_cell_by_name(opposite_name)
            else:
                opposite_y = self.height
                while opposite_cell == None:
                    opposite_y -= 1
                    opposite_name = f"x{opposite_x}y{opposite_y}"
                    opposite_cell = self.find_cell_by_name(opposite_name)
        return opposite_cell

    def find_adjacent_cell_right(self, current_cell):
        right_cell = self.find_adjacent_cell(current_cell, "x", 1)
        return right_cell

    def find_adjacent_cell_down(self, current_cell):
        down_cell = self.find_adjacent_cell(current_cell, "y", 1)
        return down_cell

    def find_adjacent_cell_left(self, current_cell):
        left_cell = self.find_adjacent_cell(current_cell, "x", -1)
        return left_cell

    def find_adjacent_cell_up(self, current_cell):
        up_cell = self.find_adjacent_cell(current_cell, "y", -1)
        return up_cell

    def find_opposite_cell_at_beginning_of_row(self, current_cell):
        opposite_cell = self.find_opposite_cell(current_cell, "x", 1)
        return opposite_cell

    def find_opposite_cell_at_top_of_column(self, current_cell):
        opposite_cell = self.find_opposite_cell(current_cell, "y", 1)
        return opposite_cell

    def find_opposite_cell_at_end_of_row(self, current_cell):
        opposite_cell = self.find_opposite_cell(current_cell, "x", -1)
        return opposite_cell

    def find_opposite_cell_at_bottom_of_column(self, current_cell):
        opposite_cell = self.find_opposite_cell(current_cell, "y", -1)
        return opposite_cell


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
        while distance > 0:
            self.move_to_position()
            distance -= 1

    def find_adjacent_cell_in_direction(self):
        match self.facing:
            case 0:
                found_cell = self.board.find_adjacent_cell_right(self.current_position)
            case 1:
                found_cell = self.board.find_adjacent_cell_down(self.current_position)
            case 2:
                found_cell = self.board.find_adjacent_cell_left(self.current_position)
            case 3:
                found_cell = self.board.find_adjacent_cell_up(self.current_position)
        return found_cell

    def find_opposite_cell_in_direction(self):
        match self.facing:
            case 0:
                found_cell = self.board.find_opposite_cell_at_beginning_of_row(self.current_position)
            case 1:
                found_cell = self.board.find_opposite_cell_at_top_of_column(self.current_position)
            case 2:
                found_cell = self.board.find_opposite_cell_at_end_of_row(self.current_position)
            case 3:
                found_cell = self.board.find_opposite_cell_at_bottom_of_column(self.current_position)
        return found_cell

    def move_to_position(self):
        new_cell = self.find_adjacent_cell_in_direction()
        if new_cell is not None and new_cell.open:
            self.current_position = new_cell
        elif new_cell is None:
            new_cell = self.find_opposite_cell_in_direction()
            if new_cell is not None and new_cell.open:
                self.current_position = new_cell

    def execute_next_step(self):
        next_step = self.instructions.steps[self.step_index]
        self.update_facing(next_step.direction)
        self.update_position(next_step.distance)
        self.step_index += 1

    def complete_all_steps(self):
        while self.step_index < len(self.instructions.steps):
            self.execute_next_step()

    def determine_password(self):
        self.complete_all_steps()
        row = self.current_position.y
        column = self.current_position.x
        facing = self.facing
        password = 1000 * row + 4 * column + facing
        return password


def solve_problem():
    data = extract_data_from_file(22, True)
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
