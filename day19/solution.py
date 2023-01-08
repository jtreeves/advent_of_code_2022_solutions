class Cost:
    def __init__(self, mineral, amount):
        self.mineral = mineral
        self.amount = amount
    
    def __repr__(self):
        return f"{self.amount} {self.mineral}"

class Robot:
    def __init__(self, description):
        self.descriptions = description.split(" costs ")
        self.type = self.extract_type()
        self.requirements = self.extract_requirements()
    
    def __repr__(self):
        description = ""
        for cost in self.requirements:
            description += f"{cost} + "
        description = description[:-2]
        description += f"-> {self.type.upper()}"
        return description

    def extract_type(self):
        type_half = self.descriptions[0]
        robot_index = type_half.index("robot") - 1
        type = type_half[5: robot_index]
        return type

    def extract_requirements(self):
        requirements_half = self.descriptions[1]
        elements = requirements_half.split(" and ")
        requirements = []
        for element in elements:
            chunks = element.split(" ")
            mineral = chunks[1].replace(".", "")
            amount = int(chunks[0])
            new_cost = Cost(mineral, amount)
            requirements.append(new_cost)
        return requirements

class Blueprint:
    def __init__(self, description):
        self.descriptions = description.split(": ")
        self.id = self.extract_id()
        self.robot_descriptions = self.descriptions[1].split(". ")
        self.robot_specs = self.determine_all_robot_specs()
    
    def __repr__(self):
        description = f"{self.id}: "
        for spec in self.robot_specs:
            description += f"{spec} // "
        description = description[:-4]
        return description

    def extract_id(self):
        id_parts = self.descriptions[0].split(" ")
        id_number = int(id_parts[1])
        return id_number
    
    def determine_all_robot_specs(self):
        specs = []
        for description in self.robot_descriptions:
            new_spec = Robot(description)
            specs.append(new_spec)
        return specs

class Selection:
    def __init__(self, description):
        self.options = description.split("\n")
        self.blueprints = self.create_blueprints()
    
    def __repr__(self):
        description = ""
        for blueprint in self.blueprints:
            description += f"{blueprint}\n"
        description = description[:-2]
        return description

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
