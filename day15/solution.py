class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def calculate_distance(self, other_point):
        horizontal = abs(self.x - other_point.x)
        vertical = abs(self.y - other_point.y)
        distance = horizontal + vertical
        return distance

class Sensor(Point):
    pass

class Beacon(Point):
    pass

class Grid:
    def __init__(self, description):
        self.descriptions = description.split("\n")

def solve_problem():
    data = extract_data_from_file(15, False)
    grid = Grid(data)
    return grid

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
