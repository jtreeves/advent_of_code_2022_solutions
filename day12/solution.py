class Cell:
    def __init__(self, x, y, letter, name, neighbors):
        self.x = x
        self.y = y
        self.letter = letter
        self.name = name
        self.neighbors = neighbors
        self.visited = False
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

    def mark_as_visited(self):
        self.visited = True

    def mark_as_unvisited(self):
        self.visited = False

    def filter_out_neighbors(self, grid):
        filtered = []
        for neighbor in self.neighbors:
            new_position = grid.find_cell_by_name(neighbor)
            new_position_value = new_position.value
            current_position_value = self.value
            distance = new_position_value - current_position_value
            if distance <= 1 and not new_position.visited:
                filtered.append(neighbor)
        self.neighbors = filtered

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
    
    def find_cell_names_by_value(self, value):
        selected_cells = []
        for cell in self.cells.values():
            if cell.value == value:
                selected_cells.append(cell.name)
        return selected_cells

    def mark_all_cells_unvisited(self):
        for cell in self.cells.values():
            cell.mark_as_unvisited()

    def repopulate_original_neighbors_for_all_cells(self):
        for cell in self.cells.values():
            neighbors = self.determine_neighbors(cell.x, cell.y)
            cell.neighbors = neighbors

class Traveler:
    def __init__(self, grid):
        self.grid = grid
        self.starting_position = self.grid.find_starting_position()
        self.ending_position = self.grid.find_ending_position()
    
    def __repr__(self):
        return f"{self.current_position}"

    def find_shortest_path(self, starting_position):
        minimum_distance = float('inf')
        queue = [(starting_position, 0)]
        starting_position.mark_as_visited()
        while queue:
            (position, distance) = queue.pop(0)
            if position == self.ending_position:
                minimum_distance = distance
                break
            else:
                position.filter_out_neighbors(self.grid)
                for neighbor in position.neighbors:
                    new_position = self.grid.find_cell_by_name(neighbor)
                    new_position.mark_as_visited()
                    queue.append((new_position, distance + 1))
        return minimum_distance

    def find_shortest_path_from_marked_start(self):
        result = self.find_shortest_path(self.starting_position, self.ending_position)
        return result

    def find_shortest_path_from_any_minimal_elevation(self):
        cell_names = self.grid.find_cell_names_by_value(1)
        distances = []
        for name in cell_names:
            self.grid.mark_all_cells_unvisited()
            self.grid.repopulate_original_neighbors_for_all_cells()
            current_position = self.grid.find_cell_by_name(name)
            distance = self.find_shortest_path(current_position)
            distances.append(distance)
        distances.sort()
        print(distances)
        return distances[0]

def solve_problem():
    data = extract_data_from_file(12, False)
    grid = Grid(data)
    traveler = Traveler(grid)
    result = traveler.find_shortest_path_from_any_minimal_elevation()
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
