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

    def blown_left(self):
        for point in self.shape:
            point.move_left()

    def blown_right(self):
        for point in self.shape:
            point.move_right()

    def fall_down(self):
        for point in self.shape:
            point.move_down()

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
