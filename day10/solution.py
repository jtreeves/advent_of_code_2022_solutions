def determine_register_statuses_at_key_cycles(moves):
    cycles = list_all_cycle_increments(moves)
    starting_values = {
        "status": 1,
        "cycles": 1,
    }
    key_values = [starting_values]
    for index in range(len(cycles)):
        new_status = key_values[index]

def list_all_cycle_increments(moves):
    cylces = []
    for move in moves:
        cycle = determine_cycles_to_wait(move)
        cylces.append(cycle)
    return cylces

def determine_register_increment(move):
    is_noop = move == "noop"
    if is_noop:
        return 0
    else:
        partitioned = move.split(" ")
        increment = int(partitioned[1])
        return increment

def determine_cycles_to_wait(move):
    is_noop = move == "noop"
    if is_noop:
        return 1
    else:
        return 2

def list_all_moves(instructions):
    moves = instructions.split("\n")
    return moves

# print(determine_cycles_to_wait("noop"))
# print(determine_cycles_to_wait("addx -6"))
print(list_all_cycle_increments(['noop', 'addx 5', 'noop', 'addx 1', 'addx -2']))