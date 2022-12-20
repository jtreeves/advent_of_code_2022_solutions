def solve_problem():
    data = extract_data_from_file(18)
    instructions = list_all_cube_central_coordinates(data)
    cubes = generate_all_cubes(instructions)
    air_packets = find_all_air_packets(cubes)
    # print(air_packets)
    cubes.extend(air_packets)
    trimmed_cubes = eliminate_duplicate_cubes(cubes)
    print(trimmed_cubes)
    surface_area = calculate_total_surface_area(trimmed_cubes)
    return surface_area

def eliminate_duplicate_cubes(cubes):
    trimmed_cubes = []
    for cube in cubes:
        for trimmed_cube in trimmed_cubes:
            if check_if_cubes_equivalent(cube, trimmed_cube):
                continue
        trimmed_cubes.append(cube)
    return trimmed_cubes

def check_if_cubes_equivalent(first_cube, second_cube):
    x1 = first_cube[0]
    x2 = second_cube[0]
    y1 = first_cube[1]
    y2 = second_cube[1]
    z1 = first_cube[2]
    z2 = second_cube[2]
    if x1 == x2 and y1 == y2 and z1 == z2:
        return True
    else:
        return False

def find_all_air_packets(cubes):
    all_air_packets = []
    for cube in cubes:
        air_packets = determine_possible_air_packets_near_cube(cube, cubes)
        all_air_packets.extend(air_packets)
    return all_air_packets

def determine_possible_air_packets_near_cube(main_cube, other_cubes):
    air_packets = []
    for other_cube in other_cubes:
        air_packet_gap = check_if_air_packet_between_cubes(main_cube, other_cube)
        if air_packet_gap:
            air_packet = find_air_packet_between_cubes(main_cube, other_cube)
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

def find_air_packet_between_cubes(first_cube, second_cube):
    x1 = first_cube[0]
    x2 = second_cube[0]
    y1 = first_cube[1]
    y2 = second_cube[1]
    z1 = first_cube[2]
    z2 = second_cube[2]
    if x1 == x2 and y1 == y2:
        return [x1, y1, int((z1 + z2) / 2)]
    elif x1 == x2 and z1 == z2:
        return [x1, int((y1 + y2) / 2), z1]
    else:
        return [int((x1 + x2) / 2), y1, z1]

def check_if_air_packet_between_cubes(first_cube, second_cube):
    distance = calculate_distance_between_cubes(first_cube, second_cube)
    if distance == 2:
        return True
    else:
        return False

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
