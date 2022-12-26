class SNAFU:
    def __init__(self, respresentation):
        self.representation = respresentation

class Bob:
    def __init__(self, directions):
        self.numbers = directions.split("\n")

def solve_problem():
    data = extract_data_from_file(25, False)
    return data

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
