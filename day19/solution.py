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
    
    def optimize_geodes(self):
        most_geodes = 0
        initial_state = State(24, 0, 0, 0, 0, 1, 0, 0, 0)
        queue = [initial_state]
        tried_options = set()
        while queue:
            current_state = queue.pop(0)
            most_geodes = max(most_geodes, current_state.geodes)
            if current_state.time == 0 or current_state in tried_options:
                continue
            else:
                tried_options.add(current_state)
                new_state = State(current_state.time - 1, current_state.ore + current_state.ore_robots, current_state.clay + current_state.clay_robots, current_state.obsidian + current_state.obsidian_robots, current_state.geodes + current_state.geode_robots, current_state.ore_robots, current_state.clay_robots, current_state.obsidian_robots, current_state.geode_robots)
                queue.append(new_state)
                if current_state.ore >= self.robot_specs[0].requirements[0].amount:
                    ore_state = State(current_state.time - 1, current_state.ore + current_state.ore_robots - self.robot_specs[0].requirements[0].amount, current_state.clay + current_state.clay_robots, current_state.obsidian + current_state.obsidian_robots, current_state.geodes + current_state.geode_robots, current_state.ore_robots, current_state.clay_robots, current_state.obsidian_robots, current_state.geode_robots)
                    queue.append(ore_state)
                if current_state.ore >= self.robot_specs[1].requirements[0].amount:
                    clay_state = State(current_state.time - 1, current_state.ore + current_state.ore_robots - self.robot_specs[1].requirements[0].amount, current_state.clay + current_state.clay_robots, current_state.obsidian + current_state.obsidian_robots, current_state.geodes + current_state.geode_robots, current_state.ore_robots, current_state.clay_robots, current_state.obsidian_robots, current_state.geode_robots)
                    queue.append(clay_state)
                if current_state.ore >= self.robot_specs[2].requirements[0].amount and current_state.clay >= self.robot_specs[2].requirements[1].amount:
                    obsidian_state = State(current_state.time - 1, current_state.ore + current_state.ore_robots - self.robot_specs[2].requirements[0].amount, current_state.clay + current_state.clay_robots - self.robot_specs[2].requirements[1].amount, current_state.obsidian + current_state.obsidian_robots, current_state.geodes + current_state.geode_robots, current_state.ore_robots, current_state.clay_robots, current_state.obsidian_robots, current_state.geode_robots)
                    queue.append(obsidian_state)
                if current_state.ore >= self.robot_specs[3].requirements[0].amount and current_state.obsidian >= self.robot_specs[3].requirements[1].amount:
                    obsidian_state = State(current_state.time - 1, current_state.ore + current_state.ore_robots - self.robot_specs[3].requirements[0].amount, current_state.clay + current_state.clay_robots, current_state.obsidian + current_state.obsidian_robots - self.robot_specs[3].requirements[1].amount, current_state.geodes + current_state.geode_robots, current_state.ore_robots, current_state.clay_robots, current_state.obsidian_robots, current_state.geode_robots)
                    queue.append(obsidian_state)
        return most_geodes
        
    def spend_one_minute(self):
        geode_requirements = self.robot_specs[3].requirements
        ore_needed_for_geode = geode_requirements[0].amount
        obsidian_needed_for_geode = geode_requirements[1].amount
        obsidian_requirements = self.robot_specs[2].requirements
        ore_needed_for_obsidian = obsidian_requirements[0].amount
        clay_needed_for_obsidian = obsidian_requirements[1].amount
        clay_requirements = self.robot_specs[1].requirements
        ore_needed_for_clay = clay_requirements[0].amount
        ore_requirements = self.robot_specs[0].requirements
        ore_needed_for_ore = ore_requirements[0].amount
        should_geode = self.ore >= ore_needed_for_geode and self.obsidian >= obsidian_needed_for_geode
        should_obsidian = self.ore >= ore_needed_for_obsidian and self.clay >= clay_needed_for_obsidian and self.obsidian + self.obsidian_robots * 2 < obsidian_needed_for_geode
        should_clay = self.ore >= ore_needed_for_clay and self.clay + self.clay_robots * 2 < clay_needed_for_obsidian
        should_ore = self.ore >= ore_needed_for_ore and self.ore + self.ore_robots * 2 < ore_needed_for_clay
        if should_geode:
            self.ore -= ore_needed_for_geode
            self.obsidian -= obsidian_needed_for_geode
        elif should_obsidian:
            self.ore -= ore_needed_for_obsidian
            self.clay -= clay_needed_for_obsidian
        elif should_clay:
            self.ore -= ore_needed_for_clay
        elif should_ore:
            self.ore -= ore_needed_for_ore
        for _ in range(self.ore_robots):
            self.ore += 1
        for _ in range(self.clay_robots):
            self.clay += 1
        for _ in range(self.obsidian_robots):
            self.obsidian += 1
        for _ in range(self.geode_robots):
            self.geodes += 1
        if should_geode:
            self.geode_robots += 1
        elif should_obsidian:
            self.obsidian_robots += 1
        elif should_clay:
            self.clay_robots += 1
        elif should_ore:
            self.ore_robots += 1

    def spend_multiple_minutes(self, minutes):
        for _ in range(minutes):
            print("////////")
            print(f"MINUTE: {_ + 1}")
            self.spend_one_minute()
            print(f"ORE: {self.ore}")
            print(f"CLAY: {self.clay}")
            print(f"OBSIDIAN: {self.obsidian}")
            print(f"GEODES: {self.geodes}")
            print("*********")
            print(f"ORE ROBOTS: {self.ore_robots}")
            print(f"CLAY ROBOTS: {self.clay_robots}")
            print(f"OBSIDIAN ROBOTS: {self.obsidian_robots}")
            print(f"GEODE ROBOTS: {self.geode_robots}")
    
    def calculate_quality_level_for_interval(self, minutes):
        self.spend_multiple_minutes(minutes)
        id_number = self.id
        geodes = self.geodes
        level = id_number * geodes
        return level

class State:
    def __init__(self, time, ore, clay, obsidian, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots):
        self.time = time
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geodes = geodes
        self.ore_robots = ore_robots
        self.clay_robots = clay_robots
        self.obsidian_robots = obsidian_robots
        self.geode_robots = geode_robots

    def __eq__(self, other):
        if self.time == other.time and self.ore == other.ore and self.clay == other.clay and self.obsidian == other.obsidian and self.geodes == other.geodes and self.ore_robots == other.ore_robots and self.clay_robots == other.clay_robots and self.obsidian_robots == other.obsidian_robots and self.geode_robots == other.geode_robots:
            return True
        else:
            return False
    
    def __hash__(self):
        return hash((self.time, self.ore, self.clay, self.obsidian, self.geodes, self.ore_robots, self.clay_robots, self.obsidian_robots, self.geode_robots))

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

    def calculate_sum_of_quality_levels_on_interval(self, minutes):
        total = 0
        for blueprint in self.blueprints:
            level = blueprint.calculate_quality_level_for_interval(minutes)
            total += level
        return total

def solve_problem():
    data = extract_data_from_file(19, True)
    selection = Selection(data)
    total = selection.calculate_sum_of_quality_levels_on_interval(24)
    return total

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
