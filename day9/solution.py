class RopeKnot:
    def __init__(self):
        self.current_position = [1, 1]

    def change_current_position(self, new_position):
        self.current_position = new_position

class Tail(RopeKnot):
    def __init__(self):
        super().__init__()
        self.all_positions = set()
        self.all_positions.add(tuple(self.current_position))

    def change_current_position(self, new_position):
        super().change_current_position(new_position)
        self.all_positions.add(tuple(self.current_position))

    def count_all_positions(self):
        total = len(self.all_positions)
        return total

    def is_touching_head(self, head):
        tail_x = self.current_position[0]
        tail_y = self.current_position[1]
        head_x = head.current_position[0]
        head_y = head.current_position[1]
        overlapping_head = tail_x == head_x and tail_y == head_y
        after_head = tail_x == head_x + 1 and tail_y == head_y
        before_head = tail_x == head_x - 1 and tail_y == head_y
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
        tail_y = self.current_position[1]
        head_y = head.current_position[1]
        same_row = tail_y == head_y
        return same_row

    def is_in_same_column_as_head(self, head):
        tail_x = self.current_position[0]
        head_x = head.current_position[0]
        same_column = tail_x == head_x
        return same_column

    def is_before_head(self, head):
        tail_x = self.current_position[0]
        head_x = head.current_position[0]
        before_head = tail_x < head_x
        return before_head

    def is_below_head(self, head):
        tail_y = self.current_position[1]
        head_y = head.current_position[1]
        below_head = tail_y < head_y
        return below_head

    def move_diagonally_to_head(self, head):
        tail_x = self.current_position[0]
        tail_y = self.current_position[1]
        is_before = self.is_before_head(head)
        is_below = self.is_below_head(head)
        if is_before and is_below:
            tail_x += 1
            tail_y += 1
        elif is_before and not is_below:
            tail_x += 1
            tail_y -= 1
        elif not is_before and is_below:
            tail_x -= 1
            tail_y += 1
        elif not is_before and not is_below:
            tail_x -= 1
            tail_y -= 1
        self.change_current_position([tail_x, tail_y])

    def move_horizontally_to_head(self, head):
        tail_x = self.current_position[0]
        tail_y = self.current_position[1]
        is_before = self.is_before_head(head)
        if is_before:
            tail_x += 1
        else:
            tail_x -= 1
        self.change_current_position([tail_x, tail_y])

    def move_vertically_to_head(self, head):
        tail_x = self.current_position[0]
        tail_y = self.current_position[1]
        is_below = self.is_below_head(head)
        if is_below:
            tail_y += 1
        else:
            tail_y -= 1
        self.change_current_position([tail_x, tail_y])

    def adjust_position_based_on_head(self, head):
        same_row = self.is_in_same_row_as_head(head)
        same_column = self.is_in_same_column_as_head(head)
        if not self.is_touching_head(head):
            if not same_row and not same_column:
                self.move_diagonally_to_head(head)
            else:
                if same_row:
                    self.move_horizontally_to_head(head)
                else:
                    self.move_vertically_to_head(head)

class Head(RopeKnot):
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
        self.distance = int(distance)
        self.direction = direction

def solve_problem(part):
    data = extract_data_from_file(9)
    moves = list_all_moves(data)
    head = Head()
    if part == 1:
        tail = Tail()
        execute_all_moves(moves, head, tail)
        total_tail_positions = tail.count_all_positions()
        return total_tail_positions
    else:
        tail1 = Tail()
        tail2 = Tail()
        tail3 = Tail()
        tail4 = Tail()
        tail5 = Tail()
        tail6 = Tail()
        tail7 = Tail()
        tail8 = Tail()
        tail9 = Tail()
        execute_all_moves_for_multiple_tails(moves, head, tail1, tail2, tail3, tail4, tail5, tail6, tail7, tail8, tail9)
        total_last_tail_positions = tail9.count_all_positions()
        return total_last_tail_positions

def execute_all_moves(moves, head, tail):
    for move in moves:
        adjust_head_then_tail_for_move(move, head, tail)

def adjust_head_then_tail_for_move(move, head, tail):
    distance = move.distance
    direction = move.direction
    for _ in range(distance):
        head.adjust_position_in_direction(direction)
        tail.adjust_position_based_on_head(head)

def execute_all_moves_for_multiple_tails(moves, head, tail1, tail2, tail3, tail4, tail5, tail6, tail7, tail8, tail9):
    for move in moves:
        adjust_head_then_multiple_tails_for_move(move, head, tail1, tail2, tail3, tail4, tail5, tail6, tail7, tail8, tail9)

def adjust_head_then_multiple_tails_for_move(move, head, tail1, tail2, tail3, tail4, tail5, tail6, tail7, tail8, tail9):
    distance = move.distance
    direction = move.direction
    for _ in range(distance):
        head.adjust_position_in_direction(direction)
        tail1.adjust_position_based_on_head(head)
        tail2.adjust_position_based_on_head(tail1)
        tail3.adjust_position_based_on_head(tail2)
        tail4.adjust_position_based_on_head(tail3)
        tail5.adjust_position_based_on_head(tail4)
        tail6.adjust_position_based_on_head(tail5)
        tail7.adjust_position_based_on_head(tail6)
        tail8.adjust_position_based_on_head(tail7)
        tail9.adjust_position_based_on_head(tail8)

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

result = solve_problem(2)
print(result)
