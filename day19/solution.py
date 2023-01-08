class Blueprint:
    def __init__(self, description):
        self.descriptions = description.split(": ")
        self.robot_descriptions = self.descriptions[1].split(". ")
        self.id = self.extract_id()
        self.ore_cost = self.extract_cost_ore_robot()
        self.clay_cost = self.extract_cost_clay_robot()
    
    def __repr__(self):
        return f"{self.id}: {self.ore_cost} ore -> ORE"

    def extract_id(self):
        id_parts = self.descriptions[0].split(" ")
        id_number = int(id_parts[1])
        return id_number
    
    def extract_cost_ore_robot(self):
        ore_descriptions = self.robot_descriptions[0].split("costs ")
        ore_cost = int(ore_descriptions[1].split(" ")[0])
        return ore_cost
    
    def extract_cost_clay_robot(self):
        clay_descriptions = self.robot_descriptions[1].split("costs ")
        clay_cost = int(clay_descriptions[1].split(" ")[0])
        return clay_cost

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
