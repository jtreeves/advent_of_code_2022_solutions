class RopePart:
    current_position = [1, 1]

    def change_current_position(self, new_position):
        self.current_position = new_position

class Tail(RopePart):
    all_positions = set()

    def __init__(self):
        self.all_positions.add(tuple(self.current_position))

    def change_current_position(self, new_position):
        super().change_current_position(new_position)
        self.all_positions.add(tuple(self.current_position))

def list_all_moves(instructions):
    lines = instructions.split("\n")
    moves = []
    for line in lines:
        command = line.split(" ")
        move = {
            "direction": command[0],
            "distance": command[1]
        }
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