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
        beacon = Point(x, y)
        return beacon
    
    def determine_maximum_range(self):
        maximum_range = self.location.calculate_distance(self.nearest_beacon)
        return maximum_range

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
        return len(beaconless_positions)

def solve_problem():
    data = extract_data_from_file(15, True)
    grid = Grid(data)
    positions = grid.determine_beaconless_positions_in_row(2000000)
    return positions

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
