class Description:
    def __init__(self, text):
        self.text = text
        self.separate_parts()
        self.extract_name()
        self.extract_value_and_expression()
        self.extract_operation_and_dependencies()
    
    def separate_parts(self):
        parts = self.text.split(": ")
        self.parts = parts
    
    def extract_name(self):
        name = self.parts[0]
        self.name = name
    
    def extract_value_and_expression(self):
        value_or_expression = self.parts[1]
        try:
            result = int(value_or_expression)
            self.value = result
            self.expression = None
            self.is_waiting = False
        except ValueError:
            result = value_or_expression
            self.expression = result
            self.value = None
            self.is_waiting = True

    def extract_operation_and_dependencies(self):
        if self.expression is not None:
            divided_expression = self.expression.split(" ")
            self.operation = divided_expression[1]
            self.dependencies = [divided_expression[0], divided_expression[2]]
        else:
            self.operation = None
            self.dependencies = []

class Monkey:
    def __init__(self, text):
        description = Description(text)
        self.name = description.name
        self.value = description.value
        self.operation = description.operation
        self.dependencies = description.dependencies
        self.is_waiting = description.is_waiting

def solve_problem():
    data = extract_data_from_file(21, False)
    descriptions = list_all_monkey_descriptions(data)
    monkeys = create_all_monkeys(descriptions)
    return monkeys

def create_all_monkeys(descriptions):
    monkeys = []
    for description in descriptions:
        monkey = Monkey(description)
        monkeys.append(monkey)
    return monkeys

def list_all_monkey_descriptions(data):
    descriptions = data.split("\n")
    return descriptions

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
