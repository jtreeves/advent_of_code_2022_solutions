class Valve:
    def __init__(self, description):
        self.description = description
        self.name = self.extract_name()
        self.flow_rate = self.extract_flow_rate()
        self.tunnels = self.extract_tunnels()
    
    def __repr__(self):
        return f"{self.name}: {self.flow_rate} -> {self.tunnels}"
    
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

class Exploration:
    def __init__(self, data):
        self.descriptions = data.split("\n")
        self.valves = self.create_valves()

    def __repr__(self):
        return f"{self.valves}"
    
    def create_valves(self):
        valves = {}
        for i in range(len(self.descriptions)):
            new_valve = Valve(self.descriptions[i])
            valves[new_valve.name] = new_valve
            if i == 0:
                self.starting_valve = new_valve
        return valves
    
    def determine_all_valves_worth_opening(self):
        worth_opening = []
        for valve in self.valves.values():
            if valve.flow_rate > 0:
                worth_opening.append(valve.name)
        return worth_opening

    def find_maximum_pressure(self):
        unopened_valves_worth_opening = self.determine_all_valves_worth_opening()
        remaining_time = 30
        maximum_pressure = 0
        current_valve = self.starting_valve
        while len(unopened_valves_worth_opening) != 0 and remaining_time > 0:
            pass
        return maximum_pressure

def solve_problem():
    data = extract_data_from_file(16, False)
    experience = Exploration(data)
    return experience

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
