import math


class Description:
    def __init__(self, text):
        self.bullets = text.split("\n")
        self.name = self.extract_name()
        self.items = self.extract_items()
        self.operation = self.extract_operation()
        self.divisible = self.extract_divisible()
        self.true_throw_name = self.extract_true_throw_name()
        self.false_throw_name = self.extract_false_throw_name()

    def extract_name(self):
        name_bullet = self.bullets[0]
        index = name_bullet[-2:-1]
        name = "m" + index
        return name

    def extract_items(self):
        items_bullet = self.bullets[1]
        stringed_items = items_bullet.split(": ")[1]
        items = stringed_items.split(", ")
        listed_items = []
        for item in items:
            listed_items.append(int(item))
        return listed_items

    def extract_operation(self):
        operation_bullet = self.bullets[2]
        sign = operation_bullet[23]
        final_element = operation_bullet.split(f" {sign} ")[1]
        return {
            "sign": sign,
            "element": final_element
        }

    def extract_divisible(self):
        divisibility_bullet = self.bullets[3]
        number_to_test = divisibility_bullet[21:]
        return int(number_to_test)

    def extract_true_throw_name(self):
        true_throw_bullet = self.bullets[4]
        index = true_throw_bullet[-1]
        name = "m" + index
        return name

    def extract_false_throw_name(self):
        false_throw_bullet = self.bullets[5]
        index = false_throw_bullet[-1]
        name = "m" + index
        return name


class Monkey:
    def __init__(self, text):
        description = Description(text)
        self.name = description.name
        self.current_items = description.items
        self.operation = description.operation
        self.divisible = description.divisible
        self.true_throw_name = description.true_throw_name
        self.false_throw_name = description.false_throw_name
        self.inspected_items = 0

    def update_worry_level_initally(self, element):
        try:
            value = int(self.operation["element"])
        except ValueError:
            value = element
        sign = self.operation["sign"]
        if sign == "+":
            return element + value
        elif sign == "-":
            return element - value
        elif sign == "*":
            return element * value
        elif sign == "/":
            return element / value

    def lower_worry_level_after(self, element):
        division_result = element / 3
        rounded_down = math.floor(division_result)
        return rounded_down

    def alternative_lower_worry_level_after(self, element, lcm):
        remainder = element % lcm
        return remainder

    def test_divisibility(self, element):
        if element % self.divisible == 0:
            return True
        else:
            return False

    def inspect_element(self, other_monkeys):
        element = self.current_items.pop(0)
        updated_worry = self.update_worry_level_initally(element)
        lowered_worry = self.lower_worry_level_after(updated_worry)
        divisible = self.test_divisibility(lowered_worry)
        if divisible:
            monkey_to_receive = self.true_throw_name
        else:
            monkey_to_receive = self.false_throw_name
        other_monkeys[monkey_to_receive].current_items.append(lowered_worry)
        self.inspected_items += 1

    def inspect_all_elements_in_round(self, other_monkeys):
        while len(self.current_items):
            self.inspect_element(other_monkeys)

    def inspect_element_with_alternative(self, other_monkeys, lcm):
        element = self.current_items.pop(0)
        updated_worry = self.update_worry_level_initally(element)
        lowered_worry = self.alternative_lower_worry_level_after(updated_worry, lcm)
        divisible = self.test_divisibility(lowered_worry)
        if divisible:
            monkey_to_receive = self.true_throw_name
        else:
            monkey_to_receive = self.false_throw_name
        other_monkeys[monkey_to_receive].current_items.append(lowered_worry)
        self.inspected_items += 1

    def inspect_all_elements_in_round_with_alternative(self, other_monkeys, lcm):
        while len(self.current_items):
            self.inspect_element_with_alternative(other_monkeys, lcm)


def execute_full_round(monkeys):
    for monkey in monkeys.values():
        monkey.inspect_all_elements_in_round(monkeys)


def execute_multiple_rounds(rounds, monkeys):
    for _ in range(rounds):
        execute_full_round(monkeys)


def execute_full_round_with_alternative(monkeys, lcm):
    for monkey in monkeys.values():
        monkey.inspect_all_elements_in_round_with_alternative(monkeys, lcm)


def execute_multiple_rounds_with_alternative(rounds, monkeys, lcm):
    for _ in range(rounds):
        execute_full_round_with_alternative(monkeys, lcm)


def calculate_monkey_business(monkeys):
    inspections = []
    for monkey in monkeys.values():
        inspections.append(monkey.inspected_items)
    inspections.sort()
    most_active = inspections[-2:]
    product = 1
    for inspection in most_active:
        product *= inspection
    return product


def find_lowest_common_multiple(monkeys):
    multiple = 1
    for monkey in monkeys.values():
        divisor = monkey.divisible
        multiple *= divisor
    return multiple


def solve_problem():
    data = extract_data_from_file(11, True)
    monkey_descriptions = list_all_monkey_descriptions(data)
    monkeys = create_all_monkeys(monkey_descriptions)
    lcm = find_lowest_common_multiple(monkeys)
    execute_multiple_rounds_with_alternative(10000, monkeys, lcm)
    business = calculate_monkey_business(monkeys)
    return business


def create_all_monkeys(descriptions):
    monkeys = {}
    for description in descriptions:
        new_monkey = Monkey(description)
        monkeys[new_monkey.name] = new_monkey
    return monkeys


def list_all_monkey_descriptions(instructions):
    monkeys = instructions.split("\n\n")
    return monkeys


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

# Got tip to use modulo with LCM (aka, Chinese Remainder Theorem) for part 2 here:
# https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/j0avpoa/?utm_source=reddit&utm_medium=web2x&context=3
