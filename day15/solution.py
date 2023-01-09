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
    
    def __hash__(self):
        return hash((self.x, self.y))

    def calculate_distance(self, other):
        horizontal = abs(self.x - other.x)
        vertical = abs(self.y - other.y)
        distance = horizontal + vertical
        return distance
    
class Beacon(Point):
    def calculate_tuning_frequency(self):
        frequency = self.x * 4000000 + self.y
        return frequency

class Sensor:
    def __init__(self, description):
        self.descriptions = description.split(": ")
        self.location = self.determine_location()
        self.nearest_beacon = self.determine_nearest_beacon()
        self.maximum_range = self.determine_maximum_range()
    
    def __repr__(self):
        return f"{self.location}: {self.maximum_range}"

    def determine_location(self):
        sensor_descriptions = self.descriptions[0].split(", ")
        x_parts = sensor_descriptions[0].split("=")
        y_parts = sensor_descriptions[1].split("=")
        x = int(x_parts[1])
        y = int(y_parts[1])
        location = Point(x, y)
        return location
    
    def determine_nearest_beacon(self):
        beacon_descriptions = self.descriptions[1].split(", ")
        x_parts = beacon_descriptions[0].split("=")
        y_parts = beacon_descriptions[1].split("=")
        x = int(x_parts[1])
        y = int(y_parts[1])
        beacon = Beacon(x, y)
        return beacon
    
    def determine_maximum_range(self):
        maximum_range = self.location.calculate_distance(self.nearest_beacon)
        return maximum_range
    
    def check_if_in_range(self, other):
        distance = self.location.calculate_distance(other)
        if distance <= self.maximum_range:
            return True
        else:
            return False

class Grid:
    def __init__(self, description):
        self.descriptions = description.split("\n")
        self.sensors = self.create_sensors()
        self.beacons = self.list_all_beacons()
    
    def __repr__(self):
        return f"{self.sensors}"

    def create_sensors(self):
        sensors = []
        for description in self.descriptions:
            new_sensor = Sensor(description)
            sensors.append(new_sensor)
        return sensors
    
    def list_all_beacons(self):
        beacons = set()
        for sensor in self.sensors:
            beacons.add(sensor.nearest_beacon)
        return list(beacons)
    
    def determine_sensors_applicable_to_row(self, row):
        applicable = []
        for sensor in self.sensors:
            sensor_range = sensor.maximum_range
            sensor_row = sensor.location.y
            sensor_min = sensor_row - sensor_range
            sensor_max = sensor_row + sensor_range
            if row in range(sensor_min, sensor_max + 1):
                applicable.append(sensor)
        return applicable
    
    def determine_beaconless_positions_in_row(self, row):
        beaconless_positions = set()
        sensors = self.determine_sensors_applicable_to_row(row)
        for sensor in sensors:
            sensor_range = sensor.maximum_range
            sensor_row = sensor.location.y
            sensor_column = sensor.location.x
            difference = abs(sensor_row - row)
            overflow = sensor_range - difference
            x_min = sensor_column - overflow
            x_max = sensor_column + overflow
            for x in range(x_min, x_max + 1):
                new_point = Point(x, row)
                if new_point not in self.beacons:
                    beaconless_positions.add(new_point)
        return list(beaconless_positions)
    
    def calculate_amount_of_beaconless_positions_in_row(self, row):
        positions = self.determine_beaconless_positions_in_row(row)
        return len(positions)

    def find_only_position_for_missing_beacon(self, maximum):
        checked_positions = set()
        for sensor in self.sensors:
            sensor_x = sensor.location.x
            sensor_y = sensor.location.y
            radius = sensor.maximum_range
            for side in range(4):
                for i in range(sensor.maximum_range + 1):
                    match side:
                        case 0:
                            edge_x = sensor_x + radius + 1 - i
                            edge_y = sensor_y + i
                        case 1:
                            edge_x = sensor_x - i
                            edge_y = sensor_y + radius + 1 - i
                        case 2:
                            edge_x = sensor_x - radius - 1 + i
                            edge_y = sensor_y - i
                        case 3:
                            edge_x = sensor_x + i
                            edge_y = sensor_y - radius - 1 + i
                    if edge_x < 0 or edge_x > maximum or edge_y < 0 or edge_y > maximum:
                        continue
                    else:
                        edge = Point(edge_x, edge_y)
                        if edge not in checked_positions:
                            not_in_ranges = []
                            for testing_sensor in self.sensors:
                                test_in_range = testing_sensor.check_if_in_range(edge)
                                if not test_in_range:
                                    not_in_ranges.append(test_in_range)
                            if len(not_in_ranges) == len(self.sensors):
                                return Beacon(edge.x, edge.y)
                            else:
                                checked_positions.add(edge)

def solve_problem():
    data = extract_data_from_file(15, True)
    grid = Grid(data)
    position = grid.find_only_position_for_missing_beacon(4000000)
    frequency = position.calculate_tuning_frequency()
    return frequency

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

# For tip to explore edges of each sensor one by one
# https://github.com/noah-clements/AoC2022/blob/master/day15/day15.py
