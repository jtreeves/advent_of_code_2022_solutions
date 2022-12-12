def list_all_cycle_increments(moves):
    cylces = []
    for move in moves:
        cycle = determine_cycles_to_wait(move)
        cylces.append(cycle)
    return cylces

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