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

    def sort_queue_by_geodes(self, queue):
        sorted_queue = sorted(queue, key=lambda x: (-x.geode_robots, -x.geodes, x.time))
        return sorted_queue

    def eliminate_state_lacking_geode_robots_from_queue(self, queue, time):
        filtered_queue = [x for x in queue if x.geode_robots != 0 or x.time >= time]
        return filtered_queue

    def eliminate_state_lacking_sufficient_geodes_from_queue(self, queue, maximum, time):
        filtered_queue = [x for x in queue if x.geodes >= maximum // 4 or x.time >= time]
        return filtered_queue

    def find_max_ore_cost(self):
        ore_for_ore = self.robot_specs[0].requirements[0].amount
        ore_for_clay = self.robot_specs[1].requirements[0].amount
        ore_for_obsidian = self.robot_specs[2].requirements[0].amount
        ore_for_geode = self.robot_specs[3].requirements[0].amount
        ore_options = [
            ore_for_ore,
            ore_for_clay,
            ore_for_obsidian,
            ore_for_geode
        ]
        ore_options.sort()
        return ore_options[-1]

    def find_max_clay_cost(self):
        clay_for_obsidian = self.robot_specs[2].requirements[1].amount
        return clay_for_obsidian

    def find_max_obsidian_cost(self):
        obsidian_for_geode = self.robot_specs[3].requirements[1].amount
        return obsidian_for_geode
    
    def optimize_geodes(self, minutes):
        most_geodes = 0
        initial_state = State(minutes, 0, 0, 0, 0, 1, 0, 0, 0)
        queue = [initial_state]
        tried_options = set()
        max_ore_cost = self.find_max_ore_cost()
        max_clay_cost = self.find_max_clay_cost()
        max_obsidian_cost = self.find_max_obsidian_cost()
        while queue:
            print(f"///// LENGTH OF QUEUE: {len(queue)}")
            if most_geodes > 0:
                queue = self.sort_queue_by_geodes(queue)
            current_state = queue.pop(0)
            if current_state.time < 5 and most_geodes > 10:
                queue = self.eliminate_state_lacking_sufficient_geodes_from_queue(queue, most_geodes, current_state.time)
            if current_state.time < 3:
                queue = self.eliminate_state_lacking_geode_robots_from_queue(queue, current_state.time)
            most_geodes = max(most_geodes, current_state.geodes)
            optimized_ore_robots = min(current_state.ore_robots, max_ore_cost)
            optimized_clay_robots = min(current_state.clay_robots, max_clay_cost)
            optimized_obsidian_robots = min(current_state.obsidian_robots, max_obsidian_cost)
            optimized_ore = min(current_state.ore, current_state.time * max_ore_cost - optimized_ore_robots * (current_state.time - 1))
            optimized_clay = min(current_state.clay, current_state.time * max_clay_cost - optimized_clay_robots * (current_state.time - 1))
            optimized_obsidian = min(current_state.obsidian, current_state.time * max_obsidian_cost - optimized_obsidian_robots * (current_state.time - 1))
            optimized_state = State(current_state.time, optimized_ore, optimized_clay, optimized_obsidian, current_state.geodes, optimized_ore_robots, optimized_clay_robots, optimized_obsidian_robots, current_state.geode_robots)
            if optimized_state.time == 0 or optimized_state in tried_options:
                continue
            else:
                print(f"*** ID: {self.id}")
                print(optimized_state)
                print(f"MOST GEODES: {most_geodes}")
                tried_options.add(optimized_state)
                new_state = State(optimized_state.time - 1, optimized_state.ore + optimized_state.ore_robots, optimized_state.clay + optimized_state.clay_robots, optimized_state.obsidian + optimized_state.obsidian_robots, optimized_state.geodes + optimized_state.geode_robots, optimized_state.ore_robots, optimized_state.clay_robots, optimized_state.obsidian_robots, optimized_state.geode_robots)
                # if (most_geodes >= 10 and new_state.geodes >= most_geodes // 2) or (new_state.time >= 3 and new_state.geodes >= most_geodes // 2):
                queue.append(new_state)
                if optimized_state.ore >= self.robot_specs[0].requirements[0].amount:
                    ore_state = State(optimized_state.time - 1, optimized_state.ore + optimized_state.ore_robots - self.robot_specs[0].requirements[0].amount, optimized_state.clay + optimized_state.clay_robots, optimized_state.obsidian + optimized_state.obsidian_robots, optimized_state.geodes + optimized_state.geode_robots, optimized_state.ore_robots + 1, optimized_state.clay_robots, optimized_state.obsidian_robots, optimized_state.geode_robots)
                    # if (most_geodes >= 10 and ore_state.geodes >= most_geodes // 2) or (ore_state.time >= 3 and ore_state.geodes >= most_geodes // 2):
                    queue.append(ore_state)
                if optimized_state.ore >= self.robot_specs[1].requirements[0].amount:
                    clay_state = State(optimized_state.time - 1, optimized_state.ore + optimized_state.ore_robots - self.robot_specs[1].requirements[0].amount, optimized_state.clay + optimized_state.clay_robots, optimized_state.obsidian + optimized_state.obsidian_robots, optimized_state.geodes + optimized_state.geode_robots, optimized_state.ore_robots, optimized_state.clay_robots + 1, optimized_state.obsidian_robots, optimized_state.geode_robots)
                    # if (most_geodes >= 10 and clay_state.geodes >= most_geodes // 2) or (clay_state.time >= 3 and clay_state.geodes >= most_geodes // 2):
                    queue.append(clay_state)
                if optimized_state.ore >= self.robot_specs[2].requirements[0].amount and optimized_state.clay >= self.robot_specs[2].requirements[1].amount:
                    obsidian_state = State(optimized_state.time - 1, optimized_state.ore + optimized_state.ore_robots - self.robot_specs[2].requirements[0].amount, optimized_state.clay + optimized_state.clay_robots - self.robot_specs[2].requirements[1].amount, optimized_state.obsidian + optimized_state.obsidian_robots, optimized_state.geodes + optimized_state.geode_robots, optimized_state.ore_robots, optimized_state.clay_robots, optimized_state.obsidian_robots + 1, optimized_state.geode_robots)
                    # if (most_geodes >= 10 and obsidian_state.geodes >= most_geodes // 2) or (obsidian_state.time >= 3 and obsidian_state.geodes >= most_geodes // 2):
                    queue.append(obsidian_state)
                if optimized_state.ore >= self.robot_specs[3].requirements[0].amount and optimized_state.obsidian >= self.robot_specs[3].requirements[1].amount:
                    geode_state = State(optimized_state.time - 1, optimized_state.ore + optimized_state.ore_robots - self.robot_specs[3].requirements[0].amount, optimized_state.clay + optimized_state.clay_robots, optimized_state.obsidian + optimized_state.obsidian_robots - self.robot_specs[3].requirements[1].amount, optimized_state.geodes + optimized_state.geode_robots, optimized_state.ore_robots, optimized_state.clay_robots, optimized_state.obsidian_robots, optimized_state.geode_robots + 1)
                    # if (most_geodes >= 10 and geode_state.geodes >= most_geodes // 2) or (geode_state.time >= 3 and geode_state.geodes >= most_geodes // 2):
                    queue.append(geode_state)
        return most_geodes
    
    def calculate_quality_level_for_interval(self, minutes):
        max_geodes = self.optimize_geodes(minutes)
        id_number = self.id
        level = id_number * max_geodes
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

    def __repr__(self):
        return f"TIME REMAINING: {self.time}\nORE: {self.ore_robots} -> {self.ore}\nCLAY: {self.clay_robots} -> {self.clay}\nOBSIDIAN: {self.obsidian_robots} -> {self.obsidian}\nGEODES: {self.geode_robots} -> {self.geodes}"

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
    
    def calculate_product_of_geodes_from_first_three_blueprints(self, minutes):
        product = 1
        for blueprint in self.blueprints[0:3]:
            geodes = blueprint.optimize_geodes(minutes)
            product *= geodes
        return product

def solve_problem():
    data = extract_data_from_file(19, True)
    selection = Selection(data)
    total = selection.calculate_product_of_geodes_from_first_three_blueprints(32)
    # total = selection.calculate_sum_of_quality_levels_on_interval(24)
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

# Idea for BFS approach and attendant optimizations:
# https://aoc.just2good.co.uk/2022/19
