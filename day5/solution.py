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

print(extract_destination_stack("move 3 from 28 to 19"))