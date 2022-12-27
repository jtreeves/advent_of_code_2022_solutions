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

class Traveler:
    def __init__(self, grid):
        self.grid = grid
        self.starting_position = self.find_starting_position()
        self.ending_position = self.find_ending_position()
        self.current_position = self.starting_position
        self.total_moves = 0
    
    def __repr__(self):
        return f"{self.current_position} -> {self.total_moves} MOVES"

    def find_starting_position(self):
        for cell in self.grid.cells:
            if cell.letter == "S":
                return cell

    def find_ending_position(self):
        for cell in self.grid.cells:
            if cell.letter == "E":
                return cell

    def find_cell_by_coordinates(self, x, y):
        for cell in self.grid.cells:
            if cell.x == x and cell.y == y:
                return cell
    
    def determine_if_can_move(self, new_x, new_y):
        if new_x >= 0 and new_x < self.grid.width and new_y >= 0 and new_y < self.grid.height:
            new_position = self.find_cell_by_coordinates(new_x, new_y)
            new_position_value = new_position.value
            current_position_value = self.current_position.value
            if new_position_value - current_position_value <= 1:
                return new_position
            else:
                return False
        else:
            return False

    def increment_moves(self):
        self.total_moves += 1

    def move_up(self):
        new_x = self.current_position.x
        new_y = self.current_position.y - 1
        result = self.determine_if_can_move(new_x, new_y)
        if result:
            self.current_position = result
        else:
            return False

    def move_down(self):
        new_x = self.current_position.x
        new_y = self.current_position.y + 1
        result = self.determine_if_can_move(new_x, new_y)
        if result:
            self.current_position = result
        else:
            return False

    def move_left(self):
        new_x = self.current_position.x - 1
        new_y = self.current_position.y
        result = self.determine_if_can_move(new_x, new_y)
        if result:
            self.current_position = result
        else:
            return False

    def move_right(self):
        new_x = self.current_position.x + 1
        new_y = self.current_position.y
        result = self.determine_if_can_move(new_x, new_y)
        if result:
            self.current_position = result
        else:
            return False

    def make_move(self):
        moves = [self.move_down, self.move_right, self.move_left, self.move_up]
        for move in moves:
            result = move()
            if result == False:
                continue
            else:
                self.increment_moves()
                break

def solve_problem():
    data = extract_data_from_file(12, False)
    grid = Grid(data)
    traveler = Traveler(grid)
    print(f"BEFORE MOVE: {traveler}")
    traveler.make_move()
    print(f"AFTER MOVE: {traveler}")
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
