class Valve:
    def __init__(self, description):
        self.name = description[6:8]

def solve_problem():
    data = extract_data_from_file(16, False)
    lines = data.split("\n")
    first_valve = Valve(lines[0])
    return first_valve.name

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
