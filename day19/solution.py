class Blueprint:
    def __init__(self, description):
        self.description = description

class Selection:
    def __init__(self, description):
        self.options = description.split("\n")

def solve_problem():
    data = extract_data_from_file(19, False)
    selection = Selection(data)
    return selection

def extract_data_from_file(day_number, is_official):
    if is_official:
        name = "data"
    else:
        name = "practice"
    file = open(f"day{day_number}/{name}.txt", "r")
    data = file.read()
    file.close()
    return data

result = solve_problem()
print(result)
