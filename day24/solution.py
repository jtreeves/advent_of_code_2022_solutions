class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Position):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            return False
    
    def __hash__(self):
        return hash((self.x, self.y))

class Blizzard(Position):
    def __init__(self, x, y, direction):
        super().__init__(x, y)
        self.direction = direction
    
    def __repr__(self):
        return f"({self.x}, {self.y}): {self.direction}"
    
    def update_position(self, height, width):
        match self.direction:
            case ">":
                new_x = self.x + 1 if self.x + 1 < width - 1 else 1
                new_y = self.y
            case "v":
                new_x = self.x
                new_y = self.y + 1 if self.y + 1 < height - 1 else 1
            case "<":
                new_x = self.x - 1 if self.x - 1 > 0 else width - 2
                new_y = self.y
            case "^":
                new_x = self.x
                new_y = self.y - 1 if self.y - 1 > 0 else height - 2
        self.x = new_x
        self.y = new_y

class Traveler(Position):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.moves = 0

    def update_position(self, height, width, blizzards):
        new_x = self.x
        new_y = self.y
        if new_y < height - 2 and Position(new_x, new_y + 1) not in blizzards:
            new_y += 1
        elif new_x < width - 2 and Position(new_x + 1, new_y) not in blizzards:
            new_x += 1
        elif Position(new_x, new_y) not in blizzards:
            self.moves += 1
            return
        elif new_x > 1 and Position(new_x - 1, new_y) not in blizzards:
            new_x -= 1
        elif new_y > 1 and Position(new_x, new_y - 1) not in blizzards:
            new_y -= 1
        self.x = new_x
        self.y = new_y
        self.moves += 1

class Valley:
    def __init__(self, description):
        self.description = description.split("\n")
        self.height = len(self.description)
        self.width = len(self.description[0])
        self.blizzards = []
        self.create_positions()
    
    def __repr__(self):
        diagram = ""
        for y in range(self.height):
            for x in range(self.width):
                if Position(x, y) == self.traveler:
                    diagram += "T"
                elif f"x{x}y{y}" == self.starting_position:
                    diagram += "S"
                elif f"x{x}y{y}" == self.ending_position:
                    diagram += "E"
                elif Position(x, y) in self.blizzards:
                    diagram += "B"
                elif x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                    diagram += "#"
                else:
                    diagram += "."
            diagram += "\n"
        diagram = diagram[:-1]
        return diagram
    
    def create_positions(self):
        for row in range(self.height):
            for column in range(self.width):
                character = self.description[row][column]
                wall = character == "#"
                empty = character == "."
                name = f"x{column}y{row}"
                if row == 0 and not wall:
                    self.starting_position = name
                    self.traveler = Traveler(column, row)
                elif row == self.height - 1 and not wall:
                    self.ending_position = name
                elif not wall and not empty:
                    self.blizzards.append(Blizzard(column, row, character))

    def determine_how_long_for_traveler_to_exit(self):
        while not self.check_if_traveler_exited():
            self.update_valley()
        return self.traveler.moves

    def update_valley(self):
        self.update_blizzards()
        self.update_traveler()

    def update_blizzards(self):
        for blizzard in self.blizzards:
            blizzard.update_position(self.height, self.width)

    def update_traveler(self):
        self.traveler.update_position(self.height, self.width, self.blizzards)
    
    def check_if_traveler_exited(self):
        traveler_position = f"x{self.traveler.x}y{self.traveler.y}"
        if traveler_position == self.ending_position:
            return True
        else:
            return False

def solve_problem():
    data = extract_data_from_file(24, False)
    valley = Valley(data)
    moves = valley.determine_how_long_for_traveler_to_exit()
    return moves

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
