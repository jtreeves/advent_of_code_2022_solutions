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

    def touching_point_on_left(self, other):
        if self.x - 1 == other.x and self.y == other.y:
            return True
        else:
            return False

    def touching_point_on_right(self, other):
        if self.x + 1 == other.x and self.y == other.y:
            return True
        else:
            return False

    def touching_point_on_bottom(self, other):
        if self.x == other.x and self.y - 1 == other.y:
            return True
        else:
            return False

class Chamber:
    def __init__(self, pattern):
        self.jet_pattern = pattern
        self.spaces = []
        self.height = 0
        self.next_rock_type = 1
        self.current_iteration = 0
        self.next_jet_blow = self.jet_pattern[self.current_iteration]
        for i in range(7):
            self.spaces.append(Coordinate(i + 1, 0))
    
    def drop_new_rock(self):
        new_rock = Rock(self.next_rock_type, self.height)
        self.let_rock_fall_to_rest(new_rock)
        self.add_rock_to_spaces(new_rock)
        self.update_height(new_rock)
        self.increment_new_rock_type()

    def let_rock_fall_to_rest(self, rock):
        self.increment_pattern(rock)
        while not rock.touching_floor(self.spaces):
            rock.fall_down(self.spaces)
            self.increment_pattern(rock)

    def blow_rock_left(self, rock):
        rock.blown_left(self.spaces)

    def blow_rock_right(self, rock):
        rock.blown_right(self.spaces)
    
    def increment_pattern(self, rock):
        if self.next_jet_blow == "<":
            self.blow_rock_left(rock)
        elif self.next_jet_blow == ">":
            self.blow_rock_right(rock)
        self.current_iteration += 1
        if self.current_iteration >= len(self.jet_pattern):
            self.jet_pattern += self.jet_pattern
        self.next_jet_blow = self.jet_pattern[self.current_iteration]

    def increment_new_rock_type(self):
        if self.next_rock_type < 5:
            self.next_rock_type += 1
        else:
            self.next_rock_type = 1
    
    def update_height(self, rock):
        for point in rock.shape:
            if point.y > self.height:
                self.height = point.y

    def add_rock_to_spaces(self, rock):
        for point in rock.shape:
            self.spaces.append(point)

class Rock:
    def __init__(self, type, height):
        if type == 1:
            self.shape = []
            for i in range(4):
                self.shape.append(Coordinate(i + 3, height + 4))
            self.left_border = [self.shape[0]]
            self.right_border = [self.shape[3]]
            self.bottom_border = self.shape
        elif type == 2:
            self.shape = [
                Coordinate(4, height + 4),
                Coordinate(3, height + 5),
                Coordinate(4, height + 5),
                Coordinate(5, height + 5),
                Coordinate(4, height + 6),
            ]
            self.left_border = [
                self.shape[0],
                self.shape[1],
                self.shape[4],
            ]
            self.right_border = [
                self.shape[0],
                self.shape[3],
                self.shape[4],
            ]
            self.bottom_border = [
                self.shape[0],
                self.shape[1],
                self.shape[3],
            ]
        elif type == 3:
            self.shape = [
                Coordinate(3, height + 4),
                Coordinate(4, height + 4),
                Coordinate(5, height + 4),
                Coordinate(5, height + 5),
                Coordinate(5, height + 6),
            ]
            self.left_border = [self.shape[0]]
            self.right_border = self.shape[2:]
            self.bottom_border = self.shape[:3]
        elif type == 4:
            self.shape = []
            for i in range(4):
                self.shape.append(Coordinate(3, height + i + 4))
            self.left_border = self.shape
            self.right_border = self.shape
            self.bottom_border = [self.shape[0]]
        else:
            self.shape = [
                Coordinate(3, height + 4),
                Coordinate(4, height + 4),
                Coordinate(3, height + 5),
                Coordinate(4, height + 5),
            ]
            self.left_border = [
                self.shape[0],
                self.shape[2]
            ]
            self.right_border = [
                self.shape[1],
                self.shape[3]
            ]
            self.bottom_border = self.shape[:2]

    def blown_left(self, other_points):
        if not self.touching_left_wall() and not self.touching_rock_to_left(other_points):
            for point in self.shape:
                point.move_left()

    def blown_right(self, other_points):
        if not self.touching_right_wall() and not self.touching_rock_to_right(other_points):
            for point in self.shape:
                point.move_right()

    def fall_down(self, other_points):
        if not self.touching_floor(other_points):
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

    def touching_rock_to_left(self, other_points):
        for point in self.shape:
            for other_point in other_points[::-1]:
                if point.touching_point_on_left(other_point):
                    return True
        return False

    def touching_rock_to_right(self, other_points):
        for point in self.shape:
            for other_point in other_points[::-1]:
                if point.touching_point_on_right(other_point):
                    return True
        return False

    def touching_floor(self, other_points):
        for point in self.shape:
            for other_point in other_points[::-1]:
                if point.touching_point_on_bottom(other_point):
                    return True
        return False

def solve_problem():
    data = extract_data_from_file(17)
    chamber = Chamber(data)
    for i in range(2022):
        chamber.drop_new_rock()
        print(f"DROPPING ROCK {i + 1}")
    return chamber.height

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
