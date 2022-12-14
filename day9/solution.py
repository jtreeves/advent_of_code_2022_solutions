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

    def is_touching_head(self, head):
        tail_x = self.current_position[0]
        tail_y = self.current_position[1]
        head_x = head.current_position[0]
        head_y = head.current_position[1]
        overlapping_head = tail_x == head_x and tail_y == head_y
        after_head = tail_x == head_x + 1 and tail_y == head_y
        before_head = tail_x == head_x - 1 and tail_y == head_y + 1
        above_head = tail_x == head_x and tail_y == head_y + 1
        under_head = tail_x == head_x and tail_y == head_y - 1
        diagonally_bl_head = tail_x == head_x - 1 and tail_y == head_y - 1
        diagonally_br_head = tail_x == head_x + 1 and tail_y == head_y - 1
        diagonally_tl_head = tail_x == head_x - 1 and tail_y == head_y + 1
        diagonally_tr_head = tail_x == head_x + 1 and tail_y == head_y + 1
        touching = overlapping_head or after_head or before_head or above_head or under_head or diagonally_br_head or diagonally_bl_head or diagonally_tl_head or diagonally_tr_head
        if touching:
            return True
        else:
            return False

    def is_in_same_row_as_head(self, head):
        tail_x = self.current_position[0]
        head_x = head.current_position[0]
        same_row = tail_x == head_x
        return same_row

    def is_in_same_column_as_head(self, head):
        tail_y = self.current_position[1]
        head_y = head.current_position[1]
        same_column = tail_y == head_y
        return same_column

    def catch_up_to_head(self, head):
        tail_x = self.current_position[0]
        tail_y = self.current_position[1]
        head_x = head.current_position[0]
        head_y = head.current_position[1]
        self.change_current_position([tail_x, tail_y])

    def adjust_position_based_on_head(self, head):
        if not self.is_touching_head(self, head):
            self.catch_up_to_head(self, head)

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