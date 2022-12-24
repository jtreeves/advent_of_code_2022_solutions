class CoordinatePair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.proposed_x = None
        self.proposed_y = None
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def check_if_equal(self, other_point):
        if self.x == other_point.x and self.y == other_point.y:
            return True
        else:
            return False

    def propose_new_location(self, new_x, new_y):
        self.proposed_x = new_x
        self.proposed_y = new_y

    def move_to_new_location(self):
        self.x = self.proposed_x
        self.y = self.proposed_y

class Grid:
    def __init__(self, description):
        self.lines = description.split("\n")
        self.original_height = len(self.lines)
        self.original_width = len(self.lines[0])
        self.pairs = self.create_pairs()
    
    def create_pairs(self):
        pairs = []
        for row in range(self.original_height):
            for column in range(self.original_width):
                if self.lines[row][column] == "#":
                    new_pair = CoordinatePair(column, row)
                    pairs.append(new_pair)
        return pairs

def solve_problem():
    data = extract_data_from_file(23, False)
    grid = Grid(data)
    return grid.pairs

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
