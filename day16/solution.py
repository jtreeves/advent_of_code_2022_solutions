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
                distance[name] = 0
            else:
                distance = self.calculate_shortest_distance_to_other_valve(name, all_valves)
                distances[name] = distance
        return distances

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
            representation += "-> "
        representation[:-3]
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

class Exploration:
    def __init__(self, data):
        self.descriptions = data.split("\n")
        self.starting_valve = None
        self.valves = self.create_valves()
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

    def find_maximum_pressure(self, time_limit):
        max_pressure = 0
        valves_worth_opening = self.determine_valves_worth_opening()
        path = [self.starting_valve.name]
        pressure = 0
        time = 0
        opened_valves = set()
        initial_state = State(path, pressure, time, opened_valves)
        stack = [initial_state]
        while stack:
            print(f"***** STACK LENGTH: {len(stack)}")
            current_state = stack.pop()
            print(f"CURRENT STATE:\n{current_state}")
            max_pressure = max(max_pressure, current_state.pressure)
            print(f"/// MAX PRESSURE: {max_pressure}")
            if current_state.time == time_limit or len(current_state.opened_valves) == len(valves_worth_opening):
                continue
            else:
                for valve_to_open in valves_worth_opening:
                    if valve_to_open not in current_state.opened_valves:
                        travel_open_copy = current_state.create_divergent_copy()
                        path = travel_open_copy["path"]
                        pressure = travel_open_copy["pressure"]
                        time = travel_open_copy["time"]
                        opened_valves = travel_open_copy["opened_valves"]
                        current_valve = self.valves[path[-1]]
                        travel_time = self.find_distance_between_valves(current_valve.name, valve_to_open)
                        time_to_open_valve = 1
                        updated_time = time + travel_time + time_to_open_valve
                        updated_pressure = pressure + current_valve.calculate_current_cumulative_flow(time_limit - updated_time)
                        updated_path = path.append(valve_to_open) if current_valve.name != valve_to_open else path
                        opened_valves.add(valve_to_open)
                        updated_state = State(updated_path, updated_pressure, updated_time, opened_valves)
                        stack.append(updated_state)
        return max_pressure

def solve_problem():
    data = extract_data_from_file(16, False)
    experience = Exploration(data)
    max_pressure = experience.find_maximum_pressure(30)
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

# Idea for BFS approach from day 19 of same blog:
# https://aoc.just2good.co.uk/2022/19
