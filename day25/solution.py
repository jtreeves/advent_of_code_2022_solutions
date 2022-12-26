import copy
import math

class SNAFU:
    def __init__(self, respresentation):
        self.digits = list(respresentation)
    
    def convert_to_decimal(self):
        total = 0
        backwards_digits = copy.deepcopy(self.digits)
        backwards_digits.reverse()
        for i in range(len(backwards_digits)):
            multiplier = 5 ** i
            value = SNAFU.determine_value_of_digit(backwards_digits[i])
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
    
    @staticmethod
    def convert_to_snafu(decimal):
        snafu = ""
        log_5 = math.log(decimal, 5)
        lower_bound = math.ceil(log_5)
        upper_bound = lower_bound + 1
        above_lower = decimal > 5 ** lower_bound
        below_upper = decimal < 5 ** upper_bound
        exact_already = log_5 % 1 == 0
        return {
            "above": above_lower,
            "below": below_upper,
            "exact": exact_already
        }
    
    @staticmethod
    def convert_to_base_5(decimal, conversion):
        remainder = decimal % 5
        conversion.insert(0, str(remainder))
        quotient = int(decimal / 5)
        if quotient == 0:
            return "".join(conversion)
        else:
            return SNAFU.convert_to_base_5(quotient, conversion)

class Bob:
    def __init__(self, directions):
        self.representations = directions.split("\n")
        self.snafu_numbers = self.create_snafu_numbers()
        self.digital_numbers = self.convert_snafu_numbers_to_digital()
    
    def create_snafu_numbers(self):
        snafu_numbers = []
        for representation in self.representations:
            snafu_number = SNAFU(representation)
            snafu_numbers.append(snafu_number)
        return snafu_numbers
    
    def convert_snafu_numbers_to_digital(self):
        digital_numbers = []
        for snafu_number in self.snafu_numbers:
            digital_number = snafu_number.convert_to_decimal()
            digital_numbers.append(digital_number)
        return digital_numbers
    
    def calculate_total_fuel_in_decimal(self):
        total = 0
        for decimal in self.digital_numbers:
            total += decimal
        return total

def solve_problem():
    data = extract_data_from_file(25, False)
    bob = Bob(data)
    for i in range(30):
        print(f"NUMBER: {i + 1}")
        print(SNAFU.convert_to_base_5(i + 1, []))
    # print(SNAFU.convert_to_base_5(353, []))
    # total_decimal = bob.calculate_total_fuel_in_decimal()
    # return total_decimal

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
