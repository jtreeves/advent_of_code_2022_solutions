import itertools

def solve_problem():
    data = extract_data_from_file(18)
    instructions = list_all_cube_initial_coordinates(data)
    cubes = generate_all_cubes(instructions)
    return cubes

def generate_all_cubes(instructions):
    cubes = []
    for instruction in instructions:
        corner = convert_string_coordinates(instruction)
        vertices = generate_all_vertices(corner)
        cubes.append(vertices)
    return cubes

def generate_all_vertices(corner):
    diagonal = []
    for coordinate in corner:
        diagonal.append(coordinate + 1)
    vertices = list(itertools.product(*zip(corner, diagonal)))
    return vertices

# def generate_all_sides(corner):
#     sides = []
#     for coordinate in corner:

#     return sides

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
