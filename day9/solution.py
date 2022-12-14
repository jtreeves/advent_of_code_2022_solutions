tail_positions = set()

def add_new_tail_position(position):
    tail_positions.add(position)

def extract_data_from_file(day_number):
    file = open(f"day{day_number}/data.txt", "r")
    data = file.read()
    file.close()
    return data
