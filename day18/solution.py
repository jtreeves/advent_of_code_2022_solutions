def solve_problem():
    data = extract_data_from_file(18)
    return data

def generate_all_cubes(instructions):
    cubes = []
    for instruction in instructions:
        corner = convert_string_coordinates(instruction)
        vertices = generate_all_vertices(corner)
        cubes.append(vertices)
    return cubes

def generate_all_vertices(corner):
    x = corner[0]
    y = corner[1]
    z = corner[2]
    x1 = x + 1
    y1 = y + 1
    z1 = z + 1
    vertices = [
        [x, y, z],
        [x1, y1, z1],
        [x, y, z1],
        [x, y1, z],
        [x1, y, z],
        [x, y1, z1],
        [x1, y, z1],
        [x1, y1, z],
    ]
    return vertices

def convert_string_coordinates(string_coordinates):
    coordinates = string_coordinates.split(",")
    final_coordinates = []
    for coordinate in coordinates:
        numbered_coordinate = int(coordinate)
        final_coordinates.append(numbered_coordinate)
    return final_coordinates

def list_all_cube_initial_coordinates(data):
    partitioned = data.split("\n")
    return partitioned

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
