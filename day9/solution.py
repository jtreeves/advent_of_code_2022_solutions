class RopeEnd:
    def __init__(self):
        self.current_position = [1, 1]

    def change_current_position(self, new_position):
        self.current_position = new_position

class Tail(RopeEnd):
    def __init__(self):
        super().__init__()
        self.all_positions = set()
        self.all_positions.add(tuple(self.current_position))

    def change_current_position(self, new_position):
        super().change_current_position(new_position)
        self.all_positions.add(tuple(self.current_position))

    def overlaps_head(self, head):
        if self.current_position[0] == head.current_position[0] and self.current_position[1] == head.current_position[1]:
            return True
        else:
            return False

    def adjust_position_based_on_head(self, head):
        tail_x = self.current_position[0]
        tail_y = self.current_position[1]
        head_x = head.current_position[0]
        head_y = head.current_position[1]
        self.change_current_position([tail_x, tail_y])

class Head(RopeEnd):
    def adjust_position_in_direction(self, direction):
        x = self.current_position[0]
        y = self.current_position[1]
        if direction == "R":
            x += 1
        if direction == "L":
            x -= 1
        if direction == "U":
            y += 1
        if direction == "D":
            y -= 1
        self.change_current_position([x, y])

class Move:
    def __init__(self, distance, direction):
        self.distance = distance
        self.direction = direction

def list_all_moves(instructions):
    lines = instructions.split("\n")
    moves = []
    for line in lines:
        command = line.split(" ")
        move = Move(command[1], command[0])
        moves.append(move)
    return moves

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

t = Tail()
print(t.current_position)
t.change_current_position([5, 7])
t.change_current_position([2, 3])
t.change_current_position([1, 1])
t.change_current_position([7, 7])
print(t.current_position)
print(t.all_positions)
h = RopeEnd()
print(h.current_position)
h.change_current_position([4, 5])
print(h.current_position)