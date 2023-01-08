class Blueprint:
    def __init__(self, description):
        self.descriptions = description.split(": ")
        self.id = self.extract_id()
    
    def __repr__(self):
        return f"{self.id}"

    def extract_id(self):
        id_parts = self.descriptions[0].split(" ")
        id_number = int(id_parts[1])
        return id_number

class Selection:
    def __init__(self, description):
        self.options = description.split("\n")
        self.blueprints = self.create_blueprints()
    
    def __repr__(self):
        return f"{self.blueprints}"

    def create_blueprints(self):
        blueprints = []
        for option in self.options:
            new_blueprint = Blueprint(option)
            blueprints.append(new_blueprint)
        return blueprints

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
