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
        self.ore_robots = 1
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geodes = 0
    
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
    
    def check_if_can_make_geode_robot(self):
        geode_requirements = self.robot_specs[3].requirements
        ore_needed = geode_requirements[0].amount
        obsidian_needed = geode_requirements[1].amount
        if self.ore >= ore_needed and self.obsidian >= obsidian_needed:
            return True
        else:
            return False
    
    def check_if_can_make_obsidian_robot(self):
        obsidian_requirements = self.robot_specs[2].requirements
        ore_needed = obsidian_requirements[0].amount
        clay_needed = obsidian_requirements[1].amount
        if self.ore >= ore_needed and self.clay >= clay_needed:
            return True
        else:
            return False
    
    def check_if_can_make_clay_robot(self):
        clay_requirements = self.robot_specs[1].requirements
        ore_needed = clay_requirements[0].amount
        if self.ore >= ore_needed:
            return True
        else:
            return False
        
    def spend_one_minute(self):
        can_geode = self.check_if_can_make_geode_robot()
        can_obsidian = self.check_if_can_make_obsidian_robot()
        can_clay = self.check_if_can_make_clay_robot()
        if can_geode:
            geode_requirements = self.robot_specs[3].requirements
            ore_needed = geode_requirements[0].amount
            obsidian_needed = geode_requirements[1].amount
            self.ore -= ore_needed
            self.obsidian -= obsidian_needed
        elif can_obsidian:
            obsidian_requirements = self.robot_specs[2].requirements
            ore_needed = obsidian_requirements[0].amount
            clay_needed = obsidian_requirements[1].amount
            self.ore -= ore_needed
            self.clay -= clay_needed
        elif can_clay:
            clay_requirements = self.robot_specs[1].requirements
            ore_needed = clay_requirements[0].amount
            self.ore -= ore_needed
        for _ in range(self.ore_robots):
            self.ore += 1
        for _ in range(self.clay_robots):
            self.clay += 1
        for _ in range(self.obsidian_robots):
            self.obsidian += 1
        for _ in range(self.geode_robots):
            self.geodes += 1
        if can_geode:
            self.geode_robots += 1
        elif can_obsidian:
            self.obsidian_robots += 1
        elif can_clay:
            self.clay_robots += 1

    def spend_multiple_minutes(self, minutes):
        for _ in range(minutes):
            print("////////")
            print(f"MINUTE: {_ + 1}")
            self.spend_one_minute()
            print(f"ORE: {self.ore}")
            print(f"CLAY: {self.clay}")
            print(f"OBSIDIAN: {self.obsidian}")
            print(f"GEODES: {self.geodes}")

class Selection:
    def __init__(self, description):
        self.options = description.split("\n")
        self.blueprints = self.create_blueprints()
    
    def __repr__(self):
        description = ""
        for blueprint in self.blueprints:
            description += f"{blueprint}\n"
        description = description[:-1]
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
    selection.blueprints[0].spend_multiple_minutes(24)
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
