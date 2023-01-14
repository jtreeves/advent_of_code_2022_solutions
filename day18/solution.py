def solve_problem():
    data = extract_data_from_file(18, True)
    instructions = list_all_cube_central_coordinates(data)
    cubes = generate_all_cubes(instructions)
    surface_area = calculate_total_surface_area(cubes)
    return surface_area

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

def find_neighbors(cube):
    return

def check_if_in_scope(cube, extrema):
    if extrema["min"][0] <= cube[0] <= extrema["max"][0] and extrema["min"][1] <= cube[1] <= extrema["max"][1] and extrema["min"][2] <= cube[2] <= extrema["max"][2]:
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
        if cube[0] > max_x:
            max_x = cube[0]
        if cube[0] < min_x:
            min_x = cube[0]
        if cube[1] > max_y:
            max_y = cube[1]
        if cube[1] < min_y:
            min_y = cube[1]
        if cube[2] > max_z:
            max_z = cube[2]
        if cube[2] < min_z:
            min_z = cube[2]
    maximum = [max_x, max_y, max_z]
    minimum = [min_x, min_y, min_z]
    extrema = {
        "max": maximum,
        "min": minimum
    }
    return extrema

def calculate_distance_between_cubes(first_cube, second_cube):
    summed_deltas = 0
    for i in range(len(first_cube)):
        delta = first_cube[i] - second_cube[i]
        delta_squared = delta ** 2
        summed_deltas += delta_squared
    distance = summed_deltas ** (1/2)
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
    return final_coordinates

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
