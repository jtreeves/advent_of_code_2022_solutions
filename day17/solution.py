class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move_left(self):
        self.x = self.x - 1
    
    def move_right(self):
        self.x = self.x + 1
    
    def move_down(self):
        self.y = self.y - 1

class Chamber:
    def __init__(self, pattern):
        while len(pattern) < 2022:
            pattern += pattern
        self.jet_pattern = pattern
        self.spaces = set()
        for i in range(7):
            self.spaces.add(Coordinate(0, i + 1))
        self.next_rock_type = 1
        self.width = 7
        self.height = 0
    
    def drop_new_rock(self):
        new_rock = Rock(self.next_rock_type, self.height)
        for point in new_rock.shape:
            self.spaces.add(point)
        if self.next_rock_type < 5:
            self.next_rock_type += 1
        else:
            self.next_rock_type = 1

class Rock:
    def __init__(self, type, height):
        if type == 1:
            self.shape = []
            for i in range(4):
                self.shape.append(Coordinate(i + 3, height + 3))
        elif type == 2:
            self.shape = [
                Coordinate(4, height + 3),
                Coordinate(3, height + 4),
                Coordinate(4, height + 4),
                Coordinate(5, height + 4),
                Coordinate(4, height + 5),
            ]
        elif type == 3:
            self.shape = [
                Coordinate(3, height + 3),
                Coordinate(4, height + 3),
                Coordinate(5, height + 3),
                Coordinate(5, height + 4),
                Coordinate(5, height + 5),
            ]
        elif type == 4:
            self.shape = []
            for i in range(4):
                self.shape.append(3, height + i + 3)
        else:
            self.shape = [
                Coordinate(3, height + 3),
                Coordinate(4, height + 3),
                Coordinate(3, height + 4),
                Coordinate(4, height + 4),
            ]

    def blown_left(self, other_points):
        if not self.touching_left_wall() and not self.touching_rock_or_floor(other_points):
            for point in self.shape:
                point.move_left()

    def blown_right(self, other_points):
        if not self.touching_right_wall() and not self.touching_rock_or_floor(other_points):
            for point in self.shape:
                point.move_right()

    def fall_down(self, other_points):
        if not self.touching_rock_or_floor(other_points):
            for point in self.shape:
                point.move_down()

    def touching_left_wall(self):
        for point in self.shape:
            if point.x == 1:
                return True
        return False

    def touching_right_wall(self):
        for point in self.shape:
            if point.x == 7:
                return True
        return False

    def touching_rock_or_floor(self, other_points):
        for rock_point in self.shape:
            for other_point in other_points:
                if rock_point.x == other_point.x and rock_point.y == other_point.y:
                    return True
        return False

def solve_problem():
    data = extract_data_from_file(17)
    chamber = Chamber(data)
    chamber.drop_new_rock()
    for space in chamber.spaces:
        print([space.x, space.y])
    print(f"NEXT ROCK TYPE: {chamber.next_rock_type}")
    return

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
