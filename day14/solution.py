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
    
    def has_identical_x(self, other):
        return self.x == other.x
    
    def has_identical_y(self, other):
        return self.y == other.y

class Sand:
    def __init__(self):
        self.location = Point(500, 0)
        self.is_falling = True
        self.is_in_cave = True
    
    def __repr__(self):
        return f"{self.location}"
    
    def fall_until_stopped(self, other_points):
        while self.is_falling:
            self.fall_down_one_unit(other_points)
    
    def fall_until_stopped_or_out_of_cave(self, other_points, min_x, min_y, max_x, max_y):
        while self.is_falling and self.is_in_cave:
            self.fall_down_one_unit(other_points)
            self.check_if_still_in_cave(min_x, min_y, max_x, max_y)
    
    def fall_down_one_unit(self, other_points):
        new_x = self.location.x
        new_y = self.location.y + 1
        one_down = f"x{new_x}y{new_y}"
        try:
            other_points[one_down]
            new_x -= 1
            one_left = f"x{new_x}y{new_y}"
            try:
                other_points[one_left]
                new_x += 2
                one_right = f"x{new_x}y{new_y}"
                try:
                    other_points[one_right]
                    self.is_falling = False
                except KeyError:
                    self.location = Point(new_x, new_y)
            except KeyError:
                self.location = Point(new_x, new_y)
        except KeyError:
            self.location = Point(new_x, new_y)
    
    def check_if_still_in_cave(self, min_x, min_y, max_x, max_y):
        x = self.location.x
        y = self.location.y
        if x < min_x or x > max_x or y < min_y or y > max_y:
            self.is_in_cave = False

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
                left_y = left_endpoint.y
                right_y = right_endpoint.y
                first_y = left_y if left_y < right_y else right_y
                second_y = right_y if first_y == left_y else left_y
                for y in range(first_y, second_y):
                    new_point = Point(left_endpoint.x, y)
                    points.add(new_point)
            elif matching_y:
                left_x = left_endpoint.x
                right_x = right_endpoint.x
                first_x = left_x if left_x < right_x else right_x
                second_x = right_x if first_x == left_x else left_x
                for x in range(first_x, second_x):
                    new_point = Point(x, left_endpoint.y)
                    points.add(new_point)
        return sorted(points)

class Cave:
    def __init__(self, description):
        self.descriptions = description.split("\n")
        self.paths = self.create_paths()
        self.rock_points = self.determine_rock_points()
        self.occupied_points = self.create_occupied_points()
        self.sand_points = []
        self.min_x = self.rock_points[0].x
        self.max_x = self.rock_points[-1].x
        self.min_y = 0
        self.max_y = self.find_max_y()
        self.floor = self.create_floor()
    
    def __repr__(self):
        diagram = ""
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if Point(x, y) in self.rock_points:
                    diagram += "#"
                else:
                    diagram += "."
            diagram += "\n"
        return diagram
    
    def calculate_total_sand_units_fallen_until_out_of_cave(self):
        units = len(self.sand_points) - 1
        return units
    
    def calculate_total_sand_units_fallen_until_reach_top(self):
        units = len(self.sand_points)
        return units
    
    def add_sand_until_first_out_of_cave(self):
        while len(self.sand_points) == 0 or self.sand_points[-1].is_in_cave:
            new_sand = Sand()
            new_sand.fall_until_stopped_or_out_of_cave(self.occupied_points, self.min_x, self.min_y, self.max_x, self.max_y)
            self.append_sand_to_both_points_trackers(new_sand)
    
    def add_sand_until_first_hits_top(self):
        while len(self.sand_points) == 0 or self.sand_points[-1].location != Point(500, 0):
            new_sand = Sand()
            new_sand.fall_until_stopped(self.occupied_points)
            self.append_sand_to_both_points_trackers(new_sand)
    
    def append_sand_to_both_points_trackers(self, sand):
        name = f"x{sand.location.x}y{sand.location.y}"
        self.occupied_points[name] = sand.location
        self.sand_points.append(sand)

    def create_paths(self):
        paths = []
        for description in self.descriptions:
            new_path = Path(description)
            paths.append(new_path)
        return paths
    
    def create_floor(self):
        floor_y = self.max_y + 2
        x_range_incr = (self.max_x - self.min_x) * 10
        floor_min_x = self.min_x - x_range_incr
        floor_max_x = self.max_x + x_range_incr
        floor = []
        for x in range(floor_min_x, floor_max_x):
            new_point = Point(x, floor_y)
            floor.append(new_point)
        return floor
    
    def add_floor_to_occupied_points(self):
        for point in self.floor:
            name = f"x{point.x}y{point.y}"
            self.occupied_points[name] = point
    
    def determine_rock_points(self):
        points = set()
        for path in self.paths:
            for point in path.all_points:
                points.add(point)
        return sorted(points)
    
    def create_occupied_points(self):
        points = {}
        for point in self.rock_points:
            name = f"x{point.x}y{point.y}"
            points[name] = point
        return points
    
    def find_max_y(self):
        y_values = []
        for point in self.rock_points:
            y_values.append(point.y)
        sorted_y = sorted(y_values)
        return sorted_y[-1]

def solve_problem(part):
    data = extract_data_from_file(14, True)
    cave = Cave(data)
    if part == 1:
        cave.add_sand_until_first_out_of_cave()
        sands = cave.calculate_total_sand_units_fallen_until_out_of_cave()
    else:
        cave.add_floor_to_occupied_points()
        cave.add_sand_until_first_hits_top()
        sands = cave.calculate_total_sand_units_fallen_until_reach_top()
    return sands

def extract_data_from_file(day_number, is_official):
    if is_official:
        name = "data"
    else:
        name = "practice"
    file = open(f"day{day_number}/{name}.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem(2)
print(result)
