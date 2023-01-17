class Valve:
    def __init__(self, description):
        self.description = description
        self.name = self.extract_name()
        self.flow_rate = self.extract_flow_rate()
        self.tunnels = self.extract_tunnels()
    
    def __repr__(self):
        return f"{self.name}: {self.flow_rate} -> {self.tunnels}"

    def __eq__(self, other):
        if isinstance(other, Valve):
            if self.name == other.name and self.flow_rate == other.flow_rate and self.tunnels == other.tunnels:
                return True
            else:
                return False
        else:
            False
    
    def __hash__(self):
        return hash((self.name, self.flow_rate, str(self.tunnels)))

    def extract_name(self):
        name = self.description[6:8]
        return name
    
    def extract_flow_rate(self):
        index_equal = self.description.find("=")
        index_semicolon = self.description.find(";")
        flow_rate = int(self.description[index_equal + 1:index_semicolon])
        return flow_rate
    
    def extract_tunnels(self):
        partitioned_description = self.description.split(";")
        tunnels_half = partitioned_description[1]
        tunnels = tunnels_half.split(", ")
        tunnels[0] = tunnels[0][-2:]
        return tunnels
    
    def calculate_current_cumulative_flow(self, time):
        total_flow = self.flow_rate * time
        return total_flow

    def calculate_shortest_distance_to_other_valve(self, other, all_valves):
        optional_distances = []
        maximum_distance = len(all_valves.keys())
        visited_valves = set()
        queue = [(self.name, 0)]
        while queue:
            name, distance = queue.pop(0)
            if name == other:
                optional_distances.append(distance)
            elif name in visited_valves:
                continue
            elif len(optional_distances) >= maximum_distance:
                break
            else:
                visited_valves.add(name)
                current_valve = all_valves[name]
                for tunnel in current_valve.tunnels:
                    queue.append((tunnel, distance + 1))
        optional_distances.sort()
        shortest_distance = optional_distances[0]
        return shortest_distance
    
    def determine_shortest_distances_to_all_other_valves(self, all_valves):
        distances = {}
        for name in all_valves.keys():
            if name == self.name:
                distances[name] = 0
            else:
                distance = self.calculate_shortest_distance_to_other_valve(name, all_valves)
                distances[name] = distance
        return distances
    
    def find_best_next_valves(self, unopened_valves, all_valves, distances, time_remaining):
        options = []
        for valve in unopened_valves:
            full_valve = all_valves[valve]
            travel_distance = distances[valve]
            time_to_open = 1
            total_time = travel_distance + time_to_open
            time_for_pressure = time_remaining - total_time
            potential_pressure = full_valve.calculate_current_cumulative_flow(time_for_pressure)
            option = {
                "valve": valve,
                "pressure": potential_pressure,
                "time": total_time
            }
            options.append(option)
        options.sort(key=lambda d: d["pressure"])
        return options

class State:
    def __init__(self, path, pressure, time, opened_valves):
        self.path = path
        self.pressure = pressure
        self.time = time
        self.opened_valves = opened_valves

    def __repr__(self):
        representation = ""
        for valve in self.path:
            representation += f"{valve}"
            if valve in self.opened_valves:
                representation += "*"
            representation += " -> "
        representation = representation[:-4]
        representation += f": {self.pressure} psi, {self.time} min"
        return representation

    def __eq__(self, other):
        if isinstance(other, State):
            if self.path == other.path and self.pressure == other.pressure and self.time == other.time and self.opened_valves == other.opened_valves:
                return True
            else:
                return False
        else:
            False
    
    def __hash__(self):
        return hash((self.path, self.pressure, self.time, str(self.opened_valves)))
    
    def create_divergent_copy(self):
        path = [x for x in self.path]
        pressure = self.pressure
        time = self.time
        opened_valves = set([x for x in self.opened_valves])
        divergent_copy = {
            "path": path,
            "pressure": pressure,
            "time": time,
            "opened_valves": opened_valves
        }
        return divergent_copy

class TandemState:
    def __init__(self, main_state, helper_state):
        self.main_state = main_state
        self.helper_state = helper_state
        self.pressure = self.calculate_total_pressure()
        self.opened_valves = self.determine_all_opened_valves()
        self.maximum_time = self.determine_maximum_time()

    def __repr__(self):
        return f"{self.main_state.path}; {self.helper_state.path}: {self.pressure} psi, {self.maximum_time} min"

    def __eq__(self, other):
        if isinstance(other, TandemState):
            if self.main_state == other.main_state and self.helper_state == other.helper_state:
                return True
            else:
                return False
        else:
            False
    
    def calculate_total_pressure(self):
        return self.main_state.pressure + self.helper_state.pressure
    
    def determine_all_opened_valves(self):
        return self.main_state.opened_valves.union(self.helper_state.opened_valves)
    
    def determine_maximum_time(self):
        return max(self.main_state.time, self.helper_state.time)
    
    def __hash__(self):
        return hash((self.main_state, self.helper_state))

class Exploration:
    def __init__(self, data):
        self.descriptions = data.split("\n")
        self.starting_valve = None
        self.valves = self.create_valves()
        self.valves_worth_opening = self.determine_valves_worth_opening()
        self.distances = self.create_distances_hash_table()

    def __repr__(self):
        return f"{self.valves}"
    
    def create_valves(self):
        valves = {}
        for description in self.descriptions:
            new_valve = Valve(description)
            valves[new_valve.name] = new_valve
            if new_valve.name == "AA":
                self.starting_valve = new_valve
        return valves
    
    def create_distances_hash_table(self):
        all_distances = {}
        for key, value in self.valves.items():
            distances = value.determine_shortest_distances_to_all_other_valves(self.valves)
            all_distances[key] = distances
        return all_distances
    
    def find_distance_between_valves(self, first_valve, second_valve):
        return self.distances[first_valve][second_valve]
    
    def determine_valves_worth_opening(self):
        worth_opening = []
        for valve in self.valves.values():
            if valve.flow_rate > 0:
                worth_opening.append(valve.name)
        return worth_opening
    
    def determine_unopened_valves_worth_opening(self, opened_valves):
        unopened_worth_opening = []
        for valve in self.valves_worth_opening:
            if valve not in opened_valves:
                unopened_worth_opening.append(valve)
        return unopened_worth_opening

    def find_maximum_pressure(self, time_limit):
        max_pressure = 0
        path = [self.starting_valve.name]
        pressure = 0
        time = 0
        opened_valves = set()
        initial_state = State(path, pressure, time, opened_valves)
        stack = [initial_state]
        while stack:
            current_state = stack.pop()
            max_pressure = max(max_pressure, current_state.pressure)
            if current_state.time >= time_limit or len(current_state.opened_valves) == len(self.valves_worth_opening):
                continue
            else:
                current_name = current_state.path[-1]
                current_valve = self.valves[current_name]
                opened_valves = current_state.opened_valves
                unopened_valves = self.determine_unopened_valves_worth_opening(opened_valves)
                current_time = current_state.time
                valve_distances = self.distances[current_name]
                time_remaining = time_limit - current_time
                options = current_valve.find_best_next_valves(unopened_valves, self.valves, valve_distances, time_remaining)
                for option in options:
                    travel_open_copy = current_state.create_divergent_copy()
                    path = travel_open_copy["path"]
                    pressure = travel_open_copy["pressure"]
                    time = travel_open_copy["time"]
                    opened_valves = travel_open_copy["opened_valves"]
                    option_valve = option["valve"]
                    option_pressure = option["pressure"]
                    option_time = option["time"]
                    updated_time = time + option_time
                    updated_pressure = pressure + option_pressure
                    if option_valve != current_name:
                        path.append(option_valve)
                    opened_valves.add(option_valve)
                    updated_state = State(path, updated_pressure, updated_time, opened_valves)
                    stack.append(updated_state)
        return max_pressure

    def find_maximum_pressure_with_help(self, time_limit):
        max_pressure = 0
        path = [self.starting_valve.name]
        pressure = 0
        time = 0
        opened_valves = set()
        initial_state = State(path, pressure, time, opened_valves)
        conjoined_state = TandemState(initial_state, initial_state)
        stack = [conjoined_state]
        while stack:
            print(f"***** STACK LENGTH: {len(stack)}")
            current_state = stack.pop()
            print(f"CURRENT STATE:\n{current_state}")
            max_pressure = max(max_pressure, current_state.pressure)
            print(f"/// MAX PRESSURE: {max_pressure}")
            if (current_state.main_state.time >= time_limit and current_state.helper_state.time >= time_limit) or len(current_state.opened_valves) == len(self.valves_worth_opening):
                continue
            else:
                main_name = current_state.main_state.path[-1]
                helper_name = current_state.helper_state.path[-1]
                main_valve = self.valves[main_name]
                helper_valve = self.valves[helper_name]
                main_distances = self.distances[main_name]
                helper_distances = self.distances[helper_name]
                main_time = current_state.main_state.time
                helper_time = current_state.helper_state.time
                opened_valves = current_state.opened_valves
                unopened_valves = self.determine_unopened_valves_worth_opening(opened_valves)
                main_time_remaining = time_limit - main_time
                helper_time_remaining = time_limit - helper_time
                main_options = main_valve.find_best_next_valves(unopened_valves, self.valves, main_distances, main_time_remaining)
                helper_options = helper_valve.find_best_next_valves(unopened_valves, self.valves, helper_distances, helper_time_remaining)
                for main_option in main_options:
                    for helper_option in helper_options:
                        if main_option["valve"] != helper_option["valve"]:
                            main_option_valve = main_option["valve"]
                            helper_option_valve = helper_option["valve"]
                            main_option_pressure = main_option["pressure"]
                            helper_option_pressure = helper_option["pressure"]
                            main_option_time = main_option["time"]
                            helper_option_time = helper_option["time"]
                            main_copy = current_state.main_state.create_divergent_copy()
                            helper_copy = current_state.helper_state.create_divergent_copy()
                            main_path = main_copy["path"]
                            helper_path = helper_copy["path"]
                            main_pressure = main_copy["pressure"]
                            helper_pressure = helper_copy["pressure"]
                            main_time = main_copy["time"]
                            helper_time = helper_copy["time"]
                            main_opened_valves = main_copy["opened_valves"]
                            helper_opened_valves = helper_copy["opened_valves"]
                            updated_main_time = main_time + main_option_time
                            updated_helper_time = helper_time + helper_option_time
                            updated_main_pressure = main_pressure + main_option_pressure
                            updated_helper_pressure = helper_pressure + helper_option_pressure
                            if main_option_valve != main_name:
                                main_path.append(main_option_valve)
                            if helper_option_valve != helper_name:
                                helper_path.append(helper_option_valve)
                            main_opened_valves.add(main_option_valve)
                            helper_opened_valves.add(helper_option_valve)
                            main_state = State(main_path, updated_main_pressure, updated_main_time, opened_valves)
                            helper_state = State(helper_path, updated_helper_pressure, updated_helper_time, opened_valves)
                            updated_tandem = TandemState(main_state, helper_state)
                            stack.append(updated_tandem)
        return max_pressure

def solve_problem():
    data = extract_data_from_file(16, False)
    experience = Exploration(data)
    max_pressure = experience.find_maximum_pressure_with_help(26)
    return max_pressure

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

# Idea for DFS approach:
# https://github.com/ChrisWojcik/advent-of-code-2022/blob/main/16/1.py
