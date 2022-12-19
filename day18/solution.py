class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Cube:
    def __init__(self, string_coordinates):
        self.corner = self.convert_string_coordinates(string_coordinates)

    def convert_string_coordinates(string_coordinates):
        coordinates = string_coordinates.split(",")
        x = int(coordinates[0])
        y = int(coordinates[1])
        z = int(coordinates[2])
        return Coordinate(x, y, z)

def solve_problem():
    data = extract_data_from_file(18)
    return data

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
