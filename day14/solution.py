class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def has_identical_x(self, other_point):
        return self.x == other_point.x
    
    def has_identical_y(self, other_point):
        return self.y == other_point.y

class Sand:
    def __init__(self):
        self.location = Point(500, 0)

class Path:
    def __init__(self, description):
        self.anchor_points = description.split(" -> ")

    def create_all_points(self):
        pass

class Cave:
    def __init__(self, description):
        self.descriptions = description.split("\n")
        self.paths = self.create_paths()
    
    def create_paths(self):
        paths = []
        for description in self.descriptions:
            new_path = Path(description)
            paths.append(new_path)
        return paths

def solve_problem():
    data = extract_data_from_file(14, False)
    return data

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
