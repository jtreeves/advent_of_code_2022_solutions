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

def determine_original_stacks(description):
    array_description = convert_multiline_string_to_array(description)
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

# print(extract_destination_stack("move 3 from 28 to 19"))
# print(determine_how_many_stacks(" 1   2   3 "))
# print(determine_how_many_stacks(" 1   2   3   4 "))
# print(determine_how_many_stacks(" 1   2   3   4   5 "))
print(determine_original_stacks("    [D]    \n[N] [C]    \n[Z] [M] [P]\n[A] [B] [C]"))
