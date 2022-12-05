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
    return

def determine_how_many_stacks(line):
    line_length = len(line)
    how_many_stacks = int((line_length + 1) / 4)
    return how_many_stacks

# print(extract_destination_stack("move 3 from 28 to 19"))
print(determine_how_many_stacks(" 1   2   3 "))
print(determine_how_many_stacks(" 1   2   3   4 "))
print(determine_how_many_stacks(" 1   2   3   4   5 "))
