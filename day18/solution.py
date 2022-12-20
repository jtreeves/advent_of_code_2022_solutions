def solve_problem():
    data = extract_data_from_file(18)
    instructions = list_all_cube_central_coordinates(data)
    cubes = generate_all_cubes(instructions)
    air_packets = find_air_packets(cubes)
    return air_packets
    # surface_area = calculate_total_surface_area(cubes)
    # return surface_area

def find_air_packets(cubes):
    cubes.sort()
    air_packets = []
    for i in range(len(cubes) - 1):
        current_cube = cubes[i]
        next_cube = cubes[i + 1]
        if current_cube[0] == next_cube[0] and current_cube[1] == next_cube[1] and current_cube[2] + 2 == next_cube[2]:
            air_packet = [
                current_cube[0], 
                current_cube[1], 
                current_cube[2] + 1
            ]
            air_packets.append(air_packet)
    return air_packets

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
