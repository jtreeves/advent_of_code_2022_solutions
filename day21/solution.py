from sympy import symbols, solve


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
        except ValueError:
            result = value_or_expression
            self.expression = result
            self.value = None

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

    def __repr__(self):
        return f"Monkey {self.name}: {self.value}"

    def determine_final_value(self, other_monkeys):
        if self.value is None:
            dependency_monkey_values = []
            for dependency in self.dependencies:
                for other_monkey in other_monkeys:
                    if other_monkey.name == dependency:
                        dependency_monkey_values.append(other_monkey.value)
            if dependency_monkey_values[0] is not None and dependency_monkey_values[1] is not None:
                self.value = self.evaluate_expression(dependency_monkey_values[0], dependency_monkey_values[1])

    def evaluate_expression(self, first_value, second_value):
        if self.operation == "+":
            return first_value + second_value
        elif self.operation == "-":
            return first_value - second_value
        elif self.operation == "*":
            return first_value * second_value
        elif self.operation == "/":
            return int(first_value / second_value)

    def create_expression_with_variables(self):
        first_variable = symbols(self.dependencies[0])
        second_variable = symbols(self.dependencies[1])
        if self.operation == "+":
            return first_variable + second_variable
        elif self.operation == "-":
            return first_variable - second_variable
        elif self.operation == "*":
            return first_variable * second_variable
        elif self.operation == "/":
            return first_variable / second_variable

    def find_deeply_nested_expression_with_humn(self, other_monkeys, expression):
        if self.name == "humn":
            expression = symbols("humn")
        elif self.value is not None:
            expression = self.value
        else:
            expression = self.create_expression_with_variables()
            for dependency in self.dependencies:
                for other_monkey in other_monkeys:
                    if other_monkey.name == dependency:
                        if other_monkey.value is not None and other_monkey.name != "humn":
                            expression = expression.subs(symbols(dependency), other_monkey.value)
                        else:
                            expression = expression.subs(symbols(dependency), other_monkey.find_deeply_nested_expression_with_humn(other_monkeys, expression))
        return expression

    @staticmethod
    def find_needed_humn_value(monkeys):
        root_monkey = Monkey.find_root_monkey(monkeys)
        left = symbols(root_monkey.dependencies[0])
        right = symbols(root_monkey.dependencies[1])
        for monkey in monkeys:
            if monkey.name == root_monkey.dependencies[0]:
                left = left.subs(left, monkey.find_deeply_nested_expression_with_humn(monkeys, left))
            if monkey.name == root_monkey.dependencies[1]:
                right = right.subs(right, monkey.find_deeply_nested_expression_with_humn(monkeys, right))
        final_expression = left - right
        solution = solve(final_expression)
        humn_value = solution[0]
        return humn_value

    @staticmethod
    def execute_all_necessary_rounds_to_get_root_value(monkeys):
        for monkey in monkeys:
            monkey.determine_final_value(monkeys)
        root_monkey = Monkey.find_root_monkey(monkeys)
        if root_monkey.value is None:
            return Monkey.execute_all_necessary_rounds_to_get_root_value(monkeys)
        else:
            return root_monkey.value

    @staticmethod
    def find_root_monkey(monkeys):
        for monkey in monkeys:
            if monkey.name == "root":
                return monkey

    @staticmethod
    def create_all_monkeys(descriptions):
        monkeys = []
        for description in descriptions:
            monkey = Monkey(description)
            monkeys.append(monkey)
        return monkeys

    @staticmethod
    def list_all_monkey_descriptions(data):
        descriptions = data.split("\n")
        return descriptions

    @staticmethod
    def determine_root_monkey_value(data):
        descriptions = Monkey.list_all_monkey_descriptions(data)
        monkeys = Monkey.create_all_monkeys(descriptions)
        root_value = Monkey.execute_all_necessary_rounds_to_get_root_value(monkeys)
        return root_value

    @staticmethod
    def determine_humn_value_for_root_equality(data):
        descriptions = Monkey.list_all_monkey_descriptions(data)
        monkeys = Monkey.create_all_monkeys(descriptions)
        humn_value = Monkey.find_needed_humn_value(monkeys)
        return humn_value


def solve_problem():
    data = extract_data_from_file(21, True)
    root_value = Monkey.determine_root_monkey_value(data)
    humn_value = Monkey.determine_humn_value_for_root_equality(data)
    return {
        "part1": root_value,
        "part2": humn_value
    }


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
