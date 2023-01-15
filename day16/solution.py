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
        self.starting_valve = ""
        self.valves = self.create_valves()

    def __repr__(self):
        return f"{self.valves}"
    
    def create_valves(self):
        valves = {}
        for i in range(len(self.descriptions)):
            new_valve = Valve(self.descriptions[i])
            valves[new_valve.name] = new_valve
            if i == 0:
                self.starting_valve = new_valve.name
        return valves
    
    def find_valve_by_name(self, name):
        try:
            valve = self.valves[name]
            return valve
        except KeyError:
            return None

    def find_maximum_pressure(self):
        starting_pressure = 0
        time_remaining = 30
        visited_valves = set()
        queue = [(self.starting_valve, starting_pressure, time_remaining)]
        maximal_pressures = []
        while queue:
            name, pressure, time = queue.pop(0)
            if time == 0:
                break
            elif name in visited_valves:
                continue
            else:
                visited_valves.add(name)
                valve = self.find_valve_by_name(name)
                if valve.flow_rate > 0:
                    time -= 1
                    pressure += valve.calculate_current_cumulative_flow(time)
                for tunnel in valve.tunnels:
                    time -= 1
                    queue.append((tunnel, pressure, time))
                    maximal_pressures.append(pressure)
        return max(maximal_pressures)
        
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
