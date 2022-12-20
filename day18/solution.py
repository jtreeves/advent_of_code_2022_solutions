def solve_problem():
    data = extract_data_from_file(18)
    instructions = list_all_cube_central_coordinates(data)
    cubes = generate_all_cubes(instructions)
    return cubes

def check_if_cubes_touching(first_cube, second_cube):
    distance = calculate_distance_between_cubes(first_cube, second_cube)
    if distance == 1:
        return True
    else:
        return False

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

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
