import copy

class SNAFU:
    def __init__(self, respresentation):
        self.digits = respresentation.split("")
        self.backwards_digits = copy.deepcopy(self.digits)
        self.backwards_digits.reverse()
        self.places = len(self.digits)
    
    def convert_to_decimal(self):
        total = 0
        for i in range(len(self.backwards_digits)):
            multiplier = 5 ** i
            value = SNAFU.determine_value_of_digit(self.backwards_digits[i])
            product = multiplier * value
            total += product
        return total
    
    @staticmethod
    def determine_value_of_digit(digit):
        if digit == "2":
            return 2
        elif digit == "1":
            return 1
        elif digit == "0":
            return 0
        elif digit == "-":
            return -1
        elif digit == "=":
            return -2

class Bob:
    def __init__(self, directions):
        self.representations = directions.split("\n")
        self.snafu_numbers = self.create_snafu_numbers()
    
    def create_snafu_numbers(self):
        snafu_numbers = []
        for representation in self.representations:
            new_snafu = SNAFU(representation)
            snafu_numbers.append(new_snafu)
        return snafu_numbers

def solve_problem():
    data = extract_data_from_file(25, False)
    return data

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
