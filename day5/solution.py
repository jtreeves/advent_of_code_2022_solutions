def solve_problem(step):
    data = extract_data_from_file(5)
    separated = separate_description_from_directions(data)
    description = separated["description"]
    directions = separated["directions"]
    original_stacks = determine_original_stacks(description)
    listed_directions = list_all_directions(directions)
    if step == 1:
        updated_stacks_one_at_a_time = move_all_crates_one_at_a_time(original_stacks, listed_directions)
        top_crates_one_at_a_time = determine_top_crates_from_stacks(updated_stacks_one_at_a_time)
        return top_crates_one_at_a_time
    else:
        updated_stacks_at_once = move_all_crates_at_once(original_stacks, listed_directions)
        top_crates_at_once = determine_top_crates_from_stacks(updated_stacks_at_once)
        return top_crates_at_once

def separate_description_from_directions(data):
    sections = data.split("\n\n")
    description = sections[0]
    directions = sections[1]
    return {
        "description": description,
        "directions": directions
    }

def determine_top_crates_from_stacks(stacks):
    result = ""
    for stack in stacks:
        top_crate = stack.pop()
        result += top_crate
    return result

def move_all_crates_at_once(original_stacks, directions):
    updated_stacks = original_stacks
    for direction in directions:
        updated_stacks = move_crates_at_once(original_stacks, direction)
    return updated_stacks

def move_all_crates_one_at_a_time(original_stacks, directions):
    updated_stacks = original_stacks
    for direction in directions:
        updated_stacks = move_crates_one_at_time(original_stacks, direction)
    return updated_stacks

def move_crates_at_once(current_stacks, direction):
    boxes_to_move = extract_how_many_boxes_to_move(direction)
    source_number = extract_source_stack(direction)
    destinaton_number = extract_destination_stack(direction)
    source_index = source_number - 1
    destination_index = destinaton_number - 1
    source_stack = current_stacks[source_index]
    destination_stack = current_stacks[destination_index]
    updated_stacks = current_stacks
    for _ in range(boxes_to_move):
        crate_to_move = source_stack.pop()
        destination_stack.append(crate_to_move)
    return updated_stacks

def move_crates_one_at_time(current_stacks, direction):
    boxes_to_move = extract_how_many_boxes_to_move(direction)
    source_number = extract_source_stack(direction)
    destinaton_number = extract_destination_stack(direction)
    source_index = source_number - 1
    destination_index = destinaton_number - 1
    source_stack = current_stacks[source_index]
    destination_stack = current_stacks[destination_index]
    updated_stacks = current_stacks
    for _ in range(boxes_to_move):
        crate_to_move = source_stack.pop()
        destination_stack.append(crate_to_move)
    return updated_stacks

def extract_how_many_boxes_to_move(direction):
    from_location = direction.find("from")
    boxes_slice = direction[5:from_location-1]
    how_many_boxes = int(boxes_slice)
    return how_many_boxes

def extract_source_stack(direction):
    from_location = direction.find("from")
    to_location = direction.find("to")
    source_slice = direction[from_location+4:to_location-1]
    source_stack = int(source_slice)
    return source_stack

def extract_destination_stack(direction):
    to_location = direction.find("to")
    destination_slice = direction[to_location+2:]
    destination_stack = int(destination_slice)
    return destination_stack

def list_all_directions(directions):
    array_directions = convert_multiline_string_to_array(directions)
    return array_directions

def determine_original_stacks(description):
    array_description = convert_multiline_string_to_array(description)
    array_description.pop()
    height = determine_tallest_original_stack(array_description)
    width = determine_how_many_stacks(array_description[0])
    list_stacks = list(range(1, width + 1))
    indices_for_stacks = []
    for stack in list_stacks:
        index = determine_index_for_stack(stack)
        indices_for_stacks.append(index)
    original_stacks = []
    for index in indices_for_stacks:
        stack = []
        reverse_rows = range(height - 1, -1, -1)
        for row in reverse_rows:
            current_row = array_description[row]
            current_stack_element = current_row[index]
            if current_stack_element != " ":
                stack.append(current_stack_element)
        original_stacks.append(stack)
    return original_stacks

def determine_how_many_stacks(line):
    line_length = len(line)
    how_many_stacks = int((line_length + 1) / 4)
    return how_many_stacks

def determine_tallest_original_stack(raw_array):
    height = len(raw_array)
    return height

def determine_index_for_stack(stack):
    index = 4 * stack - 3
    return index

def convert_multiline_string_to_array(multiline_string):
    rows = []
    while len(multiline_string):
        first_line_break = multiline_string.find("\n")
        if first_line_break != -1:
            content_before = multiline_string[0:first_line_break]
            rows.append(content_before)
            multiline_string = multiline_string[first_line_break+1:]
        else:
            rows.append(multiline_string)
            multiline_string = ""
    return rows

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem(2)
print(result)
