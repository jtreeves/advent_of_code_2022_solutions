class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))

def solve_problem():
    data = extract_data_from_file(18, True)
    instructions = list_all_cube_central_coordinates(data)
    cubes = generate_all_cubes(instructions)
    surface_area = calculate_total_surface_area(cubes)
    outer_area = calculate_outer_surface_area(cubes)
    return {
        "part1": surface_area,
        "part2": outer_area
    }

def calculate_total_surface_area(cubes):
    surface_area = 0
    for cube in cubes:
        visible_faces = determine_visible_faces_on_cube(cube, cubes)
        surface_area += visible_faces
    return surface_area

def determine_visible_faces_on_cube(main_cube, other_cubes):
    visible_faces = 6
    for other_cube in other_cubes:
        touching = check_if_cubes_touching(main_cube, other_cube)
        if touching:
            visible_faces -= 1
    return visible_faces

def check_if_cubes_touching(first_cube, second_cube):
    distance = calculate_distance_between_cubes(first_cube, second_cube)
    if distance == 1:
        return True
    else:
        return False

def calculate_outer_surface_area(cubes):
    outer_area = 0
    extrema = find_maxima_and_minima(cubes)
    visited_cubes = set()
    queue = [extrema["max"]]
    while queue:
        current_cube = queue.pop(0)
        if current_cube in visited_cubes:
            continue
        elif current_cube in cubes:
            outer_area += 1
        else:
            visited_cubes.add(current_cube)
            neighbors = find_neighbors(current_cube)
            for neighbor in neighbors:
                if check_if_in_scope(neighbor, extrema):
                    queue.append(neighbor)
    return outer_area

def find_neighbors(cube):
    x = cube.x
    y = cube.y
    z = cube.z
    x_up = Cube(x + 1, y, z)
    x_down = Cube(x - 1, y, z)
    y_up = Cube(x, y + 1, z)
    y_down = Cube(x, y - 1, z)
    z_up = Cube(x, y, z + 1)
    z_down = Cube(x, y, z - 1)
    neighbors = [
        x_up,
        x_down,
        y_up,
        y_down,
        z_up,
        z_down,
    ]
    return neighbors

def check_if_in_scope(cube, extrema):
    if extrema["min"].x <= cube.x <= extrema["max"].x and extrema["min"].y <= cube.y <= extrema["max"].y and extrema["min"].z <= cube.z <= extrema["max"].z:
        return True
    else:
        return False

def find_maxima_and_minima(cubes):
    max_x = -float('inf')
    max_y = -float('inf')
    max_z = -float('inf')
    min_x = float('inf')
    min_y = float('inf')
    min_z = float('inf')
    for cube in cubes:
        if cube.x > max_x:
            max_x = cube.x
        if cube.x < min_x:
            min_x = cube.x
        if cube.y > max_y:
            max_y = cube.y
        if cube.y < min_y:
            min_y = cube.y
        if cube.z > max_z:
            max_z = cube.z
        if cube.z < min_z:
            min_z = cube.z
    maximum = Cube(max_x + 1, max_y + 1, max_z + 1)
    minimum = Cube(min_x - 1, min_y -1 , min_z - 1)
    extrema = {
        "max": maximum,
        "min": minimum
    }
    return extrema

def calculate_distance_between_cubes(first_cube, second_cube):
    x_delta = first_cube.x - second_cube.x
    x_squared = x_delta ** 2
    y_delta = first_cube.y - second_cube.y
    y_squared = y_delta ** 2
    z_delta = first_cube.z - second_cube.z
    z_squared = z_delta ** 2
    summed_squares = x_squared + y_squared + z_squared
    distance = summed_squares ** (1/2)
    return distance

def generate_all_cubes(instructions):
    cubes = []
    for instruction in instructions:
        center = convert_string_coordinates(instruction)
        cubes.append(center)
    return cubes

def convert_string_coordinates(string_coordinates):
    coordinates = string_coordinates.split(",")
    final_coordinates = []
    for coordinate in coordinates:
        numbered_coordinate = int(coordinate)
        final_coordinates.append(numbered_coordinate)
    return Cube(final_coordinates[0], final_coordinates[1], final_coordinates[2])

def list_all_cube_central_coordinates(data):
    partitioned = data.split("\n")
    return partitioned

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

# Idea for BFS approach to solve part 2:
# https://github.com/silentw0lf/advent_of_code_2022/blob/main/18/solve.py
