class Cell:
    def __init__(self, x, y, letter, name, neighbors):
        self.x = x
        self.y = y
        self.letter = letter
        self.name = name
        self.neighbors = neighbors
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
        cells = {}
        for row in range(self.height):
            for column in range(self.width):
                letter = self.description[row][column]
                name = f"x{column}y{row}"
                neighbors = self.determine_neighbors(column, row)
                new_cell = Cell(column, row, letter, name, neighbors)
                cells[name] = new_cell
        return cells

    def determine_neighbors(self, x, y):
        neighbors = []
        x_left = x - 1
        x_right = x + 1
        y_up = y - 1
        y_down = y + 1
        if x_left >= 0:
            left_name = f"x{x_left}y{y}"
            neighbors.append(left_name)
        if y_up >= 0:
            up_name = f"x{x}y{y_up}"
            neighbors.append(up_name)
        if x_right < self.width:
            right_name = f"x{x_right}y{y}"
            neighbors.append(right_name)
        if y_down < self.height:
            down_name = f"x{x}y{y_down}"
            neighbors.append(down_name)
        return neighbors

    def find_starting_position(self):
        for cell in self.cells.values():
            if cell.letter == "S":
                return cell

    def find_ending_position(self):
        for cell in self.cells.values():
            if cell.letter == "E":
                return cell

    def find_cell_by_name(self, name):
        for cell in self.cells.values():
            if cell.name == name:
                return cell

class Traveler:
    def __init__(self, grid):
        self.grid = grid
        self.starting_position = self.grid.find_starting_position()
        self.ending_position = self.grid.find_ending_position()
        self.current_position = self.starting_position
    
    def __repr__(self):
        return f"{self.current_position}"

    def find_shortest_path(self):
        total = 0
        path = Path(self.grid, [], self.starting_position)
        neighbors = path.neighbors
        while len(neighbors) != 0 and self.current_position is not self.ending_position:
            print(self)
            for neighbor in neighbors:
                new_position = self.grid.find_cell_by_name(neighbor)
                self.current_position = new_position
                path = Path(self.grid, path.previous_positions.append(self.current_position.name), new_position)
                neighbors = path.neighbors
                total += 1
        return total

class Path:
    def __init__(self, grid, previous_positions, current_position):
        self.grid = grid
        self.previous_positions = previous_positions
        self.current_position = current_position
        self.neighbors = self.current_position.neighbors
        self.filter_out_bad_neighbors()
    
    def filter_out_previously_visited_neighbors(self):
        filtered = []
        for neighbor in self.neighbors:
            if neighbor not in self.previous_positions:
                filtered.append(neighbor)
        self.neighbors = filtered
    
    def filter_out_neighbors_exceding_climb_limit(self):
        filtered = []
        for neighbor in self.neighbors:
            new_position = self.grid.find_cell_by_name(neighbor)
            new_position_value = new_position.value
            current_position_value = self.current_position.value
            distance = new_position_value - current_position_value
            if distance <= 1:
                filtered.append(neighbor)
        self.neighbors = filtered

    def filter_out_bad_neighbors(self):
        self.filter_out_previously_visited_neighbors()
        self.filter_out_neighbors_exceding_climb_limit()

def solve_problem():
    data = extract_data_from_file(12, False)
    grid = Grid(data)
    traveler = Traveler(grid)
    result = traveler.find_shortest_path()
    return result

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
