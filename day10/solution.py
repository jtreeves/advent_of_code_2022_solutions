def solve_problem():
    data = extract_data_from_file(10)
    moves = list_all_moves(data)
    statuses = determine_register_statuses_at_key_cycles(moves)
    total = sum_key_signal_strengths(statuses)
    return total

def sum_key_signal_strengths(statuses):
    pairs = find_main_register_cycle_pairs(statuses)
    total = 0
    for pair in pairs:
        register = pair["register"]
        cycles = pair["cycles"]
        strength = calculate_signal_strength(register, cycles)
        total += strength
    return total

def find_main_register_cycle_pairs(statuses):
    key_cycles = [20, 60, 100, 140, 180, 220]
    pairs = []
    for cycle in key_cycles:
        register = find_register_at_cycle_from_statuses(statuses, cycle)
        pairs.append({
            "cycles": cycle,
            "register": register
        })
    return pairs

def calculate_signal_strength(register, cycle):
    strength = register * cycle
    return strength

def find_register_at_cycle_from_statuses(statuses, cycle_number):
    register_before = None
    register_at = None
    for status in statuses:
        if status["cycles"] == cycle_number - 1:
            register_before = status["register"]
        if status["cycles"] == cycle_number:
            register_at = status["register"]
    if register_at != None:
        return register_at
    else:
        return register_before

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

result = solve_problem()
print(result)