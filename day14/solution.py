class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Point):
            if self.x < other.x:
                return True
            elif self.x == other.x and self.y < other.y:
                return True
            else:
                return False
        else:
            return False
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def has_identical_x(self, other_point):
        return self.x == other_point.x
    
    def has_identical_y(self, other_point):
        return self.y == other_point.y

class Sand:
    def __init__(self):
        self.location = Point(500, 0)
    
    def __repr__(self):
        return f"{self.location}"

class Path:
    def __init__(self, description):
        self.descriptions = description.split(" -> ")
        self.anchor_points = self.create_anchor_points()
        self.all_points = self.create_all_points()

    def __repr__(self):
        return f"{self.all_points}: {len(self.all_points)}"

    def create_anchor_points(self):
        points = []
        for description in self.descriptions:
            coordinates = description.split(",")
            new_point = Point(int(coordinates[0]), int(coordinates[1]))
            points.append(new_point)
        return points

    def create_all_points(self):
        points = set()
        for i in range(len(self.anchor_points) - 1):
            left_endpoint = self.anchor_points[i]
            right_endpoint = self.anchor_points[i + 1]
            matching_x = left_endpoint.has_identical_x(right_endpoint)
            matching_y = left_endpoint.has_identical_y(right_endpoint)
            points.add(left_endpoint)
            points.add(right_endpoint)
            if matching_x:
                for y in range(left_endpoint.y, right_endpoint.y):
                    new_point = Point(left_endpoint.x, y)
                    points.add(new_point)
            elif matching_y:
                for x in range(right_endpoint.x, left_endpoint.x):
                    new_point = Point(x, left_endpoint.y)
                    points.add(new_point)
        return sorted(points)

class Cave:
    def __init__(self, description):
        self.descriptions = description.split("\n")
        self.paths = self.create_paths()
        self.occupied_points = self.determine_occupied_points()
    
    def __repr__(self):
        return f"{self.occupied_points}: {len(self.occupied_points)}"

    def create_paths(self):
        paths = []
        for description in self.descriptions:
            new_path = Path(description)
            paths.append(new_path)
        return paths
    
    def determine_occupied_points(self):
        points = []
        for path in self.paths:
            for point in path.all_points:
                points.append(point)
        return sorted(points)

def solve_problem():
    data = extract_data_from_file(14, False)
    cave = Cave(data)
    return cave

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
