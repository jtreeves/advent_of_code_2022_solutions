class Position:
    def __init__(self, x, y, blocked):
        self.x = x
        self.y = y
        self.blocked = blocked
    
    def __repr__(self):
        return f"({self.x}, {self.y}): {self.blocked}"

class Blizzard:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
    
    def __repr__(self):
        return f"({self.position.x}, {self.position.y}): {self.direction}"
    
    def update_position(self, all_positions):
        pass

class Traveler:
    def __init__(self, position):
        self.position = position
    
    def __repr__(self):
        return f"({self.position.x}, {self.position.y})"

    def update_position(self, all_positions):
        pass

class Valley:
    def __init__(self, description):
        self.description = description.split("\n")
        self.height = len(self.description)
        self.width = len(self.description[0])
        self.blizzards = {}
        self.positions = self.create_positions()
    
    def __repr__(self):
        return f"{self.starting_position} -> {self.ending_position}"
    
    def create_positions(self):
        positions = {}
        for row in range(self.height):
            for column in range(self.width):
                character = self.description[row][column]
                blocked = character == "#"
                name = f"x{column}y{row}"
                new_position = Position(column, row, blocked)
                positions[name] = new_position
                if row == 0 and not blocked:
                    self.starting_position = name
                    self.traveler = Traveler(new_position)
                if row == self.height - 1 and not blocked:
                    self.ending_position = name
                if character != "#" and character != ".":
                    self.blizzards[name] = Blizzard(new_position, character)
        return positions

    def update_valley(self):
        self.update_blizzards()
        self.update_traveler()

    def update_blizzards(self):
        for blizzard in self.blizzards.values():
            blizzard.update_position(self.positions)

    def update_traveler(self):
        self.traveler.update_position()

def solve_problem():
    data = extract_data_from_file(24, False)
    valley = Valley(data)
    return valley

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
