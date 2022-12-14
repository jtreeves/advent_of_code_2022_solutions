tail_current_position = tuple()
tail_positions = set()

def add_new_tail_position(position):
    tail_positions.add(position)

def change_tail_current_position(new_position):
    tail_current_position = new_position
    add_new_tail_position(tail_current_position)

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

change_tail_current_position((1, 1))
change_tail_current_position((2, 3))
change_tail_current_position((5, 10))
change_tail_current_position((7, 7))
change_tail_current_position((5, 10))
print(tail_positions)