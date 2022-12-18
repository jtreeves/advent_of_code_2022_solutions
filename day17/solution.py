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
        self.spaces = []
        self.next_rock_type = 0
        self.height = 0
        self.width = 7

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

def solve_problem():
    data = extract_data_from_file(17)
    chamber = Chamber()
    return data

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
