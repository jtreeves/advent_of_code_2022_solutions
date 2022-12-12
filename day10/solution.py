def calculate_signal_strength(register, cycle):
    strength = register * cycle
    return strength

def determine_register_statuses_at_key_cycles(moves):
    increments = list_all_cycle_and_register_increments(moves)
    starting_values = {
        "cycles": 1,
        "register": 1
    }
    key_values = [starting_values]
    for index in range(len(increments)):
        old_cycles = key_values[index]["cycles"]
        old_register = key_values[index]["register"]
        cycles_increment = increments[index]["cycles"]
        register_increment = increments[index]["register"]
        new_cycles = old_cycles + cycles_increment
        new_register = old_register + register_increment
        key_values.append({
            "cycles": new_cycles,
            "register": new_register
        })
    return key_values

def list_all_cycle_and_register_increments(moves):
    increments = []
    for move in moves:
        cycles = determine_cycles_increment(move)
        register = determine_register_increment(move)
        increments.append({
            "cycles": cycles,
            "register": register
        })
    return increments

def determine_register_increment(move):
    is_noop = move == "noop"
    if is_noop:
        return 0
    else:
        partitioned = move.split(" ")
        increment = int(partitioned[1])
        return increment

def determine_cycles_increment(move):
    is_noop = move == "noop"
    if is_noop:
        return 1
    else:
        return 2

def list_all_moves(instructions):
    moves = instructions.split("\n")
    return moves

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

# print(determine_cycle_increment("noop"))
# print(determine_cycle_increment("addx -6"))
# print(determine_register_statuses_at_key_cycles(['noop', 'addx 5', 'noop', 'addx 1', 'addx -2']))
# print(determine_register_statuses_at_key_cycles(['noop', 'addx 3', 'addx -5']))

# data = extract_data_from_file(10)
# moves = list_all_moves(data)
# print(determine_register_statuses_at_key_cycles(moves))
print(calculate_signal_strength(21, 20))