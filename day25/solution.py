import copy

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
    def convert_to_snafu(base_5):
        last_index_3 = base_5.rfind("3")
        last_index_4 = base_5.rfind("4")
        last_index_5 = base_5.rfind("5")
        if last_index_3 == -1 and last_index_4 == -1 and last_index_5 == -1:
            return base_5
        else:
            last_indices = [last_index_3, last_index_4, last_index_5]
            last_indices.sort()
            highest_index = last_indices[-1]
            preceding_index = highest_index - 1
            beginning = base_5[:preceding_index] if preceding_index > 0 else ""
            preceding_value = int(base_5[preceding_index]) if preceding_index >= 0 else 0
            value = int(base_5[highest_index])
            ending = base_5[highest_index + 1:] if highest_index < len(base_5) - 1 else ""
            if value == 3:
                updated = "="
            elif value == 4:
                updated = "-"
            elif value == 5:
                updated = "0"
            updated_preceding = str(preceding_value + 1)
            updated_base = beginning + updated_preceding + updated + ending
            return SNAFU.convert_to_snafu(updated_base)
        
    
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
    
    def calculate_total_fuel_in_snafu(self):
        decimal = self.calculate_total_fuel_in_decimal()
        base_5 = SNAFU.convert_to_base_5(decimal, [])
        snafu = SNAFU.convert_to_snafu(base_5)
        return snafu

def solve_problem():
    data = extract_data_from_file(25, True)
    bob = Bob(data)
    total_snafu = bob.calculate_total_fuel_in_snafu()
    return total_snafu

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
