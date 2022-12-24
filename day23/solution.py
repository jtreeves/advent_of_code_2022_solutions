class CoordinatePair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.proposed_x = None
        self.proposed_y = None
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def check_if_direct_north_occupied(self, other_points):
        for other_point in other_points:
            if self.x == other_point.x and self.y + 1 == other_point.y:
                return True
            else:
                return False

    def check_if_direct_south_occupied(self, other_points):
        for other_point in other_points:
            if self.x == other_point.x and self.y - 1 == other_point.y:
                return True
            else:
                return False

    def check_if_direct_east_occupied(self, other_points):
        for other_point in other_points:
            if self.x + 1 == other_point.x and self.y == other_point.y:
                return True
            else:
                return False

    def check_if_direct_west_occupied(self, other_points):
        for other_point in other_points:
            if self.x - 1 == other_point.x and self.y == other_point.y:
                return True
            else:
                return False

    def check_if_northeast_occupied(self, other_points):
        for other_point in other_points:
            if self.x + 1 == other_point.x and self.y + 1 == other_point.y:
                return True
            else:
                return False

    def check_if_northwest_occupied(self, other_points):
        for other_point in other_points:
            if self.x - 1 == other_point.x and self.y + 1 == other_point.y:
                return True
            else:
                return False

    def check_if_southeast_occupied(self, other_points):
        for other_point in other_points:
            if self.x + 1 == other_point.x and self.y - 1 == other_point.y:
                return True
            else:
                return False

    def check_if_southwest_occupied(self, other_points):
        for other_point in other_points:
            if self.x - 1 == other_point.x and self.y - 1 == other_point.y:
                return True
            else:
                return False

    def check_if_any_north_occupied(self, other_points):
        direct_north = self.check_if_direct_north_occupied(other_points)
        northwest = self.check_if_northwest_occupied(other_points)
        northeast = self.check_if_northeast_occupied(other_points)
        if not direct_north and not northwest and not northeast:
            return True
        else:
            return False

    def check_if_any_south_occupied(self, other_points):
        direct_south = self.check_if_direct_south_occupied(other_points)
        southwest = self.check_if_southwest_occupied(other_points)
        southeast = self.check_if_southeast_occupied(other_points)
        if not direct_south and not southwest and not southeast:
            return True
        else:
            return False

    def check_if_any_east_occupied(self, other_points):
        direct_east = self.check_if_direct_east_occupied(other_points)
        southeast = self.check_if_southeast_occupied(other_points)
        northeast = self.check_if_northeast_occupied(other_points)
        if not direct_east and not northeast and not southeast:
            return True
        else:
            return False

    def check_if_any_west_occupied(self, other_points):
        direct_west = self.check_if_direct_west_occupied(other_points)
        southwest = self.check_if_southwest_occupied(other_points)
        northwest = self.check_if_northwest_occupied(other_points)
        if not direct_west and not northwest and not southwest:
            return True
        else:
            return False

    def check_if_proposed_location_already_proposed(self, other_points):
        for other_point in other_points:
            if self.proposed_x == other_point.proposed_x and self.proposed_y == other_point.proposed_y:
                return True
            else:
                return False

    def find_new_location_to_propose(self, round, other_points):
        step = round % 4
        if step == 1:
            north = self.check_if_any_north_occupied(other_points)
            if north:
                self.propose_new_location(self.x, self.y + 1)
            else:
                south = self.check_if_any_south_occupied(other_points)
                if south:
                    self.propose_new_location(self.x, self.y - 1)
                else:
                    west = self.check_if_any_west_occupied(other_points)
                    if west:
                        self.propose_new_location(self.x - 1, self.y)
                    else:
                        east = self.check_if_any_east_occupied(other_points)
                        if east:
                            self.propose_new_location(self.x + 1, self.y)
        elif step == 2:
            south = self.check_if_any_south_occupied(other_points)
            if south:
                self.propose_new_location(self.x, self.y - 1)
            else:
                west = self.check_if_any_west_occupied(other_points)
                if west:
                    self.propose_new_location(self.x - 1, self.y)
                else:
                    east = self.check_if_any_east_occupied(other_points)
                    if east:
                        self.propose_new_location(self.x + 1, self.y)
                    else:
                        north = self.check_if_any_north_occupied(other_points)
                        if north:
                            self.propose_new_location(self.x, self.y + 1)
        elif step == 3:
            west = self.check_if_any_west_occupied(other_points)
            if west:
                self.propose_new_location(self.x - 1, self.y)
            else:
                east = self.check_if_any_east_occupied(other_points)
                if east:
                    self.propose_new_location(self.x + 1, self.y)
                else:
                    north = self.check_if_any_north_occupied(other_points)
                    if north:
                        self.propose_new_location(self.x, self.y + 1)
                    else:
                        south = self.check_if_any_south_occupied(other_points)
                        if south:
                            self.propose_new_location(self.x, self.y - 1)
        else:
            east = self.check_if_any_east_occupied(other_points)
            if east:
                self.propose_new_location(self.x + 1, self.y)
            else:
                north = self.check_if_any_north_occupied(other_points)
                if north:
                    self.propose_new_location(self.x, self.y + 1)
                else:
                    south = self.check_if_any_south_occupied(other_points)
                    if south:
                        self.propose_new_location(self.x, self.y - 1)
                    else:
                        west = self.check_if_any_west_occupied(other_points)
                        if west:
                            self.propose_new_location(self.x - 1, self.y)

    def propose_new_location(self, new_x, new_y):
        self.proposed_x = new_x
        self.proposed_y = new_y

    def move_to_new_location(self):
        self.x = self.proposed_x
        self.y = self.proposed_y

class Grid:
    def __init__(self, description):
        self.lines = description.split("\n")
        self.round = 1
        self.original_height = len(self.lines)
        self.original_width = len(self.lines[0])
        self.pairs = self.create_pairs()
    
    def create_pairs(self):
        pairs = []
        for row in range(self.original_height):
            for column in range(self.original_width):
                if self.lines[row][column] == "#":
                    new_pair = CoordinatePair(column, row)
                    pairs.append(new_pair)
        return pairs
    
    def increment_round(self):
        self.round += 1

def solve_problem():
    data = extract_data_from_file(23, False)
    grid = Grid(data)
    return grid.pairs

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
