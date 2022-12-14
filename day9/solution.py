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