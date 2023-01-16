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
        return hash((self.name, self.flow_rate, self.tunnels))

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

class State:
    def __init__(self, current_valve, pressure, time, opened_valves):
        self.current_valve = current_valve
        self.pressure = pressure
        self.time = time
        self.opened_valves = opened_valves

    def __repr__(self):
        return f"{self.current_valve.name}: {self.pressure} psi, {self.time} min -> {self.opened_valves}"

    def __eq__(self, other):
        if isinstance(other, State):
            if self.current_location == other.current_location and self.pressure == other.pressure and self.time == other.time and self.opened_valves == other.opened_valves:
                return True
            else:
                return False
        else:
            False
    
    def __hash__(self):
        return hash((self.current_location, self.pressure, self.time, self.open_valves))

class Exploration:
    def __init__(self, data):
        self.descriptions = data.split("\n")
        self.starting_valve = None
        self.valves = self.create_valves()

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
    
    def determine_valves_worth_opening(self):
        worth_opening = []
        for valve in self.valves.values():
            if valve.flow_rate > 0:
                worth_opening.append(valve.name)
        return worth_opening
    
    def find_valve_by_name(self, name):
        try:
            valve = self.valves[name]
            return valve
        except KeyError:
            return None

    def find_maximum_pressure(self):
        max_pressure = 0
        valves_worth_opening = self.determine_valves_worth_opening()
        current_valve = self.starting_valve
        pressure = 0
        time = 0
        opened_valves = []
        initial_state = State(current_valve, pressure, time, opened_valves)
        queue = [initial_state]
        attempted_configurations = set()
        while queue and len(opened_valves) != len(valves_worth_opening):
            print(f"***** QUEUE LENGTH: {len(queue)}")
            current_state = queue.pop(0)
            print(f"CURRENT STATE:\n{current_state}")
            max_pressure = max(max_pressure, current_state.pressure)
            print(f"/// MAX PRESSURE: {max_pressure}")
            if current_state.time == 30 or current_state in attempted_configurations:
                continue
            else:
                attempted_configurations.add(current_state)
                if current_state.current_valve.flow_rate > 0 and current_state.current_valve.name not in current_state.opened_valves:
                    current_state.opened_valves.append(current_state.current_valve.name)
                    current_state.time -= 1
                    current_state.pressure += current_state.current_valve.calculate_current_cumulative_flow(30 - current_state.time)
                for tunnel in current_state.current_valve.tunnels:
                    current_state.current_valve = self.find_valve_by_name(tunnel)
                    current_state.time -= 1
                    if current_state.current_valve.flow_rate > 0 and current_state.current_valve.name not in current_state.opened_valves:
                        current_state.opened_valves.append(current_state.current_valve.name)
                        current_state.time -= 1
                        current_state.pressure += current_state.current_valve.calculate_current_cumulative_flow(30 - current_state.time)
                    new_state = State(current_state.current_valve, current_state.pressure, current_state.time, current_state.opened_valves)
                    queue.append(new_state)
        return max_pressure

def solve_problem():
    data = extract_data_from_file(16, False)
    experience = Exploration(data)
    max_pressure = experience.find_maximum_pressure()
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
